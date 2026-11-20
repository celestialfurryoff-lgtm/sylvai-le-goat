"""Traductions anglaises et textes d'interface bilingues du dossier Durif.

Les affirmations rapportées restent attribuées à Sylvain Durif : la traduction
ne les présente pas comme des faits.
"""

# ---------------------------------------------------------------------------
# Textes d'interface (templates + JavaScript)
# ---------------------------------------------------------------------------

UI = {
    "fr": {
        "guillemets": ["«", "»"],
        "langue_aria": "Choisir la langue",
        "marque": "DOSSIER DURIF",
        "nav": [
            ("index", "Accueil"),
            ("pouvoirs", "Pouvoirs"),
            ("programme", "Programme 2027"),
            ("paroles", "Paroles"),
            ("chronologie", "Chronologie"),
            ("jeux", "Les Jeux"),
            ("faq", "FAQ"),
        ],
        "chrono_filtres": [
            ("toutes", "Tout"),
            ("origines", "Origines · avant 2012"),
            ("ascension", "Ascension · 2012-2016"),
            ("campagnes", "Campagnes · 2017+"),
        ],
        "jeux_eyebrow": "DOSSIER · 06",
        "jeux_h1": ("LES ", "JEUX"),
        "jeux_intro": (
            "Trois mini-jeux pour explorer le dossier : le bingo des signes, le quiz des répliques "
            "et la course aux 500 parrainages. Aucune donnée n'est envoyée : tout se joue dans votre navigateur."
        ),
        "bingo_titre": "01 / BINGO COSMIQUE",
        "bingo_desc": "Cochez les signes annoncés par le cosmos. Trois cases alignées et le signal est complet.",
        "bingo_tirer": "✳ Tirer un signe",
        "bingo_grille": "Grille de bingo",
        "bingo_affiche": "Signe annoncé",
        "bingo_score": "Signes trouvés",
        "bingo_gagne": "ALIGNEMENT COSMIQUE ! Le messie est informé.",
        "bingo_deja": "Ce signe a déjà été annoncé.",
        "quiz_titre": "02 / QUIZ : DEVINE LA RÉPLIQUE",
        "quiz_desc": "Une citation, trois titres. Un seul est authentique — les autres sont cosmiquement improvisés.",
        "quiz_question": "Question",
        "quiz_suivant": "Signe suivant →",
        "quiz_score": "Score",
        "quiz_resultat": "Réponse exacte.",
        "quiz_faux": "Pas tout à fait…",
        "quiz_fin": "Fin du quiz",
        "quiz_rejouer": "Rejouer",
        "parrainage_titre": "03 / COURSE AUX 500 PARRAINAGES",
        "parrainage_desc": (
            "Cliquez pour réunir des élus avant le 12 mars 2027. Attention aux revers du cosmos."
        ),
        "parrainage_btn": "✳ Solliciter un élu",
        "parrainage_legende": "parrainages obtenus",
        "parrainage_gagne": "500 parrainages ! Candidature officielle validée.",
        "parrainage_perte": "Hallucination collective ! −",
        "parrainage_bonus": "Un élu convaincu ! +",
        "faq_eyebrow": "DOSSIER · 07",
        "faq_h1": ("QUESTIONS ", "FRÉQUENTES"),
        "faq_intro": (
            "Les questions les plus posées sur Sylvain Durif, avec des réponses sourcées et sans adhésion "
            "aux affirmations rapportées."
        ),
        "faq": [
            ("Qui est Sylvain Durif ?", "Un vidéaste français né en 1969 à Nantua, autoproclamé « Christ cosmique » et « Grand Monarque ». Il devient connu en 2012 à Bugarach et via ses vidéos, devenues des mèmes."),
            ("Pourquoi l'appelle-t-on le Christ cosmique ?", "C'est le titre qu'il se donne lui-même. En décembre 2012, il déclare au Parisien : « J'incarne l'énergie du Christ cosmique ». La formule est reprise par la presse puis par internet."),
            ("A-t-il vraiment été abducté par un vaisseau ?", "Il le raconte dans sa vidéo la plus vue, avec un voyage sur Aldébaran à l'âge de cinq ans. Aucune source indépendante ne confirme ce récit : il est présenté ici comme son affirmation."),
            ("Que dit la phrase « hallucination collective » ?", "C'est une réplique tirée de ses vidéos, devenue un mème TikTok fin 2023, notamment avec des serpents et des singes dansants."),
            ("Participe-t-il à la présidentielle 2027 ?", "Il a annoncé sa candidature en août 2026. Pour être officiellement candidat, il doit réunir 500 parrainages d'élus avant le 12 mars 2027."),
            ("Ce site valide-t-il ces affirmations ?", "Non. C'est un dossier documentaire et parodique : les propos sont attribués à Sylvain Durif, sourcés, et présentés comme les siens, pas comme des faits."),
        ],
        "bandeau": [
            "HALLUCINATION COLLECTIVE",
            "VAISSEAU DORÉ DE 300 MÈTRES",
            "J'INCARNE L'ÉNERGIE DU CHRIST COSMIQUE",
        ],
        "footer_titre": "✳ DOSSIER DURIF",
        "footer_texte": (
            "Site documentaire et parodique, sans lien avec Sylvain Durif. "
            "Les affirmations rapportées sont les siennes et sont présentées comme telles."
        ),
        "footer_sources": "SOURCES",
        "footer_images": "CRÉDITS IMAGES",
        "footer_bas": "Archive cosmique · Fait avec curiosité et un peu de Soleil · ",
        "footer_retour": "retour au début",
        "hero_eyebrow": "ARCHIVE N°001 · NANTUA, 23 AOÛT 1969",
        "hero_sous_titre": "LE CHRIST COSMIQUE · LE GRAND MONARQUE · LE MESSIE",
        "hero_btn_pouvoirs": "Explorer ses pouvoirs →",
        "hero_btn_chronologie": "Lire la chronologie",
        "hero_img_alt": "Sylvain Durif jouant de la flûte, en 2014",
        "hero_img_legende": "PORTRAIT · 2014",
        "hero_signe": "SIGNE REÇU",
        "hero_btn_signal": "Recevoir un autre signal",
        "s01_numero": "01 / L'HOMME",
        "s01_titre": "Un vidéaste devenu phénomène internet",
        "s01_p1": (
            "Sylvain Pierre Durif, né en 1969 à Nantua, vit dans l'Aude près de Bugarach. "
            "En décembre 2012, alors que le village est au centre des prédictions de fin du monde, "
            "il déclare à <em>Le Parisien</em> : « J'incarne l'énergie du Christ cosmique ». "
            "La phrase fait le tour du web francophone."
        ),
        "s01_p2": (
            "Ses vidéos mêlent ésotérisme, récits d'abduction, théories du complot et propositions "
            "politiques. Amixem lui consacre « Analysons l'homme le plus perché du monde », Antoine "
            "Daniel l'intègre à une vidéo de près de 17 millions de vues. Fin 2023, un extrait avec "
            "des « serpents et des singes danser » devient un mème TikTok : "
            "<strong>« hallucination collective »</strong>."
        ),
        "s01_img_alt": "Sylvain Durif sur une aire d'autoroute en 2013",
        "s01_img_legende": (
            "Sylvain Durif sur une aire d'autoroute en 2013, racontant son voyage à Jérusalem "
            "et annonçant une marche pacifique. "
        ),
        "chiffres": [
            ("1969", "Naissance à Nantua"),
            ("7", "Voix aux municipales de 2014"),
            ("4 M+", "Vues sur sa vidéo la plus regardée"),
            ("13", "Répliques cultes recensées"),
        ],
        "s02_numero": "02 / LES POUVOIRS (REVENDIQUÉS)",
        "s02_titre": "Ce qu'il dit savoir faire",
        "s02_intro": (
            "Bilocation, abduction, guérison, précognition, rugissement de lion… "
            "Voici ses affirmations, telles que relayées par la presse."
        ),
        "s02_lien": "Voir les 10 pouvoirs →",
        "s03_numero": "03 / ÉMETTEUR COSMIQUE",
        "s03_titre": "Générez votre proclamation",
        "s03_intro": (
            "Un assemblage de ses titres et de ses répliques les plus connues. "
            "Aucune affirmation générée ici n'est nouvelle : tout vient du dossier."
        ),
        "s03_placeholder": "Appuyez sur le bouton pour capter le signal…",
        "s03_btn": "✳ Émettre une proclamation",
        "s04_numero": "04 / REPÈRES",
        "s04_titre": "Les derniers jalons",
        "s04_lien": "Chronologie complète →",
        "pouvoirs_eyebrow": "DOSSIER · 02",
        "pouvoirs_h1": ("LES POUVOIRS ", "REVENDIQUÉS"),
        "pouvoirs_intro": (
            "« J'ai la capacité d'aller n'importe où dans le cosmos, et la barrière physique "
            "n'a aucune importance pour moi. » — Le Parisien, décembre 2012."
        ),
        "pouvoirs_attention": (
            "Il s'agit d'affirmations de Sylvain Durif, rapportées par la presse ou tirées de ses "
            "vidéos. Elles sont présentées ici à titre documentaire et humoristique."
        ),
        "pouvoirs_img_alt": "Sylvain Durif jouant de la flûte en 2022",
        "pouvoirs_img_legende": "Sylvain Durif jouant de la flûte (2022). ",
        "pouvoirs_hors": "HORS CATÉGORIE",
        "pouvoirs_palette": "La palette des identités",
        "pouvoirs_nuage": [
            "Grand Monarque", "Christ cosmique", "Messie", "Roi", "Pape Pierre", "Oriana",
            "Sylvanus", "Homme Vert", "Merlin", "Président d'Elvita", "Médium", "Guérisseur",
        ],
        "pouvoirs_nuage_intro": (
            "Autant de titres qu'il s'est attribués, et qui reviennent dans ses annonces de "
            "candidature, notamment en 2016 et 2026."
        ),
        "programme_eyebrow": "DOSSIER · 03",
        "programme_h1": ("PROGRAMME ", "2027"),
        "programme_intro": (
            "Le 23 août 2026, il annonce sa candidature à l'élection présidentielle. "
            "Sa vidéo dépasse 800 000 vues en quelques jours."
        ),
        "programme_img_alt": "Logo de la campagne présidentielle 2027 de Sylvain Durif",
        "programme_img_legende": "Logo de campagne pour l'élection présidentielle de 2027. ",
        "programme_obstacle": "LE GRAND OBSTACLE",
        "programme_parrainages": "500 parrainages",
        "programme_obstacle_texte": (
            "Pour être officiellement candidat, il lui faut être présenté par 500 élus avant le "
            "<strong>12 mars 2027</strong>. En 2017, il n'en avait obtenu aucun. En 2014, aux "
            "municipales d'Arques, il avait récolté 7 voix."
        ),
        "programme_compteur": "parrainages confirmés à ce jour",
        "programme_mesures_numero": "SES MESURES ANNONCÉES",
        "programme_mesures_titre": "Le programme",
        "programme_mesures_intro": (
            "Mesures annoncées et relayées par la presse et les réseaux sociaux en 2026, "
            "présentées ici sans adhésion ni commentaire."
        ),
        "programme_cite_numero": "LA CITÉ DE LUMIÈRE",
        "programme_cite_titre": "Le projet de société",
        "programme_cite_p1": (
            "Depuis 2016, il porte un projet de « cité de lumière » : un centre de ressourcement "
            "et de bien-être où des personnes du monde entier apprendraient à « se guérir par "
            "elles-mêmes ». Il l'imaginait dans la haute vallée de l'Aude, au Brésil et au Québec."
        ),
        "programme_cite_p2": (
            "En 2022, il annonce vouloir racheter le Fort Queyras (Hautes-Alpes) pour 221 millions "
            "d'euros et y installer le « siège du Cosmos ». Sa profession de foi de 2014 prévoyait "
            "déjà une cellule mobile de médecine naturelle et un pôle de recherche sur la "
            "communication numérique et « télépathique »."
        ),
        "paroles_eyebrow": "DOSSIER · 04",
        "paroles_h1": ("LES ", "PAROLES"),
        "paroles_intro": (
            "Répliques tirées de ses vidéos (via La Soundboard, qui en recense 13), complétées par "
            "des propos rapportés par Le Parisien, L'Indépendant et 20 Minutes."
        ),
        "paroles_filtre_aria": "Filtrer les paroles",
        "paroles_toutes": "Toutes",
        "paroles_videos": "Vidéos",
        "paroles_presse": "Presse",
        "paroles_bonus": "BONUS",
        "paroles_bonus_titre": "Une réplique au hasard",
        "paroles_bonus_placeholder": "Cliquez pour capter une parole…",
        "paroles_bonus_btn": "✳ Nouvelle réplique",
        "chrono_eyebrow": "DOSSIER · 05",
        "chrono_h1": ("CHRONOLOGIE ", "COSMIQUE"),
        "chrono_intro": (
            "De Nantua en 1969 à la campagne présidentielle de 2027 : les étapes documentées "
            "du personnage."
        ),
        "chrono_sources_numero": "POUR ALLER PLUS LOIN",
        "chrono_sources_titre": "Les sources du dossier",
        "js_signal_perdu": "Signal perdu, réessayez",
        "js_reception": "Réception du signal…",
        "js_hors_portee": "Le vaisseau est hors de portée. Réessayez.",
        "js_parole_perdue": "Signal perdu.",
    },
    "en": {
        "guillemets": ["“", "”"],
        "langue_aria": "Choose language",
        "marque": "DURIF FILES",
        "nav": [
            ("index", "Home"),
            ("pouvoirs", "Powers"),
            ("programme", "2027 platform"),
            ("paroles", "Quotes"),
            ("chronologie", "Timeline"),
            ("jeux", "Games"),
            ("faq", "FAQ"),
        ],
        "chrono_filtres": [
            ("toutes", "All"),
            ("origines", "Origins · before 2012"),
            ("ascension", "Rise · 2012-2016"),
            ("campagnes", "Campaigns · 2017+"),
        ],
        "jeux_eyebrow": "FILE · 06",
        "jeux_h1": ("THE ", "GAMES"),
        "jeux_intro": (
            "Three mini-games to explore the dossier: sign bingo, the quote quiz and the race to 500 "
            "endorsements. Nothing is sent anywhere: everything runs in your browser."
        ),
        "bingo_titre": "01 / COSMIC BINGO",
        "bingo_desc": "Tick off the signs announced by the cosmos. Three in a row and the signal is complete.",
        "bingo_tirer": "✳ Draw a sign",
        "bingo_grille": "Bingo grid",
        "bingo_affiche": "Announced sign",
        "bingo_score": "Signs found",
        "bingo_gagne": "COSMIC ALIGNMENT! The Messiah has been notified.",
        "bingo_deja": "That sign was already announced.",
        "quiz_titre": "02 / QUIZ: GUESS THE LINE",
        "quiz_desc": "One quote, three titles. Only one is genuine — the others are cosmically improvised.",
        "quiz_question": "Question",
        "quiz_suivant": "Next sign →",
        "quiz_score": "Score",
        "quiz_resultat": "Correct.",
        "quiz_faux": "Not quite...",
        "quiz_fin": "Quiz over",
        "quiz_rejouer": "Play again",
        "parrainage_titre": "03 / RACE TO 500 ENDORSEMENTS",
        "parrainage_desc": (
            "Click to win over elected officials before 12 March 2027. Beware of cosmic setbacks."
        ),
        "parrainage_btn": "✳ Win over an official",
        "parrainage_legende": "endorsements secured",
        "parrainage_gagne": "500 endorsements! Official candidacy confirmed.",
        "parrainage_perte": "Collective hallucination! −",
        "parrainage_bonus": "An official is convinced! +",
        "faq_eyebrow": "FILE · 07",
        "faq_h1": ("FREQUENTLY ", "ASKED QUESTIONS"),
        "faq_intro": (
            "The most common questions about Sylvain Durif, with sourced answers and no endorsement "
            "of the claims reported."
        ),
        "faq": [
            ("Who is Sylvain Durif?", "A French video creator born in 1969 in Nantua, who calls himself the ‘Cosmic Christ’ and the ‘Great Monarch’. He became known in 2012 at Bugarach and through his videos, which turned into memes."),
            ("Why is he called the Cosmic Christ?", "It is a title he gave himself. In December 2012 he told Le Parisien: “I embody the energy of the Cosmic Christ”. The phrase was picked up by the press and then by the internet."),
            ("Was he really abducted by a ship?", "He tells that story in his most-viewed video, including a journey to Aldebaran at the age of five. No independent source confirms it: it is presented here as his claim."),
            ("What does ‘collective hallucination’ mean?", "It is a line from his videos that became a TikTok meme in late 2023, notably with dancing snakes and monkeys."),
            ("Is he running in the 2027 election?", "He announced his candidacy in August 2026. To become an official candidate, he needs 500 endorsements from elected officials before 12 March 2027."),
            ("Does this site endorse these claims?", "No. It is a documentary and satirical dossier: the remarks are attributed to Sylvain Durif, sourced, and presented as his words, not as facts."),
        ],
        "bandeau": [
            "COLLECTIVE HALLUCINATION",
            "A 300-METRE GOLDEN SHIP",
            "I EMBODY THE ENERGY OF THE COSMIC CHRIST",
        ],
        "footer_titre": "✳ DURIF FILES",
        "footer_texte": (
            "A documentary and satirical site, unconnected to Sylvain Durif. The claims reported "
            "are his own and are presented as such."
        ),
        "footer_sources": "SOURCES",
        "footer_images": "IMAGE CREDITS",
        "footer_bas": "Cosmic archive · Made with curiosity and a little Sun · ",
        "footer_retour": "back to the top",
        "hero_eyebrow": "ARCHIVE NO. 001 · NANTUA, 23 AUGUST 1969",
        "hero_sous_titre": "THE COSMIC CHRIST · THE GREAT MONARCH · THE MESSIAH",
        "hero_btn_pouvoirs": "Explore his powers →",
        "hero_btn_chronologie": "Read the timeline",
        "hero_img_alt": "Sylvain Durif playing the flute in 2014",
        "hero_img_legende": "PORTRAIT · 2014",
        "hero_signe": "SIGNAL RECEIVED",
        "hero_btn_signal": "Receive another signal",
        "s01_numero": "01 / THE MAN",
        "s01_titre": "A YouTuber turned internet phenomenon",
        "s01_p1": (
            "Sylvain Pierre Durif, born in 1969 in Nantua, lives in the Aude near Bugarach. "
            "In December 2012, while the village was at the centre of doomsday predictions, he told "
            "<em>Le Parisien</em>: “I embody the energy of the Cosmic Christ”. The line spread "
            "across the French-speaking web."
        ),
        "s01_p2": (
            "His videos blend esotericism, abduction stories, conspiracy theories and political "
            "proposals. Amixem dedicated “Analysons l'homme le plus perché du monde” to him, and "
            "Antoine Daniel featured him in a video with nearly 17 million views. In late 2023, a "
            "clip about “snakes and monkeys dancing” became a TikTok meme: "
            "<strong>“collective hallucination”</strong>."
        ),
        "s01_img_alt": "Sylvain Durif at a motorway service area in 2013",
        "s01_img_legende": (
            "Sylvain Durif at a motorway service area in 2013, talking about his journey to "
            "Jerusalem and announcing a peaceful march. "
        ),
        "chiffres": [
            ("1969", "Born in Nantua"),
            ("7", "Votes in the 2014 local election"),
            ("4M+", "Views on his most-watched video"),
            ("13", "Cult lines catalogued"),
        ],
        "s02_numero": "02 / POWERS (AS CLAIMED)",
        "s02_titre": "What he says he can do",
        "s02_intro": (
            "Bilocation, abduction, healing, precognition, a lion's roar... Here are his claims, "
            "as reported by the press."
        ),
        "s02_lien": "See all 10 powers →",
        "s03_numero": "03 / COSMIC TRANSMITTER",
        "s03_titre": "Generate your proclamation",
        "s03_intro": (
            "A mash-up of his best-known titles and lines. Nothing generated here is new: "
            "everything comes from the dossier."
        ),
        "s03_placeholder": "Press the button to pick up the signal…",
        "s03_btn": "✳ Broadcast a proclamation",
        "s04_numero": "04 / MILESTONES",
        "s04_titre": "The latest landmarks",
        "s04_lien": "Full timeline →",
        "pouvoirs_eyebrow": "FILE · 02",
        "pouvoirs_h1": ("CLAIMED ", "POWERS"),
        "pouvoirs_intro": (
            "“I have the ability to go anywhere in the cosmos, and physical barriers mean nothing "
            "to me.” — Le Parisien, December 2012."
        ),
        "pouvoirs_attention": (
            "These are claims made by Sylvain Durif, reported by the press or taken from his "
            "videos. They are presented here for documentary and satirical purposes."
        ),
        "pouvoirs_img_alt": "Sylvain Durif playing the flute in 2022",
        "pouvoirs_img_legende": "Sylvain Durif playing the flute (2022). ",
        "pouvoirs_hors": "UNCATEGORISED",
        "pouvoirs_palette": "The identity palette",
        "pouvoirs_nuage": [
            "Great Monarch", "Cosmic Christ", "Messiah", "King", "Pope Peter", "Oriana",
            "Sylvanus", "Green Man", "Merlin", "President of Elvita", "Medium", "Healer",
        ],
        "pouvoirs_nuage_intro": (
            "Titles he has given himself, recurring in his candidacy announcements, particularly "
            "in 2016 and 2026."
        ),
        "programme_eyebrow": "FILE · 03",
        "programme_h1": ("2027 ", "PLATFORM"),
        "programme_intro": (
            "On 23 August 2026 he announced his run for the presidency. His video passed "
            "800,000 views within days."
        ),
        "programme_img_alt": "Sylvain Durif's 2027 presidential campaign logo",
        "programme_img_legende": "Campaign logo for the 2027 presidential election. ",
        "programme_obstacle": "THE BIG OBSTACLE",
        "programme_parrainages": "500 endorsements",
        "programme_obstacle_texte": (
            "To become an official candidate, he must be nominated by 500 elected officials before "
            "<strong>12 March 2027</strong>. In 2017 he secured none. In 2014, in the Arques local "
            "election, he received 7 votes."
        ),
        "programme_compteur": "endorsements confirmed to date",
        "programme_mesures_numero": "HIS ANNOUNCED MEASURES",
        "programme_mesures_titre": "The platform",
        "programme_mesures_intro": (
            "Measures announced and relayed by the press and social media in 2026, presented here "
            "without endorsement or comment."
        ),
        "programme_cite_numero": "THE CITY OF LIGHT",
        "programme_cite_titre": "The society project",
        "programme_cite_p1": (
            "Since 2016 he has promoted a “city of light”: a retreat and wellbeing centre where "
            "people from around the world would learn to “heal themselves”. He imagined it in the "
            "upper Aude valley, in Brazil and in Quebec."
        ),
        "programme_cite_p2": (
            "In 2022 he said he wanted to buy Fort Queyras (Hautes-Alpes) for €221 million and set "
            "up the “headquarters of the Cosmos” there. His 2014 election statement already "
            "envisaged a mobile natural-medicine unit and a research centre for digital and "
            "“telepathic” communication."
        ),
        "paroles_eyebrow": "FILE · 04",
        "paroles_h1": ("THE ", "WORDS"),
        "paroles_intro": (
            "Lines taken from his videos (via La Soundboard, which lists 13), supplemented by "
            "remarks reported by Le Parisien, L'Indépendant and 20 Minutes."
        ),
        "paroles_filtre_aria": "Filter quotes",
        "paroles_toutes": "All",
        "paroles_videos": "Videos",
        "paroles_presse": "Press",
        "paroles_bonus": "BONUS",
        "paroles_bonus_titre": "A random line",
        "paroles_bonus_placeholder": "Click to pick up a line…",
        "paroles_bonus_btn": "✳ Another line",
        "chrono_eyebrow": "FILE · 05",
        "chrono_h1": ("COSMIC ", "TIMELINE"),
        "chrono_intro": (
            "From Nantua in 1969 to the 2027 presidential campaign: the documented milestones "
            "of the character."
        ),
        "chrono_sources_numero": "GOING FURTHER",
        "chrono_sources_titre": "Sources for this dossier",
        "js_signal_perdu": "Signal lost, try again",
        "js_reception": "Receiving signal…",
        "js_hors_portee": "The ship is out of range. Try again.",
        "js_parole_perdue": "Signal lost.",
    },
}

