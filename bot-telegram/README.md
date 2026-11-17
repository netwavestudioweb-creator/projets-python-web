# 🤖 Bot Telegram (écho)

Bot Telegram d'exemple : répond à `/start` et `/help`, et renvoie en écho les messages reçus.

## 🔐 Sécurité — à lire en premier

⚠️ L'ancienne version contenait le **token du bot en clair**. **Régénérez-le** via @BotFather (`/revoke`) s'il a été partagé. Le token est désormais lu depuis une variable d'environnement.

## ⚙️ Configuration

```powershell
# Windows (PowerShell)
$env:TELEGRAM_BOT_TOKEN = "votre_token_botfather"
```
```bash
# Linux / macOS
export TELEGRAM_BOT_TOKEN="votre_token_botfather"
```

## 🚀 Utilisation

```bash
pip install -r requirements.txt
python scripts.py
```

## 🔧 Améliorations apportées

- 🔐 Token retiré du code → variable d'environnement
- Messages d'accueil plus clairs, écho du texte réellement reçu
- Arrêt propre documenté (Ctrl+C)
