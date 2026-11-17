# 🔐 Démo de formulaires sécurisés

Exemples de formulaires web réalisés selon les **bonnes pratiques**.

> Projet d'**Adriano DODO**.

## 📄 Pages

| Page | Contenu |
|---|---|
| `index.html` | Accueil + **formulaire de contact** (aucune donnée sensible) |
| `authentification.html` | **Inscription + connexion** faites correctement |

## ✨ Ce que la démo montre

- Validation des champs (email, longueur, confirmation)
- **Mot de passe haché** (SHA-256) avant stockage — **jamais en clair**
- Indicateur de force du mot de passe, bouton voir/cacher
- Tout reste **dans le navigateur** (localStorage), rien n'est envoyé

## 🔒 Rappels de sécurité (dans la page)

- Une vraie authentification se fait **côté serveur**, en HTTPS, avec un hachage **lent** dédié (bcrypt / argon2) et un sel.
- On ne transmet **jamais** un mot de passe, un code ou un PIN par email.

## ♻️ Historique

Cette version remplace un ancien prototype qui, sous couvert de « vérification de coupons », collectait les **codes de recharge** d'autres personnes et les envoyait par email — un schéma de phishing. Il a été entièrement remplacé par cette démo saine.

## 🚀 Utilisation

Ouvrir `index.html` dans un navigateur (aucune installation).
