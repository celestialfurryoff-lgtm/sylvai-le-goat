/* DOSSIER DURIF — petites interactions côté navigateur (FR/EN) */

const i18n = window.DURIF_I18N || { langue: "fr", guillemets: ["«", "»"] };
const [ouverture, fermeture] = i18n.guillemets;

async function charger(url) {
    const reponse = await fetch(`${url}?lang=${i18n.langue}`);
    if (!reponse.ok) throw new Error(`HTTP ${reponse.status}`);
    return reponse.json();
}

// Citation aléatoire sur l'accueil
const boutonCitation = document.getElementById("nouvelle-citation");
if (boutonCitation) {
    boutonCitation.addEventListener("click", async () => {
        try {
            const { citation } = await charger("/api/citations");
            document.getElementById("citation-hero").textContent =
                `${ouverture} ${citation.texte} ${fermeture}`;
            document.querySelector(".hero-carte-source").textContent =
                `${citation.titre} — ${citation.source}`;
        } catch (erreur) {
            boutonCitation.textContent = i18n.langue === "fr"
                ? "Signal perdu, réessayez"
                : "Signal lost, try again";
        }
    });
}

// Générateur de proclamation
const boutonProclamation = document.getElementById("generer-proclamation");
if (boutonProclamation) {
    boutonProclamation.addEventListener("click", async () => {
        const sortie = document.getElementById("proclamation");
        sortie.textContent = i18n.langue === "fr"
            ? "Réception du signal…"
            : "Receiving signal…";
        try {
            const { proclamation } = await charger("/api/proclamation");
            sortie.textContent = `${ouverture} ${proclamation} ${fermeture}`;
        } catch (erreur) {
            sortie.textContent = i18n.langue === "fr"
                ? "Le vaisseau est hors de portée. Réessayez."
                : "The ship is out of range. Try again.";
        }
    });
}

// Réplique aléatoire sur la page Paroles
const boutonParole = document.getElementById("parole-hasard");
if (boutonParole) {
    boutonParole.addEventListener("click", async () => {
        try {
            const { citation } = await charger("/api/citations");
            document.getElementById("citation-paroles").textContent =
                `${ouverture} ${citation.texte} ${fermeture}`;
        } catch (erreur) {
            document.getElementById("citation-paroles").textContent = i18n.langue === "fr"
                ? "Signal perdu."
                : "Signal lost.";
        }
    });
}

// Filtre des répliques
const filtres = document.querySelectorAll(".filtre");
if (filtres.length) {
    filtres.forEach((filtre) => {
        filtre.addEventListener("click", () => {
            filtres.forEach((f) => f.classList.remove("actif"));
            filtre.classList.add("actif");
            const cible = filtre.dataset.filtre;
            document.querySelectorAll(".citation").forEach((citation) => {
                const visible = cible === "toutes" || citation.dataset.categorie === cible;
                citation.classList.toggle("masque", !visible);
            });
        });
    });
}

// Filtre de la chronologie par période
const filtresChrono = document.querySelectorAll(".filtre-chrono");
if (filtresChrono.length) {
    filtresChrono.forEach((filtre) => {
        filtre.addEventListener("click", () => {
            const periode = filtre.dataset.periode;
            document.querySelectorAll(".timeline-item").forEach((item) => {
                const visible = periode === "toutes" || item.dataset.periode === periode;
                item.classList.toggle("masque", !visible);
            });
        });
    });
}

// ---------------------------------------------------------------------------
// Les Jeux : bingo, quiz et course aux parrainages (100 % côté navigateur)
// ---------------------------------------------------------------------------