# ---------------------------------------------------------------------------
# Métadonnées SEO par page et par langue
# ---------------------------------------------------------------------------

META = {
    "fr": {
        "index": {
            "titre": "Sylvain Durif — Le Christ cosmique | Dossier documentaire",
            "description": (
                "Dossier documentaire et parodique sur Sylvain Durif, alias le Christ cosmique : "
                "ses titres, ses pouvoirs revendiqués, ses répliques cultes, son programme 2027 "
                "et sa chronologie, sources à l'appui."
            ),
            "keywords": (
                "Sylvain Durif, Christ cosmique, Grand Monarque, Oriana, Bugarach, vidéaste "
                "français, mème internet, hallucination collective, présidentielle 2027, cité de lumière"
            ),
        },
        "pouvoirs": {
            "titre": "Les pouvoirs revendiqués de Sylvain Durif — Christ cosmique",
            "description": (
                "Les pouvoirs que Sylvain Durif, le Christ cosmique, dit posséder : bilocation, "
                "abduction par un vaisseau de la Vierge Marie, précognition, guérison, illumination "
                "des cinq Bouddhas, Merlin l'enchanteur et cités d'Agartha."
            ),
            "keywords": (
                "Sylvain Durif pouvoirs, Christ cosmique bilocation, vaisseau Vierge Marie, "
                "Aldébaran, précognition, chakra, Homme Vert, Merlin l'enchanteur, Agartha, reptiliens"
            ),
        },
        "programme": {
            "titre": "Programme 2027 de Sylvain Durif, le Christ cosmique",
            "description": (
                "Le programme annoncé par Sylvain Durif, le Grand Monarque, pour la présidentielle "
                "2027 : suppression de la fiscalité, des dettes et des prisons, effacement des "
                "frontières, cité de lumière et 500 parrainages à réunir avant le 12 mars 2027."
            ),
            "keywords": (
                "Sylvain Durif programme 2027, candidat présidentielle 2027, Christ cosmique "
                "candidature, 500 parrainages, suppression impôts, cité de lumière, siège du Cosmos, "
                "Fort Queyras"
            ),
        },
        "paroles": {
            "titre": "Les répliques cultes de Sylvain Durif — Christ cosmique",
            "description": (
                "16 répliques et citations de Sylvain Durif, le Christ cosmique : « hallucination "
                "collective », vaisseaux de lumière dorée, serpents et singes sur le lit, Aldébaran "
                "et déclarations de candidature. Sources vidéo et presse."
            ),
            "keywords": (
                "Sylvain Durif citations, Christ cosmique répliques, hallucination collective, "
                "serpents et singes, vaisseaux de lumière dorée, Aldébaran, mème TikTok, La Soundboard"
            ),
        },
        "chronologie": {
            "titre": "Chronologie de Sylvain Durif, du Christ cosmique à la présidentielle 2027",
            "description": (
                "Chronologie documentée de Sylvain Durif : naissance en 1969 à Nantua, Bugarach et "
                "le Christ cosmique en 2012, Elvita, municipales de 2014, cité de lumière, mème "
                "TikTok en 2023 et candidature présidentielle 2027."
            ),
            "keywords": (
                "Sylvain Durif chronologie, Bugarach 2012 fin du monde, Elvita, Christ cosmique "
                "2012, municipales Arques 2014, Fort Queyras, hallucination collective TikTok, "
                "présidentielle 2027"
            ),
        },
        "jeux": {
            "titre": "Les Jeux — Bingo, quiz et parrainages | Sylvain Durif",
            "description": "Trois mini-jeux gratuits sur Sylvain Durif : bingo cosmique, quiz des répliques cultes et course aux 500 parrainages pour la présidentielle 2027.",
            "keywords": "jeu Sylvain Durif, bingo cosmique, quiz Christ cosmique, parrainages 2027, hallucination collective, mini-jeu web",
        },
        "faq": {
            "titre": "FAQ sur Sylvain Durif — Le Christ cosmique",
            "description": "Questions fréquentes sur Sylvain Durif : qui il est, pourquoi il se dit Christ cosmique, ses récits d'abduction, le mème de l'hallucination collective et sa candidature 2027.",
            "keywords": "FAQ Sylvain Durif, Christ cosmique questions, abduction Aldébaran, hallucination collective, candidature 2027",
        },
    },
    "en": {
        "index": {
            "titre": "Sylvain Durif — The Cosmic Christ | Documentary Dossier",
            "description": (
                "A documentary and satirical dossier on Sylvain Durif, aka the Cosmic Christ: his "
                "titles, claimed powers, cult quotes, 2027 platform and timeline, with sources."
            ),
            "keywords": (
                "Sylvain Durif, Cosmic Christ, Great Monarch, Bugarach, French YouTuber, internet "
                "meme, collective hallucination, 2027 presidential election, city of light"
            ),
        },
        "pouvoirs": {
            "titre": "The claimed powers of Sylvain Durif — Cosmic Christ",
            "description": (
                "Powers Sylvain Durif, the Cosmic Christ, says he has: bilocation, abduction by a "
                "ship of the Virgin Mary, precognition, healing, illumination from the five Buddhas, "
                "Merlin the wizard and the cities of Agartha."
            ),
            "keywords": (
                "Sylvain Durif powers, Cosmic Christ bilocation, Virgin Mary ship, Aldebaran, "
                "precognition, chakra, Green Man, Merlin, Agartha, reptilians"
            ),
        },
        "programme": {
            "titre": "Sylvain Durif — The Cosmic Christ 2027 platform",
            "description": (
                "The platform announced by Sylvain Durif, the Great Monarch, for the 2027 "
                "presidential election: scrapping taxes, debt and prisons, opening borders, a city "
                "of light and 500 endorsements needed before 12 March 2027."
            ),
            "keywords": (
                "Sylvain Durif 2027 platform, 2027 presidential candidate, Cosmic Christ candidacy, "
                "500 endorsements, abolishing taxes, city of light, headquarters of the Cosmos, "
                "Fort Queyras"
            ),
        },
        "paroles": {
            "titre": "The cult quotes of Sylvain Durif — Cosmic Christ",
            "description": (
                "16 quotes and lines from Sylvain Durif, the Cosmic Christ: “collective "
                "hallucination”, golden light ships, snakes and monkeys on the bed, Aldebaran and "
                "candidacy announcements. Video and press sources."
            ),
            "keywords": (
                "Sylvain Durif quotes, Cosmic Christ lines, collective hallucination, snakes and "
                "monkeys, golden light ships, Aldebaran, TikTok meme, La Soundboard"
            ),
        },
        "chronologie": {
            "titre": "Timeline of Sylvain Durif, from Cosmic Christ to the 2027 election",
            "description": (
                "A documented timeline of Sylvain Durif: born in 1969 in Nantua, Bugarach and the "
                "Cosmic Christ in 2012, Elvita, the 2014 local election, the city of light, a 2023 "
                "TikTok meme and the 2027 presidential run."
            ),
            "keywords": (
                "Sylvain Durif timeline, Bugarach 2012 doomsday, Elvita, Cosmic Christ 2012, Arques "
                "2014 election, Fort Queyras, collective hallucination TikTok, 2027 presidential election"
            ),
        },
        "jeux": {
            "titre": "Games — Bingo, quiz and endorsements | Sylvain Durif",
            "description": "Three free mini-games about Sylvain Durif: cosmic bingo, a cult-quote quiz and a race to 500 endorsements for the 2027 presidential election.",
            "keywords": "Sylvain Durif game, cosmic bingo, Cosmic Christ quiz, 2027 endorsements, collective hallucination, web mini-game",
        },
        "faq": {
            "titre": "FAQ about Sylvain Durif — The Cosmic Christ",
            "description": "Frequently asked questions about Sylvain Durif: who he is, why he calls himself the Cosmic Christ, his abduction stories, the collective hallucination meme and his 2027 run.",
            "keywords": "Sylvain Durif FAQ, Cosmic Christ questions, Aldebaran abduction, collective hallucination, 2027 candidacy",
        },
    },
}

