# 🎬 Traducteur de vidéo

Extrait la parole d'une vidéo, la reconnaît, puis la **traduit en français** et enregistre la transcription.

## 🔗 Pipeline

```
Vidéo → (moviepy) audio → (SpeechRecognition) texte → (googletrans) français → fichier
```

## 🚀 Utilisation

### Prérequis
```bash
pip install -r requirements.txt
```
+ **FFmpeg** installé sur le système (requis par moviepy) : https://ffmpeg.org/download.html

### Exemples
```bash
python main.py ma_video.mp4
python main.py ma_video.mp4 -o sous_titres.txt -l en
```

### Options
| Option | Description | Défaut |
|---|---|---|
| `video` | Chemin de la vidéo | (demandé) |
| `-o`, `--sortie` | Fichier de sortie | `sous_titres.txt` |
| `-l`, `--langue` | Langue parlée dans la vidéo | `en` |

## 🔧 Améliorations apportées

- Fusion de `main.py` et `main2.py` en **une seule version**
- Chemin de vidéo en **argument** (plus de chemin codé en dur)
- **Gestion d'erreurs** : vidéo sans audio, parole non reconnue, service indisponible, dépendances manquantes
- Nettoyage automatique du fichier audio temporaire

## ⚠️ Limite

La reconnaissance Google renvoie un **bloc de texte** sans horodatage : la sortie est une transcription traduite, pas un vrai `.srt` minuté.
