#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RAPPEL-TOI — rappel téléphonique programmé
==========================================
Interface Tkinter : saisir un destinataire, enregistrer un message audio, et
planifier un appel (via Twilio) à une date/heure future.

🔐 SÉCURITÉ — Identifiants Twilio
    Les identifiants NE sont PLUS codés en dur dans ce fichier. Ils sont lus
    depuis les variables d'environnement :
        TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
    Définissez-les avant de lancer l'application (voir README).
"""
import logging
import os
import threading
import tkinter as tk
import wave
from datetime import datetime
from tkinter import messagebox

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# --- Identifiants Twilio : lus depuis l'environnement (jamais codés en dur) ---
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")

# PyAudio est optionnel : l'app s'ouvre même sans micro configuré.
try:
    import pyaudio
    PYAUDIO_DISPO = True
except ImportError:
    PYAUDIO_DISPO = False


class RappelToiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rappel Toi")

        self.nom = tk.StringVar()
        self.prenom = tk.StringVar()
        self.age = tk.StringVar()
        self.numero = tk.StringVar()
        self.date_envoi = tk.StringVar()
        self.heure_envoi = tk.StringVar()

        self.main_frame = tk.Frame(root, padx=20, pady=20, bg="#f0f0f0")
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        label_font = ("Helvetica", 12)
        entry_font = ("Helvetica", 12)
        button_font = ("Helvetica", 12, "bold")

        champs = [
            ("Nom :", self.nom),
            ("Prénom :", self.prenom),
            ("Âge :", self.age),
            ("Numéro du destinataire :", self.numero),
            ("Date d'envoi (YYYY-MM-DD) :", self.date_envoi),
            ("Heure d'envoi (HH:MM) :", self.heure_envoi),
        ]
        for i, (libelle, variable) in enumerate(champs):
            tk.Label(self.main_frame, text=libelle, font=label_font, bg="#f0f0f0")\
                .grid(row=i, column=0, sticky="w", pady=5)
            tk.Entry(self.main_frame, textvariable=variable, font=entry_font)\
                .grid(row=i, column=1, pady=5)

        self.recording = False
        tk.Button(self.main_frame, text="Démarrer l'enregistrement",
                  command=self.start_recording, font=button_font,
                  bg="#4caf50", fg="white").grid(row=6, column=0, pady=10, ipadx=10)
        tk.Button(self.main_frame, text="Arrêter l'enregistrement",
                  command=self.stop_recording, font=button_font,
                  bg="#f44336", fg="white").grid(row=6, column=1, pady=10, ipadx=10)
        tk.Button(self.main_frame, text="Valider la demande",
                  command=self.valider_demande, font=button_font,
                  bg="#2196f3", fg="white").grid(row=7, columnspan=2, pady=20, ipadx=10)

        self.audio_filename = ""
        self.frames = []
        self.p = None
        self.stream = None

        if PYAUDIO_DISPO:
            try:
                self.p = pyaudio.PyAudio()
                self.stream = self.p.open(format=pyaudio.paInt16, channels=1,
                                          rate=44100, input=True,
                                          frames_per_buffer=1024)
            except Exception as e:
                logging.error("Initialisation audio impossible : %s", e)
                messagebox.showwarning(
                    "Audio", f"Micro indisponible, l'enregistrement sera désactivé.\n({e})")
        else:
            logging.warning("PyAudio non installé — enregistrement désactivé.")

    # ------------------------- Enregistrement audio -------------------------
    def start_recording(self):
        if not self.p or not self.stream:
            messagebox.showerror("Erreur", "L'audio n'est pas disponible.")
            return
        self.recording = True
        self.frames = []
        self.audio_filename = f"message_{datetime.now():%Y%m%d_%H%M%S}.wav"
        threading.Thread(target=self.record, daemon=True).start()
        messagebox.showinfo("Information", "Enregistrement commencé")

    def record(self):
        while self.recording:
            try:
                self.frames.append(self.stream.read(1024))
            except Exception as e:
                logging.error("Erreur d'enregistrement : %s", e)
                self.recording = False

    def stop_recording(self):
        if not self.recording:
            messagebox.showerror("Erreur", "Aucun enregistrement en cours.")
            return
        self.recording = False
        try:
            with wave.open(self.audio_filename, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
                wf.setframerate(44100)
                wf.writeframes(b"".join(self.frames))
            messagebox.showinfo("Information", f"Enregistrement sauvegardé : {self.audio_filename}")
        except Exception as e:
            logging.error("Sauvegarde audio impossible : %s", e)
            messagebox.showerror("Erreur", f"Sauvegarde impossible : {e}")

    # ----------------------------- Validation -----------------------------
    def valider_demande(self):
        if not all([self.nom.get(), self.prenom.get(), self.age.get(),
                    self.numero.get(), self.date_envoi.get(), self.heure_envoi.get()]):
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        try:
            if int(self.age.get()) <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erreur", "L'âge doit être un nombre positif.")
            return

        try:
            date_envoi = datetime.strptime(
                f"{self.date_envoi.get()} {self.heure_envoi.get()}", "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror(
                "Erreur", "Format invalide. Date : YYYY-MM-DD, Heure : HH:MM.")
            return

        if date_envoi <= datetime.now():
            messagebox.showerror("Erreur", "La date d'envoi doit être dans le futur.")
            return

        self.planifier_appel(date_envoi)
        messagebox.showinfo("Succès", f"Appel planifié pour {date_envoi:%Y-%m-%d %H:%M}.")

    # ----------------------------- Planification --------------------------
    def planifier_appel(self, date_envoi: datetime):
        if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER]):
            messagebox.showerror(
                "Configuration manquante",
                "Identifiants Twilio absents.\nDéfinissez les variables d'environnement "
                "TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN et TWILIO_PHONE_NUMBER.")
            return

        delai_secondes = (date_envoi - datetime.now()).total_seconds()
        if delai_secondes <= 0:
            return

        # threading.Timer : planification correcte (l'ancien code utilisait
        # schedule.enter/run qui n'existent pas dans la librairie `schedule`).
        timer = threading.Timer(delai_secondes, self._passer_appel)
        timer.daemon = True
        timer.start()
        logging.info("Appel planifié pour %s (dans %.0f s)", date_envoi, delai_secondes)

    def _passer_appel(self):
        try:
            from twilio.rest import Client
            from twilio.base.exceptions import TwilioRestException
        except ImportError:
            logging.error("Le paquet `twilio` n'est pas installé.")
            return
        try:
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            appel = client.calls.create(
                to=self.numero.get(),
                from_=TWILIO_PHONE_NUMBER,
                url="http://demo.twilio.com/docs/voice.xml",
            )
            logging.info("Appel passé : %s", appel.sid)
        except TwilioRestException as e:
            logging.error("Échec de l'appel Twilio : %s", e)


if __name__ == "__main__":
    root = tk.Tk()
    RappelToiApp(root)
    root.mainloop()
