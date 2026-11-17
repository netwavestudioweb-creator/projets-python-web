#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de mot de passe
==========================
Génère un mot de passe aléatoire **sécurisé** (module `secrets`), avec une
longueur minimale et des options chiffres / caractères spéciaux.

Note : une version plus complète (entropie, interface web) existe dans le
projet `SecurePassGen` de la Suite Cybersécurité.
"""
import secrets
import string
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def generer_mot_de_passe(longueur_min: int, chiffres: bool = True,
                         caracteres_speciaux: bool = True) -> str:
    """Génère un mot de passe respectant les critères, via `secrets`."""
    classes = [string.ascii_letters]
    if chiffres:
        classes.append(string.digits)
    if caracteres_speciaux:
        classes.append(string.punctuation)

    longueur = max(longueur_min, len(classes))
    # Au moins un caractère de chaque classe demandée, puis complément aléatoire.
    mdp = [secrets.choice(classe) for classe in classes]
    tous = "".join(classes)
    mdp += [secrets.choice(tous) for _ in range(longueur - len(mdp))]
    secrets.SystemRandom().shuffle(mdp)
    return "".join(mdp)


def demander_entier(question: str, minimum: int = 1) -> int:
    while True:
        brut = input(question).strip()
        try:
            valeur = int(brut)
            if valeur < minimum:
                print(f"⚠️  Entrez un nombre ≥ {minimum}.")
                continue
            return valeur
        except ValueError:
            print("⚠️  Veuillez entrer un nombre valide.")


def main() -> None:
    longueur_min = demander_entier("Longueur minimale : ", minimum=1)
    chiffres = input("Inclure des chiffres ? (O/N) : ").strip().lower() == "o"
    speciaux = input("Inclure des caractères spéciaux ? (O/N) : ").strip().lower() == "o"

    mdp = generer_mot_de_passe(longueur_min, chiffres, speciaux)
    print("\n🔐 Mot de passe généré :", mdp)


if __name__ == "__main__":
    main()