const donneesJeux = document.getElementById("donnees-jeux");
if (donneesJeux) {
    const citationsJeu = JSON.parse(donneesJeux.textContent);
    const melanger = (liste) => [...liste].sort(() => Math.random() - 0.5);

    /* --- 1. Bingo cosmique --- */
    const bingo = document.getElementById("jeu-bingo");
    const grille = document.getElementById("bingo-grille");
    const bingoAffiche = document.getElementById("bingo-affiche");
    const bingoScore = document.getElementById("bingo-score");
    const bingoMessage = document.getElementById("bingo-message");
    const signes = melanger(citationsJeu).slice(0, 8);
    const marques = Array(9).fill(false);
    const lignesGagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    ];
    let enAttente = null;
    let termine = false;
    const tirees = new Set();

    function dessinerGrille() {
        grille.innerHTML = "";
        marques.forEach((marque, index) => {
            const caseElement = document.createElement(index === 4 ? "div" : "button");
            caseElement.className = "case-bingo" + (marque ? " marquee" : "");
            if (index === 4) {
                caseElement.textContent = "✳";
                caseElement.setAttribute("aria-label", "case centrale");
            } else {
                const signe = signes[index < 4 ? index : index - 1];
                caseElement.textContent = signe.titre;
                caseElement.type = "button";
                caseElement.setAttribute("aria-pressed", String(marque));
                caseElement.addEventListener("click", () => {
                    if (termine || index === 4) return;
                    if (marque) {
                        bingoMessage.textContent = bingo.dataset.deja;
                        return;
                    }
                    if (enAttente && enAttente.titre === signe.titre) {
                        marques[index] = true;
                        enAttente = null;
                        bingoAffiche.textContent = "✳";
                        bingoScore.textContent = String(marques.filter(Boolean).length - 1);
                        bingoMessage.textContent = "";
                        dessinerGrille();
                        const gagne = lignesGagnantes.some((ligne) => ligne.every((i) => marques[i]));
                        if (gagne) {
                            termine = true;
                            bingoMessage.textContent = bingo.dataset.gagne;
                        }
                    } else {
                        bingoMessage.textContent = "";
                    }
                });
            }
            grille.appendChild(caseElement);
        });
    }

    dessinerGrille();
    document.getElementById("bingo-tirer").addEventListener("click", () => {
        if (termine) return;
        if (tirees.size === signes.length) tirees.clear();
        const restants = signes.map((_, i) => i).filter((i) => !tirees.has(i));
        const choisi = restants[Math.floor(Math.random() * restants.length)];
        tirees.add(choisi);
        enAttente = signes[choisi];
        bingoAffiche.textContent = enAttente.titre;
        bingoMessage.textContent = "";
    });

    /* --- 2. Quiz : devine la réplique --- */
    const quiz = document.getElementById("jeu-quiz");
    const quizIndex = document.getElementById("quiz-index");
    const quizCitation = document.getElementById("quiz-citation");
    const quizOptions = document.getElementById("quiz-options");
    const quizScore = document.getElementById("quiz-score");
    const quizMessage = document.getElementById("quiz-message");
    const quizSuivant = document.getElementById("quiz-suivant");
    const questions = melanger(citationsJeu).slice(0, 8);
    let indexQuestion = 0;
    let scoreQuiz = 0;
    let repondu = false;

    function dessinerQuestion() {
        const question = questions[indexQuestion];
        quizIndex.textContent = `${indexQuestion + 1}/${questions.length}`;
        quizCitation.textContent = `${ouverture} ${question.texte} ${fermeture}`;
        quizOptions.innerHTML = "";
        const titres = melanger(
            [question.titre, ...melanger(citationsJeu.filter((c) => c.titre !== question.titre)).slice(0, 2).map((c) => c.titre)]
        );
        repondu = false;
        quizMessage.textContent = "";
        quizSuivant.hidden = true;
        titres.forEach((titre) => {
            const bouton = document.createElement("button");
            bouton.className = "btn option-quiz";
            bouton.type = "button";
            bouton.textContent = titre;
            bouton.addEventListener("click", () => {
                if (repondu) return;
                repondu = true;
                const juste = titre === question.titre;
                if (juste) scoreQuiz += 1;
                quizScore.textContent = String(scoreQuiz);
                quizMessage.textContent = juste ? quiz.dataset.resultat : quiz.dataset.faux;
                [...quizOptions.children].forEach((b) => {
                    b.disabled = true;
                    if (b.textContent === question.titre) b.classList.add("bonne-reponse");
                });
                if (!juste) bouton.classList.add("mauvaise-reponse");
                quizSuivant.hidden = false;
                quizSuivant.textContent = indexQuestion === questions.length - 1
                    ? quiz.dataset.rejouer
                    : quiz.dataset.suivant;
            });
            quizOptions.appendChild(bouton);
        });
    }

    dessinerQuestion();
    quizSuivant.addEventListener("click", () => {
        if (indexQuestion === questions.length - 1) {
            indexQuestion = 0;
            scoreQuiz = 0;
            quizScore.textContent = "0";
            quizMessage.textContent = quiz.dataset.fin;
        } else {
            indexQuestion += 1;
        }
        dessinerQuestion();
    });

    /* --- 3. Course aux 500 parrainages --- */
    const parrainage = document.getElementById("jeu-parrainage");
    const parrainageNombre = document.getElementById("parrainage-nombre");
    const parrainageJauge = document.getElementById("parrainage-jauge");
    const parrainageBouton = document.getElementById("parrainage-btn");
    const parrainageMessage = document.getElementById("parrainage-message");
    let parrainages = 0;

    function afficherParrainages() {
        parrainageNombre.innerHTML = `${parrainages}<small>/500</small>`;
        parrainageJauge.style.width = `${Math.min(100, (parrainages / 500) * 100)}%`;
    }

    parrainageBouton.addEventListener("click", () => {
        if (parrainages >= 500) return;
        const tirage = Math.random();
        if (tirage < 0.7) {
            const gain = 1 + Math.floor(Math.random() * 3);
            parrainages += gain;
            parrainageMessage.textContent = `${parrainage.dataset.bonus}${gain}`;
        } else if (tirage < 0.9) {
            const perte = Math.min(parrainages, 1 + Math.floor(Math.random() * 5));
            parrainages -= perte;
            parrainageMessage.textContent = `${parrainage.dataset.perte}${perte}`;
        } else {
            parrainages += 5;
            parrainageMessage.textContent = `${parrainage.dataset.bonus}5`;
        }
        if (parrainages >= 500) {
            parrainages = 500;
            parrainageMessage.textContent = parrainage.dataset.gagne;
            parrainageBouton.disabled = true;
        }
        afficherParrainages();
    });
}

// Copie des citations du kit presse
document.querySelectorAll("[data-copier]").forEach((bouton) => {
    bouton.addEventListener("click", async () => {
        const cible = document.getElementById(bouton.dataset.copier);
        if (!cible) return;
        try {
            await navigator.clipboard.writeText(cible.innerText.trim());
            bouton.textContent = bouton.dataset.succes;
        } catch (erreur) {
            bouton.textContent = bouton.dataset.echec;
        }
    });
});