# ---------------------------------------------------------------------------
# Contenus traduits
# ---------------------------------------------------------------------------

CITATIONS_EN = [
    {"texte": "I am Sylvain-Pierre Durif, the Great Monarch, the Cosmic Christ, the Messiah.", "titre": "The Cosmic Christ", "source": "La Soundboard"},
    {"texte": "So I was abducted by a ship, by one of the ships of the Virgin Mary.", "titre": "Abducted", "source": "La Soundboard"},
    {"texte": "My soul name is Oriana, and I am connected to the energy of the Green Man.", "titre": "Green Man", "source": "La Soundboard"},
    {"texte": "I have repeatedly observed ships of golden light, about 300...", "titre": "The ships of the Virgin Mary", "source": "La Soundboard"},
    {"texte": "You have an important mission to fulfil for the planet, to accompany humanity into the new dimension.", "titre": "An important mission", "source": "La Soundboard"},
    {"texte": "I have had paranormal experiences, where I dreamed of information in advance...", "titre": "Paranormal", "source": "La Soundboard"},
    {"texte": "The druids of Brocéliande I met in the forest of Paimpont told me...", "titre": "The druids of Brocéliande", "source": "La Soundboard"},
    {"texte": "At five, when I was taken, I was taken to a planet...", "titre": "Aldebaran", "source": "La Soundboard"},
    {"texte": "At the age of five I saw snakes and monkeys dancing on my bed.", "titre": "Monkeys and snakes", "source": "La Soundboard · TikTok meme, late 2023"},
    {"texte": "I received an illumination from the five Buddhas, so all my cells became golden light.", "titre": "Golden light", "source": "La Soundboard"},
    {"texte": "My throat chakra was released, I roared like a giant lion...", "titre": "Roaring like a giant lion", "source": "La Soundboard"},
    {"texte": "Connected with Quetzalcoatl, the feathered serpent god of the Toltecs.", "titre": "Bird god", "source": "La Soundboard"},
    {"texte": "If I feel like it, I can go into someone's kitchen in Montreal who invites me — I've already done it.", "titre": "The gift of ubiquity", "source": "Le Parisien, December 2012"},
    {"texte": "I am here to bring peace on earth and in the cosmos in order to establish paradise.", "titre": "The mission", "source": "L'Indépendant, February 2016"},
    {"texte": "Hello. I am the Great Monarch, the Cosmic Christ, the Messiah, the King and Pope Peter... I announce my official and public candidacy for 2027. Have a good day.", "titre": "2027 candidacy", "source": "20 Minutes, August 2026"},
    {"texte": "Collective hallucination.", "titre": "The line that became a meme", "source": "TikTok, late 2023"},
]

