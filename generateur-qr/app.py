from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    # Récupérer les données du formulaire
    name = request.form.get('name', '')
    phone = request.form.get('phone', '')
    email = request.form.get('email', '')
    facebook = request.form.get('facebook', '')
    linkedin = request.form.get('linkedin', '')
    instagram = request.form.get('instagram', '')
    twitter = request.form.get('twitter', '')
    website = request.form.get('website', '')
    message = request.form.get('message', '')

    # Construire les données pour le QR Code
    qr_data = f"Name: {name}\nPhone: {phone}\nEmail: {email}\n"
    if facebook:
        qr_data += f"Facebook: {facebook}\n"
    if linkedin:
        qr_data += f"LinkedIn: {linkedin}\n"
    if instagram:
        qr_data += f"Instagram: {instagram}\n"
    if twitter:
        qr_data += f"Twitter: {twitter}\n"
    if website:
        qr_data += f"Website: {website}\n"
    if message:
        qr_data += f"Message: {message}\n"

    # Vérifier que certaines informations sont présentes
    if not any([name, phone, email, facebook, linkedin, instagram, twitter, website, message]):
        return "Please provide at least one piece of information to generate a QR code."

    # Générer le QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Sauvegarder l'image dans un objet BytesIO pour l'envoyer sans écrire sur le disque
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    # Envoyer le QR Code généré en tant qu'image à l'utilisateur
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

if __name__ == '__main__':
    # Local uniquement + debug désactivé : valeurs sûres par défaut.
    app.run(host='127.0.0.1', port=5000, debug=False)
