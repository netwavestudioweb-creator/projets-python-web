#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de QR code — version ligne de commande (hors-ligne)
==============================================================

Génère un QR code PNG sans avoir à lancer de serveur web.

Exemples :
    python qr_cli.py "https://exemple.com"
    python qr_cli.py "Mon texte" -o mon_qr.png -s 12
    python qr_cli.py            (mode interactif)
"""
import argparse
import sys

import qrcode

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def generer(donnees: str, sortie: str, taille: int = 10, bordure: int = 4) -> str:
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=taille,
        border=bordure,
    )
    qr.add_data(donnees)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(sortie)
    return sortie


def main() -> None:
    parser = argparse.ArgumentParser(description="Générateur de QR code (CLI).")
    parser.add_argument("donnees", nargs="?", help="Texte ou URL à encoder")
    parser.add_argument("-o", "--sortie", default="qrcode.png",
                        help="Fichier PNG de sortie (défaut : qrcode.png)")
    parser.add_argument("-s", "--taille", type=int, default=10,
                        help="Taille des modules (défaut : 10)")
    args = parser.parse_args()

    donnees = args.donnees or input("Données à encoder : ").strip()
    if not donnees:
        raise SystemExit("❌ Aucune donnée fournie.")

    chemin = generer(donnees, args.sortie, args.taille)
    print(f"✅ QR code généré : {chemin}")


if __name__ == "__main__":
    main()
