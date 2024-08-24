from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

# Chave secreta para geração de tokens JWT
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

mail = Mail(app)

from app.routes import auth, email
app.register_blueprint(auth.bp)
app.register_blueprint(email.bp)
