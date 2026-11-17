# 💰 Gestion des dépenses et épargne

Application de bureau (Tkinter) pour estimer son budget quotidien, son épargne, et visualiser la répartition de ses dépenses sous forme de camembert.

## ✨ Fonctionnalités

- Saisie du revenu, de la durée, de l'objectif d'épargne et des dépenses
- Calcul du budget quotidien, du restant et de l'épargne possible
- Graphique camembert de la répartition des dépenses

## 🚀 Utilisation

### Prérequis
```bash
pip install -r requirements.txt
```

```bash
python main.py
```

## 🔧 Corrections apportées

- Compatibilité **Pillow 10+** (`Image.ANTIALIAS` remplacé par `Resampling.LANCZOS`)
- L'icône `icon.png` est désormais **optionnelle** (plus de plantage si absente)
- Gardes ajoutées : saisies non numériques et graphique sans dépense
