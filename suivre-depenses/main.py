#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestion des dépenses et épargne
===============================
Petite application de bureau (Tkinter) pour estimer un budget quotidien,
l'épargne possible, et visualiser la répartition des dépenses.
"""
import os
import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt

# Pillow est optionnel : l'app fonctionne même sans icône.
try:
    from PIL import Image, ImageTk
    PIL_DISPO = True
except ImportError:
    PIL_DISPO = False


def _charger_icone(root):
    """Charge icon.png si présent, en gérant les versions récentes de Pillow."""
    chemin = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.png")
    if not (PIL_DISPO and os.path.exists(chemin)):
        return None
    try:
        image = Image.open(chemin)
        # Image.ANTIALIAS a été supprimé dans Pillow 10 → on utilise Resampling.
        filtre = getattr(getattr(Image, "Resampling", Image), "LANCZOS", None)
        image = image.resize((50, 50), filtre) if filtre else image.resize((50, 50))
        return ImageTk.PhotoImage(image)
    except Exception:
        return None


class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Dépenses et Épargne")

        self.income = tk.DoubleVar()
        self.days = tk.IntVar()
        self.savings_goal = tk.DoubleVar()
        self.food_expense = tk.DoubleVar()
        self.transport_expense = tk.DoubleVar()
        self.other_expense = tk.DoubleVar()

        self.create_widgets()

    def create_widgets(self):
        icone = _charger_icone(self.root)
        if icone is not None:
            tk.Label(self.root, image=icone).grid(row=0, column=0, columnspan=2)
            self.root.icon_image = icone  # garde une référence

        champs = [
            ("Revenu Hebdomadaire :", self.income),
            ("Nombre de jours que l'argent dure :", self.days),
            ("Objectif d'Épargne :", self.savings_goal),
            ("Dépense Bouffe :", self.food_expense),
            ("Dépense Transport :", self.transport_expense),
            ("Autres Dépenses :", self.other_expense),
        ]
        for i, (libelle, variable) in enumerate(champs, start=1):
            tk.Label(self.root, text=libelle).grid(row=i, column=0, sticky="w")
            tk.Entry(self.root, textvariable=variable).grid(row=i, column=1)

        tk.Button(self.root, text="Calculer", command=self.calculate_budget)\
            .grid(row=7, column=0, columnspan=2, sticky="ew")
        tk.Button(self.root, text="Afficher Graphique", command=self.show_chart)\
            .grid(row=8, column=0, columnspan=2, sticky="ew")

    def _lire_valeurs(self):
        """Lit les champs ; lève ValueError si une saisie est invalide."""
        try:
            income = self.income.get()
            days = self.days.get()
            savings_goal = self.savings_goal.get()
            food = self.food_expense.get()
            transport = self.transport_expense.get()
            other = self.other_expense.get()
        except tk.TclError:
            raise ValueError("Veuillez entrer des nombres valides dans tous les champs.")

        if income <= 0 or days <= 0:
            raise ValueError("Le revenu et le nombre de jours doivent être positifs.")
        if min(savings_goal, food, transport, other) < 0:
            raise ValueError("Les montants ne peuvent pas être négatifs.")
        return income, days, savings_goal, food, transport, other

    def calculate_budget(self):
        try:
            income, days, savings_goal, food, transport, other = self._lire_valeurs()
            total_expense = food + transport + other
            daily_budget = income / days
            remaining_amount = income - total_expense
            short_term_savings = remaining_amount - savings_goal

            message = (
                f"Budget quotidien : {daily_budget:.2f}\n"
                f"Dépense totale : {total_expense:.2f}\n"
                f"Montant restant : {remaining_amount:.2f}\n"
                f"Épargne à court terme : {short_term_savings:.2f}"
            )
            messagebox.showinfo("Résultats", message)
        except ValueError as err:
            messagebox.showerror("Erreur", str(err))

    def show_chart(self):
        try:
            depenses = [self.food_expense.get(), self.transport_expense.get(),
                        self.other_expense.get()]
        except tk.TclError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")
            return

        if sum(depenses) <= 0:
            messagebox.showwarning("Graphique",
                                   "Entrez au moins une dépense pour afficher le graphique.")
            return

        labels = ["Bouffe", "Transport", "Autres"]
        plt.figure(figsize=(8, 6))
        plt.pie(depenses, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title("Répartition des Dépenses")
        plt.axis("equal")
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    BudgetApp(root)
    root.mainloop()