POUVOIRS_EN = [
    {"icone": "🚀", "titre": "Travelling anywhere in the cosmos", "texte": "He told Le Parisien in 2012 that he had the “ability to go anywhere in the cosmos”, physical barriers being irrelevant to him. His example: entering someone's kitchen in Montreal.", "source": "Le Parisien · 2012"},
    {"icone": "🛸", "titre": "Abduction at age five", "texte": "His most-viewed video (over 4 million views) tells of an abduction by a ship of the Virgin Mary and a journey to Aldebaran, the origin of his precognitive abilities.", "source": "Conspiracy Watch · YouTube video"},
    {"icone": "🔮", "titre": "Precognition and informative dreams", "texte": "He says he receives information about future events in dreams. He also reports encounters with extraterrestrials and cosmic journeys.", "source": "La Soundboard · Conspiracy Watch"},
    {"icone": "✨", "titre": "Healing powers", "texte": "In 2016 he claimed to have healing powers and presented his “city of light” project as a centre where everyone would learn to “heal themselves”.", "source": "L'Indépendant · 2016"},
    {"icone": "🦁", "titre": "The cosmic roar", "texte": "After his throat chakra was released, he says he “roared like a giant lion” in front of fifty people and received the illumination of the five Buddhas.", "source": "La Soundboard"},
    {"icone": "🧙", "titre": "Merlin, Oriana and the Green Man", "texte": "A walk in the forest of Brocéliande apparently put him “in touch with the energy of Merlin the wizard”. His soul name is said to be Oriana; he also calls himself Sylvanus or the Green Man.", "source": "Vice · 2017"},
    {"icone": "🌍", "titre": "Seeing the cities of Agartha", "texte": "He claims a network of underground cities of light called Agartha exists, and argues that political leaders are infiltrated by “reptilians”.", "source": "Vice · 2017 / La Provence · 2016"},
    {"icone": "🤖", "titre": "Inventor of artificial intelligence", "texte": "In 2026 France Inter described him as the “self-proclaimed inventor of artificial intelligence”, leading a mission of universal governance to save humanity.", "source": "France Inter · 2026"},
    {"icone": "🛠️", "titre": "Buyer, mover, detective, carpenter", "texte": "In a self-promotion video he lists these skills as qualities he believes are useful to a president of the Republic.", "source": "Vice · 2017"},
    {"icone": "👑", "titre": "King, pope and president of the cosmos", "texte": "He introduces himself as “the Great Monarch, the Cosmic Christ, the Messiah, the King, Pope Peter, the president of the planetary and cosmic governance Elvita, the president of France and of all countries on Earth and in the Cosmos”.", "source": "20 Minutes · 2026"},
]

