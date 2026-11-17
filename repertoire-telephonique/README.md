# 📞 Répertoire téléphonique

Gestionnaire de contacts en console, avec stockage **JSON** persistant.

## ✨ Fonctionnalités

- **Ajouter** un contact (avec confirmation si le nom existe déjà)
- **Rechercher** par nom ou partie du nom (insensible à la casse)
- **Lister** tous les contacts (triés)
- **Supprimer** un contact
- Sauvegarde automatique dans `contacts.json`

## 🚀 Utilisation

### Prérequis
- Python 3.8+ (aucune dépendance externe)

```bash
python contact.py
```

## 📝 Note

Version refondue : l'ancienne basait le stockage sur `contact.txt` (recherche boguée, pas de suppression). Les données sont désormais dans `contacts.json`. Le fichier `contact.txt` d'origine est conservé pour mémoire.
