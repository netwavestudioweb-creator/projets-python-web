#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DODDS APPLICATION — connexion (Tkinter) + page d'accueil
========================================================
Petite application de bureau : l'utilisateur se connecte, puis une page web
de bienvenue personnalisée s'ouvre dans le navigateur.

🔒 Les mots de passe ne sont PAS stockés en clair : on compare leur
   empreinte SHA-256 (voir aussi le projet SecurePassGen pour aller plus loin).
"""
import hashlib
import os
import webbrowser
from tkinter import Tk, Label, Entry, Button, messagebox, X

# Utilisateurs : nom -> empreinte SHA-256 du mot de passe (jamais en clair).
UTILISATEURS = {
    "DODO":    "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",  # 1234
    "MARIANO": "38083c7ee9121e17401883566a148aa5c2e2d55dc53bc4a94a026517dbff3c6b",  # 2345
    "ADRIANO": "f8638b979b2f4f793ddb6dbd197e0ee25a7a6ea32b0ae22f5e3c5d119d839e75",  # 5678
}

DOSSIER = os.path.dirname(os.path.abspath(__file__))


def hacher(mot_de_passe: str) -> str:
    return hashlib.sha256(mot_de_passe.encode("utf-8")).hexdigest()


def generer_page(nom: str) -> str:
    """Crée une page d'accueil personnalisée et renvoie son chemin."""
    chemin = os.path.join(DOSSIER, "index.html")
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>DODDS APPLICATION</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f0f4f8;
                display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }}
        .carte {{ background: #fff; padding: 40px 48px; border-radius: 16px;
                  box-shadow: 0 8px 28px rgba(0,0,0,.1); text-align: center; }}
        h1 {{ color: #2e7d32; margin: 0 0 8px; }}
        p {{ color: #555; }}
    </style>
</head>
<body>
    <div class="carte">
        <h1>Bienvenue, {nom} !</h1>
        <p>Vous êtes connecté à DODDS APPLICATION.</p>
    </div>
</body>
</html>
"""
    with open(chemin, "w", encoding="utf-8") as page:
        page.write(html)
    return chemin


def valider():
    nom = E1.get().strip().upper()
    mot_de_passe = E2.get()
    if nom in UTILISATEURS and UTILISATEURS[nom] == hacher(mot_de_passe):
        chemin = generer_page(nom.title())
        webbrowser.open("file://" + chemin)
    else:
        messagebox.showerror(
            "Échec de connexion",
            "Nom d'utilisateur ou mot de passe incorrect.")


# --- Interface ---
APL = Tk()
APL.title("DODDS APP")
APL.geometry("420x320")
APL.configure(bg="#f0f4f8")

Label(APL, text="BIENVENUE", bg="#2e7d32", fg="white",
      font=("tajawal", 18, "bold")).pack(fill=X)
Label(APL, text="Connexion", bg="#f0f4f8", fg="#333",
      font=("tajawal", 13)).pack(pady=(18, 10))

Label(APL, text="Identifiant", bg="#f0f4f8").pack()
E1 = Entry(APL, justify="center", width=28)
E1.pack(pady=(0, 12))

Label(APL, text="Mot de passe", bg="#f0f4f8").pack()
E2 = Entry(APL, justify="center", show="*", width=28)
E2.pack(pady=(0, 18))

Button(APL, text="Valider", bg="#2e7d32", fg="white", width=22,
       command=valider).pack()

# Valider avec la touche Entrée
APL.bind("<Return>", lambda event: valider())

APL.mainloop()
