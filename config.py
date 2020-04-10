import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    MONGODB_SETTINGS = {"db": "test"}

    ##### настройка Flask-Mail #####
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'YOU_MAIL@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME



class DevelopementConfig(BaseConfig):
    DEBUG = True
    DATABASE_URI = os.environ.get('http://localhost:27017/test')


class TestingConfig(BaseConfig):
    DEBUG = True
    DATABASE_URI = os.environ.get('TESTING_DATABASE_URI')

class ProductionConfig(BaseConfig):
    DEBUG = False
    DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI')