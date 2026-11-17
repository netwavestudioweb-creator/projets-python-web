#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Répertoire téléphonique
=======================
Gestionnaire de contacts en console, avec stockage JSON.

Fonctions : ajouter, rechercher, lister, supprimer un contact.
Les données sont enregistrées dans `contacts.json` (à côté de ce script).
"""
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FICHIER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.json")


def charger() -> dict:
    """Charge les contacts depuis le fichier JSON (dict nom -> téléphone)."""
    if not os.path.exists(FICHIER):
        return {}
    try:
        with open(FICHIER, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("⚠️  Fichier de contacts illisible — on repart d'un répertoire vide.")
        return {}


def sauvegarder(contacts: dict) -> None:
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def ajouter(contacts: dict) -> None:
    nom = input("Nom : ").strip()
    if not nom:
        print("❌ Le nom ne peut pas être vide.")
        return
    telephone = input("Téléphone : ").strip()
    if not telephone:
        print("❌ Le téléphone ne peut pas être vide.")
        return
    if nom in contacts:
        rep = input(f"⚠️  « {nom} » existe déjà ({contacts[nom]}). Remplacer ? (o/n) : ").lower()
        if rep not in ("o", "oui"):
            print("Annulé.")
            return
    contacts[nom] = telephone
    sauvegarder(contacts)
    print(f"✅ Contact enregistré : {nom} — {telephone}")


def rechercher(contacts: dict) -> None:
    terme = input("Rechercher (nom ou partie du nom) : ").strip().lower()
    if not terme:
        return
    resultats = {n: t for n, t in contacts.items() if terme in n.lower()}
    if resultats:
        print(f"\n🔎 {len(resultats)} résultat(s) :")
        for nom, tel in sorted(resultats.items()):
            print(f"   {nom} : {tel}")
    else:
        print("Aucun contact trouvé.")


def lister(contacts: dict) -> None:
    if not contacts:
        print("📭 Répertoire vide.")
        return
    print(f"\n📒 {len(contacts)} contact(s) :")
    for nom, tel in sorted(contacts.items()):
        print(f"   {nom} : {tel}")


def supprimer(contacts: dict) -> None:
    nom = input("Nom du contact à supprimer : ").strip()
    if nom in contacts:
        del contacts[nom]
        sauvegarder(contacts)
        print(f"🗑️  Contact « {nom} » supprimé.")
    else:
        print("❌ Contact introuvable.")


def menu() -> None:
    contacts = charger()
    actions = {
        "1": ("Ajouter un contact", ajouter),
        "2": ("Rechercher un contact", rechercher),
        "3": ("Lister tous les contacts", lister),
        "4": ("Supprimer un contact", supprimer),
    }
    while True:
        print("\n=== 📞 Répertoire téléphonique ===")
        for cle, (libelle, _) in actions.items():
            print(f"{cle} : {libelle}")
        print("0 : Quitter")

        choix = input("Votre choix : ").strip()
        if choix == "0":
            print("👋 À bientôt !")
            break
        action = actions.get(choix)
        if action:
            action[1](contacts)
        else:
            print("❌ Choix invalide.")


if __name__ == "__main__":
    menu()
