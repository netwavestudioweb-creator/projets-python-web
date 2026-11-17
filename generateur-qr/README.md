# 📱 Générateur de QR code

Génère des QR codes personnalisés (coordonnées, URL, texte…), en **ligne de commande** ou via une **interface web**.

## ✨ Deux interfaces

| Interface | Fichier | Usage |
|---|---|---|
| **CLI** (hors-ligne) | `qr_cli.py` | Rapide, sans serveur |
| **Web** (formulaire) | `app.py` + `templates/index.html` | Formulaire complet (nom, réseaux sociaux…) |

## 🚀 Utilisation

### Prérequis
```bash
pip install -r requirements.txt
```

### En ligne de commande
```bash
python qr_cli.py "https://exemple.com"
python qr_cli.py "Mon texte" -o mon_qr.png -s 12
```

### Interface web
```bash
python app.py
```
Puis ouvrir **http://127.0.0.1:5000**

## 📝 Note

Un dossier voisin (`… entrer 2`) ne contenait qu'une maquette HTML sans backend ; cette version-ci est la version de référence (CLI + web fonctionnels).
