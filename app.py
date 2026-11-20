"""Site documentaire et parodique consacré à Sylvain Durif, le Christ cosmique."""

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

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        citation=choice(CITATIONS),
        pouvoirs=POUVOIRS[:4],
        chronologie=CHRONOLOGIE[-4:],
    )


@app.route("/pouvoirs")
def pouvoirs():
    return render_template("pouvoirs.html", pouvoirs=POUVOIRS)


@app.route("/programme")
def programme():
    return render_template("programme.html", programme=PROGRAMME)


@app.route("/paroles")
def paroles():
    return render_template("paroles.html", citations=CITATIONS)


@app.route("/chronologie")
def chronologie():
    return render_template("chronologie.html", chronologie=CHRONOLOGIE)


@app.route("/api/citations")
def api_citations():
    return jsonify({"citation": choice(CITATIONS), "total": len(CITATIONS)})


@app.route("/api/pouvoirs")
def api_pouvoirs():
    return jsonify({"pouvoirs": POUVOIRS})


@app.route("/api/proclamation")
def api_proclamation():
    """Génère une proclamation sur la base des titres et répliques documentés."""
    texte = (
        f"Bonjour. Je suis {choice(TITRES)}, et {choice(ACTIONS)}. {choice(FINS)}"
    )
    return jsonify({"proclamation": texte})


PAGES_INDEXABLES = [
    ("index", "1.0", "weekly"),
    ("pouvoirs", "0.9", "monthly"),
    ("programme", "0.9", "weekly"),
    ("paroles", "0.8", "monthly"),
    ("chronologie", "0.8", "monthly"),
]


@app.route("/robots.txt")
def robots():
    """Fichier d'instructions pour les robots d'indexation."""
    texte = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /api/\n"
        f"Sitemap: {request.url_root.rstrip('/')}/sitemap.xml\n"
    )
    return app.response_class(texte, mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap():
    """Plan du site XML pour Google Search Console."""
    base = request.url_root.rstrip("/")
    aujourdhui = datetime.now(timezone.utc).date().isoformat()
    lignes = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for endpoint, priorite, frequence in PAGES_INDEXABLES:
        lignes.extend(
            [
                "  <url>",
                f"    <loc>{base}{url_for(endpoint)}</loc>",
                f"    <lastmod>{aujourdhui}</lastmod>",
                f"    <changefreq>{frequence}</changefreq>",
                f"    <priority>{priorite}</priority>",
                "  </url>",
            ]
        )
    lignes.append("</urlset>")
    return app.response_class("\n".join(lignes), mimetype="application/xml")


@app.route("/sante")
def sante():
    return jsonify(
        {
            "statut": "ok",
            "message": "Le signal cosmique est stable.",
            "date": datetime.now(timezone.utc).isoformat(),
        }
    )


@app.context_processor
def injecter_contexte():
    """Injecte les crédits, l'URL de base et les données structurées."""
    base = request.url_root.rstrip("/")
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{base}/#website",
                "url": f"{base}/",
                "name": "Dossier Durif — Le Christ cosmique",
                "inLanguage": "fr",
                "description": (
                    "Dossier documentaire et parodique consacré à Sylvain Durif, "
                    "vidéaste français autoproclamé Christ cosmique et Grand Monarque."
                ),
            },
            {
                "@type": "Person",
                "@id": f"{base}/#sylvain-durif",
                "name": "Sylvain Durif",
                "alternateName": [
                    "Le Christ cosmique",
                    "Le Grand Monarque",
                    "Oriana",
                    "L'Homme Vert",
                ],
                "birthDate": "1969-08-23",
                "birthPlace": {"@type": "Place", "name": "Nantua, Ain, France"},
                "jobTitle": "Vidéaste web",
                "description": (
                    "Vidéaste français connu sous le nom de « Christ cosmique », "
                    "rendu célèbre en 2012 à Bugarach et auteur de répliques devenues mèmes."
                ),
                "sameAs": [
                    "https://fr.wikipedia.org/wiki/Sylvain_Durif",
                    "https://www.youtube.com/channel/UCX33oHPsFlI8nhR6524-_Jg",
                ],
            },
        ],
    }
    return {
        "sources": SOURCES,
        "images": IMAGES,
        "url_base": base,
        "schema": schema,
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