CHRONOLOGIE_EN = [
    ("1969", "23 August", "Birth of Sylvain Pierre Durif in Nantua (Ain)."),
    ("2004", "Elvita", "Creation of the company Elvita, registered as a publisher of application software."),
    ("2008", "Quebec", "A decisive meeting with “George”, a Romanian clairvoyant who supposedly told him: “Your name is Pierre, I have been waiting for you for 20 years.”"),
    ("2012", "Bugarach", "At the heart of doomsday predictions, he told Le Parisien: “I embody the energy of the Cosmic Christ.” Elvita was registered on 22 December."),
    ("2013-2015", "Marches", "Two peaceful marches towards Israel, from which he says he was turned away."),
    ("2014", "Local election", "Candidate in Arques (Aude): 7 votes, 5.03% of the vote. His platform mentioned a natural-medicine unit and “telepathic” communication."),
    ("2016", "City of light", "A retreat centre project in the upper Aude valley, in Brazil and in Quebec. He also announced a run in the 2017 presidential election."),
    ("2017", "Vice", "61,000 YouTube subscribers, 5,540 on Twitter. His candidacy secured none of the 500 elected-official endorsements required."),
    ("2019", "Rumour", "A false report of his death circulated; he denied it in a video. A similar rumour appeared in 2024."),
    ("2022", "Headquarters of the Cosmos", "A plan to buy Fort Queyras (Hautes-Alpes) for €221 million to install the “headquarters of the Cosmos” there."),
    ("2023", "Collective hallucination", "A video clip with dancing snakes and monkeys became a TikTok meme."),
    ("2026", "Back on the campaign trail", "A 2027 candidacy announced (video with over 800,000 views), a debate with Francis Lalanne and a rally in Montauban on 18 November."),
    ("2027", "12 March", "Endorsement deadline: 500 elected officials must nominate him for him to become an official candidate."),
]

