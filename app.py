"""Site bilingue (FR/EN) documentaire et parodique consacré à Sylvain Durif."""

import os
from datetime import datetime, timezone
from random import choice

from flask import Flask, jsonify, render_template, request, url_for

from contenu import (
    ACTIONS,
    CHRONOLOGIE,
    CITATIONS,
    FINS,
    IMAGES,
    POUVOIRS,
    PROGRAMME,
    SOURCES,
    TITRES,
)
from traductions import (
    ACTIONS_EN,
    CHRONOLOGIE_EN,
    CITATIONS_EN,
    FINS_EN,
    IMAGES_EN,
    META,
    POUVOIRS_EN,
    PROGRAMME_EN,
    SOURCES_EN,
    TITRES_EN,
    UI,
)

app = Flask(__name__)

# Sur Vercel, définir SITE_URL=https://votre-projet.vercel.app pour éviter
# les URL localhost dans les canonical, le sitemap et les données structurées.
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")
LANGUES = ("fr", "en")

DONNEES = {
    "fr": {
        "citations": CITATIONS,
        "pouvoirs": POUVOIRS,
        "chronologie": CHRONOLOGIE,
        "programme": PROGRAMME,
        "titres": TITRES,
        "actions": ACTIONS,
        "fins": FINS,
        "sources": SOURCES,
        "images": IMAGES,
    },
    "en": {
        "citations": CITATIONS_EN,
        "pouvoirs": POUVOIRS_EN,
        "chronologie": CHRONOLOGIE_EN,
        "programme": PROGRAMME_EN,
        "titres": TITRES_EN,
        "actions": ACTIONS_EN,
        "fins": FINS_EN,
        "sources": SOURCES_EN,
        "images": [
            {**image, "legende": legende}
            for image, legende in zip(IMAGES, IMAGES_EN)
        ],
    },
}

PREFIXES = {"fr": "Bonjour.", "en": "Hello."}


def langue_courante():
    """Langue déduite de l'URL (/en/... => en, sinon fr)."""
    return (request.view_args or {}).get("langue", "fr")


def rendu(modele, langue, **contexte):
    """Rend un template avec les données et l'interface de la langue donnée."""
    donnees = dict(DONNEES[langue])
    donnees.update(contexte)
    return render_template(modele, langue=langue, **donnees)


# ---------------------------------------------------------------------------
# Pages : les URL FR restent inchangées, les URL EN sont préfixées par /en
# ---------------------------------------------------------------------------

@app.route("/", defaults={"langue": "fr"})
@app.route("/en/", defaults={"langue": "en"})
def index(langue):
    donnees = DONNEES[langue]
    return rendu(
        "index.html",
        langue,
        citation=choice(donnees["citations"]),
        pouvoirs=donnees["pouvoirs"][:4],
        chronologie=donnees["chronologie"][-4:],
    )


@app.route("/pouvoirs", defaults={"langue": "fr"})
@app.route("/en/pouvoirs", defaults={"langue": "en"})
def pouvoirs(langue):
    return rendu("pouvoirs.html", langue)


@app.route("/programme", defaults={"langue": "fr"})
@app.route("/en/programme", defaults={"langue": "en"})
def programme(langue):
    return rendu("programme.html", langue)


@app.route("/paroles", defaults={"langue": "fr"})
@app.route("/en/paroles", defaults={"langue": "en"})
def paroles(langue):
    return rendu("paroles.html", langue)


@app.route("/chronologie", defaults={"langue": "fr"})
@app.route("/en/chronologie", defaults={"langue": "en"})
def chronologie(langue):
    return rendu("chronologie.html", langue)


@app.route("/jeux", defaults={"langue": "fr"})
@app.route("/en/jeux", defaults={"langue": "en"})
def jeux(langue):
    return rendu("jeux.html", langue)


@app.route("/faq", defaults={"langue": "fr"})
@app.route("/en/faq", defaults={"langue": "en"})
def faq(langue):
    return rendu("faq.html", langue)


# ---------------------------------------------------------------------------
# API : ?lang=en permet au JavaScript de rester dans la langue courante
# ---------------------------------------------------------------------------

@app.route("/api/citations")
def api_citations():
    langue = request.args.get("lang", "fr")
    if langue not in LANGUES:
        langue = "fr"
    donnees = DONNEES[langue]
    return jsonify(
        {"citation": choice(donnees["citations"]), "total": len(donnees["citations"])}
    )


@app.route("/api/pouvoirs")
def api_pouvoirs():
    langue = request.args.get("lang", "fr")
    if langue not in LANGUES:
        langue = "fr"
    return jsonify({"pouvoirs": DONNEES[langue]["pouvoirs"]})


