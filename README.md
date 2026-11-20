# Dossier Durif — Le Christ cosmique

Site web Flask (Python) documentaire et parodique consacré à **Sylvain Durif** (une seule « f »), vidéaste français autoproclamé « Christ cosmique » et « Grand Monarque ».

Refonte complète du projet initial : contenus réels, navigation en 5 pages, esthétique « archive cosmique », générateur de proclamations et API JSON.

## Lancer

```powershell
cd sylvain-durif-cosmos
.\.venv\Scripts\Activate.ps1
python app.py
```

Puis <http://127.0.0.1:5000>.

Environnement virtuel déjà présent dans le dossier. Pour le recréer :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Structure

```
app.py            routes Flask et API
contenu.py        citations, pouvoirs, chronologie, programme, sources
templates/        base.html + 5 pages
static/css/       style.css
static/js/        main.js
```

## Routes

| Route | Contenu |
| --- | --- |
| `/` | Accueil, dossier, pouvoirs, générateur |
| `/pouvoirs` | Les 10 pouvoirs revendiqués |
| `/programme` | Programme 2027 et compteur de parrainages |
| `/paroles` | 16 répliques avec filtre Vidéos / Presse |
| `/chronologie` | De 1969 à 2027 + sources |
| `/api/citations` | Citation aléatoire en JSON |
| `/api/pouvoirs` | Liste des pouvoirs en JSON |
| `/api/proclamation` | Proclamation générée en JSON |
| `/sante` | État du serveur |

## Sources

Wikipédia, Vice (2017), Le Parisien (2012), L'Indépendant (2016), 20 Minutes (2026), France Inter (2026), Conspiracy Watch, La Soundboard. Liens complets dans le pied de page et sur `/chronologie`.

> Site sans lien avec Sylvain Durif. Les affirmations rapportées sont présentées comme les siennes, à titre documentaire et humoristique.
