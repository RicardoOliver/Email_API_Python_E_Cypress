from flask import Flask
from flask_mail import Mail
from app.config import DevelopmentConfig  # Altere conforme necessário
import os

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)  # Altere conforme necessário

mail = Mail(app)

from app.routes import auth, email
app.register_blueprint(auth.bp)
app.register_blueprint(email.bp)
