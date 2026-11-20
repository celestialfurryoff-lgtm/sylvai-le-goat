"""Site documentaire et parodique consacré à Sylvain Durif, le Christ cosmique."""

from datetime import datetime, timezone
from random import choice

from flask import Flask, jsonify, render_template

from contenu import (
    ACTIONS,
    CHRONOLOGIE,
    CITATIONS,
    FINS,
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
def injecter_sources():
    return {"sources": SOURCES}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
