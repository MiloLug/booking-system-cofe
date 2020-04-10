from flask import Flask
from flask_script import Manager, Command, Shell
from werkzeug.security import generate_password_hash,  check_password_hash
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface,BaseQuerySet
from flask_mongoengine.wtf import model_form

import datetime

#app
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')

#exp
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# import views
from . import views