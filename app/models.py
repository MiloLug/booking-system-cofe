from app import db, login_manager
from datetime import datetime
from flask_login import (LoginManager, UserMixin, login_required,login_user, current_user, logout_user)
from flask_login import LoginManager,UserMixin,login_required, login_user, current_user,logout_user
import mongoengine as me
from mongoengine.fields import DateTimeField



class User(me.Document,UserMixin):
    username = db.StringField()
    password = db.StringField()
    role = db.StringField()

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)



class Order(me.Document):
    number = db.IntField()
    customer = db.IntField()
    table_id = db.IntField()
    date = DateTimeField()
    people_number = db.IntField()

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)







class Customer():
    name = db.StringField()
    email = db.EmailField()
    visits =  db.IntField()
    phone = db.StringField()

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)