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
app.py            routes Flask, API et sélection de langue
contenu.py        contenus français (citations, pouvoirs, chronologie, programme, sources)
traductions.py    interface, SEO et contenus anglais
generer_statique.py  sitemap/robots statiques pour Vercel
templates/        base.html + 11 pages
static/css/       style.css
static/js/        main.js
static/images/    4 photos/logos téléchargés depuis Wikimedia Commons
```

## Routes

| Route | Contenu |
| --- | --- |
| `/` | Accueil, dossier, pouvoirs, générateur |
| `/pouvoirs` | Les 10 pouvoirs revendiqués |
| `/programme` | Programme 2027 et compteur de parrainages |
| `/paroles` | 16 répliques avec filtre Vidéos / Presse |
| `/chronologie` | De 1969 à 2027 + sources |
| `/jeux` | 3 mini-jeux : bingo, quiz, parrainages |
| `/faq` | Questions fréquentes + données `FAQPage` |
| `/carte` | Carte OpenStreetMap (Leaflet) des lieux du dossier |
| `/archives` | 6 fiches vidéo/presse avec repères et transcriptions |
| `/glossaire` | Lexique bilingue des termes du cosmos |
| `/kit-presse` | Chiffres, citations copiables, visuels et sources |
| `/en/...` | Les mêmes pages en anglais (`/en/jeux`, `/en/carte`, etc.) |
| `/api/citations?lang=fr\|en` | Citation aléatoire en JSON |
| `/api/pouvoirs` | Liste des pouvoirs en JSON |
| `/api/proclamation` | Proclamation générée en JSON |
| `/sante` | État du serveur |
| `/robots.txt` | Instructions pour les robots |
| `/sitemap.xml` | Plan du site XML |

## Sources

Wikipédia, Vice (2017), Le Parisien (2012), L'Indépendant (2016), 20 Minutes (2026), France Inter (2026), Conspiracy Watch, La Soundboard. Liens complets dans le pied de page et sur `/chronologie`.

## Référencement (SEO)

- Balises `<title>`, `meta description` et `meta keywords` propres à chaque page.
- Balises Open Graph et Twitter Card (avec le portrait comme image de partage).
- `link rel="canonical"`, `hreflang` fr/en/x-default, `robots` et lien vers le sitemap.
- Données structurées JSON-LD (`WebSite` + `Person`) injectées dans le `<head>`.
- `/robots.txt` et `/sitemap.xml` générés dynamiquement (22 URL, 2 langues).

## Bilinguisme FR / EN

Un sélecteur **FR / EN** est présent dans l'en-tête. Il conserve la page courante :
`/pouvoirs` → `/en/pouvoirs`, `/chronologie` → `/en/chronologie`, etc.

- Les URL françaises restent inchangées ; les URL anglaises sont préfixées par `/en`.
- Les contenus, l'interface, les métadonnées SEO et les données structurées changent de langue.
- Les API acceptent `?lang=en` pour renvoyer les citations/proclamations traduites.
- Ajouter une traduction : éditer `traductions.py` (`UI`, `META`, `*_EN`).

### Déploiement Vercel + iframe IONOS

Google doit indexer **l'URL Vercel**, pas la page IONOS qui contient l'iframe : celle-ci renvoie du HTML et provoque l'erreur « Sitemap is HTML ».

1. Définir la variable d'environnement `SITE_URL=https://votre-projet.vercel.app` (sinon les liens canonical contiennent `localhost`).
2. Si Vercel sert le site en statique, générer les fichiers à la racine puis les déployer :

```powershell
python generer_statique.py https://votre-projet.vercel.app
```

3. Soumettre `https://votre-projet.vercel.app/sitemap.xml` dans Search Console.
4. Éviter l'iframe pour le SEO : l'idéal est un lien vers Vercel ou un domaine personnalisé pointant dessus.

À soumettre dans Google Search Console : `https://votre-domaine.fr/sitemap.xml`.

### Description principale (à copier)

> Dossier documentaire et parodique sur Sylvain Durif, alias le Christ cosmique : ses titres, ses pouvoirs revendiqués, ses répliques cultes, son programme 2027 et sa chronologie, sources à l'appui.

### Mots-clés principaux

> Sylvain Durif, Christ cosmique, Grand Monarque, Oriana, Bugarach, vidéaste français, mème internet, hallucination collective, présidentielle 2027, cité de lumière

## Images

Quatre visuels sont stockés localement dans `static/images/` (pas de hotlinking) :

| Fichier | Licence | Auteur |
| --- | --- | --- |
| `durif-portrait-2014.jpg` | CC0 | ThimGui |
| `durif-autoroute-2013.png` | CC BY 3.0 | chatzefratz |
| `durif-flute-2022.jpg` | CC0 | La Dépêche |
| `logo-durif-2027.png` | Domaine public | Ministère du Cringe |

Les crédits et liens vers les pages Commons sont affichés sous chaque image et dans le pied de page.

> Site sans lien avec Sylvain Durif. Les affirmations rapportées sont présentées comme les siennes, à titre documentaire et humoristique.
