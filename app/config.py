import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuração base para o aplicativo Flask."""
    SECRET_KEY = os.getenv('SECRET_KEY')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

class DevelopmentConfig(Config):
    """Configuração para o ambiente de desenvolvimento."""
    DEBUG = True

class TestingConfig(Config):
    """Configuração para o ambiente de teste."""
    TESTING = True
    MAIL_SUPPRESS_SEND = True

class ProductionConfig(Config):
    """Configuração para o ambiente de produção."""
    DEBUG = False
