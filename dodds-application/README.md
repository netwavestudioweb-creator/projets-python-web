# 🖥️ DODDS APPLICATION

Petite application de bureau (**Tkinter**) : connexion par identifiant / mot de passe, puis ouverture d'une **page web de bienvenue personnalisée** dans le navigateur.

> Projet d'**Adriano DODO**.

## ✨ Fonctionnalités

- Fenêtre de connexion stylée
- Validation à la touche **Entrée** ou par le bouton
- Page d'accueil HTML générée et ouverte dans le navigateur, **personnalisée au nom** de l'utilisateur

## 🔒 Sécurité

Les mots de passe ne sont **pas stockés en clair** : le code ne garde que leur **empreinte SHA-256** et compare les empreintes à la connexion.

> Comptes de démonstration : `DODO`, `MARIANO`, `ADRIANO` (mots de passe d'origine conservés). Pour un vrai usage, voir `SecurePassGen` (Suite Cybersécurité) pour les bonnes pratiques.

## 🔧 Améliorations apportées

- 🔐 Mots de passe en clair → **empreintes SHA-256**
- 🎨 Interface Tkinter nettoyée (mise en page cohérente, couleurs)
- 🖊️ Page d'accueil personnalisée (salue l'utilisateur) au lieu d'un simple « BIENVENUE »
- 🐛 `page.close` (jamais appelé) corrigé ; fichier généré en UTF-8 ; fautes corrigées
- Fichier redondant `pagenet.py` supprimé

## 🚀 Utilisation

### Prérequis
- Python 3.8+ (Tkinter est inclus avec Python)

```bash
python sys1.py
```
