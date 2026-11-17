# ⏰ RAPPEL-TOI

Application de bureau (Tkinter) pour **planifier un appel téléphonique** de rappel à une date/heure future, avec enregistrement d'un message audio. L'appel est passé via **Twilio**.

> Version 1.3 — refondue (sécurité + planification corrigée). Remplace les versions 1.1 (`sys.py`) et 1.2 (`sys1.py`).

---

## 🔐 Sécurité — à lire en premier

⚠️ **Les anciennes versions contenaient des identifiants Twilio écrits en clair dans le code.** Si vous aviez committé/partagé ce fichier, **révoquez et régénérez immédiatement votre Auth Token** dans la console Twilio (Account → API credentials). Un token exposé doit être considéré comme compromis.

Désormais, les identifiants sont lus depuis des **variables d'environnement**, jamais stockés dans le code.

---

## ⚙️ Configuration

Définir les variables d'environnement avant de lancer l'app :

**Windows (PowerShell)**
```powershell
$env:TWILIO_ACCOUNT_SID = "votre_sid"
$env:TWILIO_AUTH_TOKEN  = "votre_token"
$env:TWILIO_PHONE_NUMBER = "+1234567890"
```

**Linux / macOS**
```bash
export TWILIO_ACCOUNT_SID="votre_sid"
export TWILIO_AUTH_TOKEN="votre_token"
export TWILIO_PHONE_NUMBER="+1234567890"
```

---

## 🚀 Utilisation

```bash
pip install -r requirements.txt
python sysam.py
```

---

## 🔧 Corrections apportées

- 🔐 **Identifiants Twilio retirés du code** → variables d'environnement
- 🐛 **Planification corrigée** : `schedule.enter/run` (inexistants dans la lib `schedule`) remplacés par `threading.Timer`
- 🎙️ Enregistrement micro rendu **optionnel** (l'app s'ouvre même sans PyAudio / sans micro)
- Validation des champs et journalisation conservées
