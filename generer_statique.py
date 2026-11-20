"""Génère un sitemap.xml et un robots.txt statiques pour un déploiement Vercel.

Usage :
    python generer_statique.py https://votre-projet.vercel.app

La variable d'environnement SITE_URL est utilisée si aucun argument n'est fourni.
Les fichiers sont écrits à la racine du projet (à déployer avec le site).
"""

import os
import sys
from datetime import datetime, timezone

PAGES = [
    ("", "1.0", "weekly"),
    ("pouvoirs", "0.9", "monthly"),
    ("programme", "0.9", "weekly"),
    ("paroles", "0.8", "monthly"),
    ("chronologie", "0.8", "monthly"),
    ("jeux", "0.7", "monthly"),
    ("faq", "0.7", "monthly"),
]
LANGUES = ("fr", "en")


def url_page(base, langue, chemin):
    if langue == "en":
        return f"{base}/en/{chemin}".rstrip("/") + ("/" if not chemin else "")
    return f"{base}/{chemin}".rstrip("/") + ("/" if not chemin else "")


def generer(domaine):
    base = domaine.rstrip("/")
    aujourdhui = datetime.now(timezone.utc).date().isoformat()
    lignes = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for langue in LANGUES:
        for chemin, priorite, frequence in PAGES:
            lignes.extend(
                [
                    "  <url>",
                    f"    <loc>{url_page(base, langue, chemin)}</loc>",
                    f"    <lastmod>{aujourdhui}</lastmod>",
                    f"    <changefreq>{frequence}</changefreq>",
                    f"    <priority>{priorite}</priority>",
                ]
            )
            for alternative in LANGUES:
                lignes.append(
                    f'    <xhtml:link rel="alternate" hreflang="{alternative}" '
                    f'href="{url_page(base, alternative, chemin)}"/>'
                )
            lignes.append("  </url>")
    lignes.append("</urlset>")

    with open("sitemap.xml", "w", encoding="utf-8") as fichier:
        fichier.write("\n".join(lignes) + "\n")
    with open("robots.txt", "w", encoding="utf-8") as fichier:
        fichier.write(
            "User-agent: *\nAllow: /\nDisallow: /api/\n"
            f"Sitemap: {base}/sitemap.xml\n"
        )
    print(f"sitemap.xml et robots.txt générés pour {base} ({len(PAGES) * len(LANGUES)} URL)")


if __name__ == "__main__":
    domaine = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("SITE_URL", "")
    if not domaine or "EXEMPLE" in domaine.upper():
        raise SystemExit(
            "Indiquez le domaine public : python generer_statique.py https://votre-projet.vercel.app"
        )
    generer(domaine)