PROGRAMME_EN = [
    {"icone": "💰", "titre": "Abolish taxation", "texte": "Scrapping income tax and taxation, announced in his 2027 platform."},
    {"icone": "💸", "titre": "Erase debts", "texte": "Writing off debt, presented as an act of peaceful governance."},
    {"icone": "🚓", "titre": "Abolish prisons", "texte": "The abolition of prisons features among the announced measures."},
    {"icone": "🌐", "titre": "Erase borders", "texte": "The disappearance of borders within a planetary and cosmic governance framework."},
    {"icone": "🕊️", "titre": "Peace on Earth and in the cosmos", "texte": "The thread running through his candidacies since 2016: “establishing paradise” and a “new universal governance”."},
    {"icone": "🏯", "titre": "The city of light", "texte": "A retreat and wellbeing centre where people would learn to heal themselves, envisioned in the Aude, Brazil and Quebec."},
]

TITRES_EN = [
    "the Great Monarch",
    "the Cosmic Christ",
    "the Messiah",
    "the King and Pope Peter",
    "the Green Man",
    "Oriana",
    "the president of the peaceful planetary and cosmic governance Elvita",
]

ACTIONS_EN = [
    "I announce my official and public candidacy",
    "I am coming to install the headquarters of the Cosmos",
    "I was abducted by a ship of the Virgin Mary",
    "I roared like a giant lion",
    "I am preparing the city of light",
    "I am broadcasting the illumination of the five Buddhas",
    "I am walking towards Aldebaran",
]

