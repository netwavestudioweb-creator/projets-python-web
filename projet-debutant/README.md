# 🎓 Projet niveau débutant

Pack de 4 mini-applications web, chacune autonome (ouvrir le `index.html` du sous-dossier).

> Projets d'**Adriano DODO**.

| Sous-projet | Description | État |
|---|---|---|
| **1 — Portfolio** | Portfolio multi-pages (accueil, à propos, compétences, contact) | ✅ Fonctionnel |
| **2 — To-Do List** | Liste de tâches | ✅ Amélioré |
| **3 — Convertisseur de devises** | Conversion entre 11 devises | ✅ Amélioré |
| **4 — Jeu du Pendu** | Jeu de lettres | ✅ Réparé |

## 🔧 Améliorations apportées

**To-Do List**
- 💾 **Persistance** (localStorage) : les tâches restent après fermeture
- ✅ Cases « terminé » (barré), **filtres** (Toutes / Actives / Terminées), compteur, « supprimer les terminées »
- Doublons `index2.html` / `style.css` supprimés

**Convertisseur de devises**
- 🌍 **Taux en direct** via une API gratuite (repli automatique sur des taux de référence hors-ligne)
- 💾 Favoris et historique **persistés** et **dédupliqués** (fini les doublons à chaque conversion)
- Validation du montant

**Jeu du Pendu**
- 🐛 **Bug bloquant corrigé** : `button:contains(...)` (sélecteur jQuery invalide en CSS) qui empêchait toute partie
- 🎨 Vrai **dessin SVG** du pendu qui se construit à chaque erreur
- Lettres **vertes/rouges**, support du **clavier physique**, compteur d'erreurs, **score**, bouton « Nouvelle partie », plus de mots

## 🚀 Utilisation

Aucune installation : ouvrir le `index.html` du sous-dossier voulu dans un navigateur. (Le convertisseur a besoin d'Internet pour les taux en direct, sinon il bascule sur des taux indicatifs.)
