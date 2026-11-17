#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Traducteur de vidéo → sous-titres français
==========================================

Pipeline : vidéo → extraction audio → reconnaissance vocale → traduction FR
→ fichier de sous-titres / transcription.

Dépendances (voir requirements.txt) :
    moviepy, SpeechRecognition, pydub, googletrans
    + l'outil système **ffmpeg** (requis par moviepy/pydub).

Exemples :
    python main.py ma_video.mp4
    python main.py ma_video.mp4 -o sous_titres.txt -l en
"""
from __future__ import annotations

import argparse
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def _importer_dependances():
    """Importe les dépendances lourdes en donnant un message clair si absentes."""
    manquants = []
    try:
        import moviepy.editor as mp  # noqa: F401
    except ImportError:
        manquants.append("moviepy")
    try:
        import speech_recognition as sr  # noqa: F401
    except ImportError:
        manquants.append("SpeechRecognition")
    try:
        from googletrans import Translator  # noqa: F401
    except ImportError:
        manquants.append("googletrans")
    if manquants:
        raise SystemExit(
            "❌ Dépendances manquantes : " + ", ".join(manquants) +
            "\n   Installez-les avec : pip install -r requirements.txt"
        )


def extraire_audio(video_path: str, audio_path: str = "audio.wav") -> str:
    import moviepy.editor as mp
    video = mp.VideoFileClip(video_path)
    if video.audio is None:
        raise ValueError("La vidéo ne contient pas de piste audio.")
    video.audio.write_audiofile(audio_path, logger=None)
    video.close()
    return audio_path


def audio_vers_texte(audio_path: str, langue_source: str) -> str:
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language=langue_source)
    except sr.UnknownValueError:
        raise ValueError("Impossible de comprendre l'audio (parole non reconnue).")
    except sr.RequestError as err:
        raise ValueError(f"Service de reconnaissance indisponible : {err}")


def traduire_en_francais(texte: str) -> str:
    from googletrans import Translator
    translator = Translator()
    return translator.translate(texte, dest="fr").text


def sauvegarder(texte: str, sortie: str) -> None:
    with open(sortie, "w", encoding="utf-8") as f:
        f.write(texte)


def traiter(video_path: str, sortie: str, langue_source: str) -> None:
    if not os.path.exists(video_path):
        raise SystemExit(f"❌ Vidéo introuvable : {video_path}")

    print("🎬 Extraction de l'audio…")
    audio_path = extraire_audio(video_path)

    print("🗣️  Reconnaissance vocale…")
    texte = audio_vers_texte(audio_path, langue_source)

    print("🌍 Traduction en français…")
    traduit = traduire_en_francais(texte)

    sauvegarder(traduit, sortie)
    print(f"✅ Transcription traduite enregistrée : {sortie}")

    # Nettoyage du fichier audio temporaire
    try:
        os.remove(audio_path)
    except OSError:
        pass


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Traduit la parole d'une vidéo en français.")
    parser.add_argument("video", nargs="?", help="Chemin de la vidéo à traiter")
    parser.add_argument("-o", "--sortie", default="sous_titres.txt",
                        help="Fichier de sortie (défaut : sous_titres.txt)")
    parser.add_argument("-l", "--langue", default="en",
                        help="Langue parlée dans la vidéo (défaut : en)")
    args = parser.parse_args()

    video = args.video or input("Chemin de la vidéo : ").strip()
    if not video:
        raise SystemExit("❌ Aucune vidéo fournie.")

    _importer_dependances()
    try:
        traiter(video, args.sortie, args.langue)
    except ValueError as err:
        raise SystemExit(f"❌ {err}")


if __name__ == "__main__":
    main()
