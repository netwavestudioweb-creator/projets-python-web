#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bot Telegram — exemple d'écho
=============================
Répond à /start et /help, puis fait l'écho des messages reçus.

🔐 Le token du bot est lu depuis la variable d'environnement TELEGRAM_BOT_TOKEN
    (jamais codé en dur). Obtenez un token auprès de @BotFather sur Telegram.
"""
import os
import sys

import telebot

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    sys.exit("❌ Variable d'environnement TELEGRAM_BOT_TOKEN manquante. "
             "Obtenez un token via @BotFather, puis définissez-la (voir README).")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(
        message,
        "👋 Salut ! Je suis un bot d'exemple.\n"
        "Envoie-moi un message et je te le renverrai.",
    )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Tu as dit : {message.text}")


if __name__ == "__main__":
    print("🤖 Bot démarré. Ctrl+C pour arrêter.")
    bot.infinity_polling()
