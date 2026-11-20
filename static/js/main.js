/* DOSSIER DURIF — petites interactions côté navigateur */

async function charger(url) {
    const reponse = await fetch(url);
    if (!reponse.ok) throw new Error(`HTTP ${reponse.status}`);
    return reponse.json();
}

// Citation aléatoire sur l'accueil
const boutonCitation = document.getElementById("nouvelle-citation");
if (boutonCitation) {
    boutonCitation.addEventListener("click", async () => {
        try {
            const { citation } = await charger("/api/citations");
            document.getElementById("citation-hero").textContent = `« ${citation.texte} »`;
            document.querySelector(".hero-carte-source").textContent =
                `${citation.titre} — ${citation.source}`;
        } catch (erreur) {
            boutonCitation.textContent = "Signal perdu, réessayez";
        }
    });
}

// Générateur de proclamation
const boutonProclamation = document.getElementById("generer-proclamation");
if (boutonProclamation) {
    boutonProclamation.addEventListener("click", async () => {
        const sortie = document.getElementById("proclamation");
        sortie.textContent = "Réception du signal…";
        try {
            const { proclamation } = await charger("/api/proclamation");
            sortie.textContent = `« ${proclamation} »`;
        } catch (erreur) {
            sortie.textContent = "Le vaisseau est hors de portée. Réessayez.";
        }
    });
}

// Réplique aléatoire sur la page Paroles
const boutonParole = document.getElementById("parole-hasard");
if (boutonParole) {
    boutonParole.addEventListener("click", async () => {
        try {
            const { citation } = await charger("/api/citations");
            document.getElementById("citation-paroles").textContent = `« ${citation.texte} »`;
        } catch (erreur) {
            document.getElementById("citation-paroles").textContent = "Signal perdu.";
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