FINS_EN = [
    "Have a good day.",
    "Collective hallucination.",
    "Peace on Earth and in the cosmos.",
    "Follow the 300-metre golden ship.",
    "The mission is important for the planet.",
]

IMAGES_EN = [
    "Sylvain Durif playing the flute (2014)",
    "At a motorway service area, in 2013",
    "Playing the flute (2022)",
    "2027 presidential campaign logo",
]

SOURCES_EN = [
    ("Wikipedia — Sylvain Durif", "https://fr.wikipedia.org/wiki/Sylvain_Durif"),
    ("Vice — The life and work of the Cosmic Christ", "https://www.vice.com/fr/article/la-vie-et-l-oeuvre-du-christ-cosmique-sylvain-durif/"),
    ("20 Minutes — Who is Sylvain Durif?", "https://www.20minutes.fr/politique/4241053-20260826-presidentielle-2027-sylvain-durif-christ-cosmique-veut-presenter"),
    ("France Inter — Les 80'' of 22 October 2026", "https://www.radiofrance.fr/franceinter/podcasts/les-80/les-80-du-jeudi-22-octobre-2026-9573504"),
    ("Conspiracy Watch — Sylvain Durif profile", "https://www.conspiracywatch.info/notice/sylvain-durif"),
    ("La Soundboard — 13 cult lines", "https://lasoundboard.fr/repliques/christ-cosmique/"),
]