@app.route("/api/proclamation")
def api_proclamation():
    """Assemblage de titres et de répliques documentés, dans la langue choisie."""
    langue = request.args.get("lang", "fr")
    if langue not in LANGUES:
        langue = "fr"
    donnees = DONNEES[langue]
    titre = choice(donnees["titres"])
    action = choice(donnees["actions"])
    fin = choice(donnees["fins"])
    if langue == "en":
        texte = f"Hello. I am {titre}, and {action}. {fin}"
    else:
        texte = f"Bonjour. Je suis {titre}, et {action}. {fin}"
    return jsonify({"proclamation": texte})


# ---------------------------------------------------------------------------
# Référencement : sitemap bilingue, hreflang, données structurées
# ---------------------------------------------------------------------------

PAGES_INDEXABLES = [
    ("index", "1.0", "weekly"),
    ("pouvoirs", "0.9", "monthly"),
    ("programme", "0.9", "weekly"),
    ("paroles", "0.8", "monthly"),
    ("chronologie", "0.8", "monthly"),
    ("jeux", "0.7", "monthly"),
    ("faq", "0.7", "monthly"),
]


@app.route("/robots.txt")
def robots():
    """Instructions pour les robots d'indexation."""
    texte = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /api/\n"
        f"Sitemap: {request.url_root.rstrip('/')}/sitemap.xml\n"
    )
    return app.response_class(texte, mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap():
    """Plan du site XML avec une entrée par langue et liens hreflang."""
    base = SITE_URL or request.url_root.rstrip("/")
    aujourdhui = datetime.now(timezone.utc).date().isoformat()
    lignes = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for langue in LANGUES:
        for endpoint, priorite, frequence in PAGES_INDEXABLES:
            url = base + url_for(endpoint, langue=langue)
            lignes.extend(
                [
                    "  <url>",
                    f"    <loc>{url}</loc>",
                    f"    <lastmod>{aujourdhui}</lastmod>",
                    f"    <changefreq>{frequence}</changefreq>",
                    f"    <priority>{priorite}</priority>",
                ]
            )
            for alternative in LANGUES:
                lignes.append(
                    f'    <xhtml:link rel="alternate" hreflang="{alternative}" '
                    f'href="{base}{url_for(endpoint, langue=alternative)}"/>'
                )
            lignes.append("  </url>")
    lignes.append("</urlset>")
    return app.response_class("\n".join(lignes), mimetype="application/xml")


@app.route("/sante")
def sante():
    return jsonify(
        {
            "statut": "ok",
            "message": (
                "Le signal cosmique est stable."
                if langue_courante() == "fr"
                else "The cosmic signal is stable."
            ),
            "date": datetime.now(timezone.utc).isoformat(),
        }
    )


@app.context_processor
def injecter_contexte():
    """Injecte UI, SEO, crédits et helpers de langue dans tous les templates."""
    langue = langue_courante()
    base = SITE_URL or request.url_root.rstrip("/")

    def url_locale(endpoint, lng=None):
        return base + url_for(endpoint, langue=lng or langue)

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{base}/#website",
                "url": f"{base}/" if langue == "fr" else f"{base}/en/",
                "name": (
                    "Dossier Durif — Le Christ cosmique"
                    if langue == "fr"
                    else "Durif Files — The Cosmic Christ"
                ),
                "inLanguage": langue,
                "description": (
                    "Dossier documentaire et parodique consacré à Sylvain Durif, vidéaste français autoproclamé Christ cosmique."
                    if langue == "fr"
                    else "Documentary and satirical dossier on Sylvain Durif, a French YouTuber who calls himself the Cosmic Christ."
                ),
            },
            {
                "@type": "Person",
                "@id": f"{base}/#sylvain-durif",
                "name": "Sylvain Durif",
                "alternateName": [
                    "Le Christ cosmique",
                    "The Cosmic Christ",
                    "Le Grand Monarque",
                    "The Great Monarch",
                    "Oriana",
                ],
                "birthDate": "1969-08-23",
                "birthPlace": {"@type": "Place", "name": "Nantua, Ain, France"},
                "jobTitle": "Vidéaste web" if langue == "fr" else "Web video creator",
                "description": (
                    "Vidéaste français connu sous le nom de « Christ cosmique », rendu célèbre en 2012 à Bugarach."
                    if langue == "fr"
                    else "French video creator known as the ‘Cosmic Christ’, who rose to fame in 2012 at Bugarach."
                ),
                "sameAs": [
                    "https://fr.wikipedia.org/wiki/Sylvain_Durif",
                    "https://www.youtube.com/channel/UCX33oHPsFlI8nhR6524-_Jg",
                ],
            },
        ],
    }
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {"@type": "Answer", "text": reponse},
            }
            for question, reponse in UI[langue]["faq"]
        ],
    }
    return {
        "langue": langue,
        "t": UI[langue],
        "faq_schema": faq_schema,
        "meta": META[langue],
        "sources": DONNEES[langue]["sources"],
        "images": DONNEES[langue]["images"],
        "url_base": base,
        "url_locale": url_locale,
        "schema": schema,
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
