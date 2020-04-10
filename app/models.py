from app import db, login_manager
from datetime import datetime
from flask_login import (LoginManager, UserMixin, login_required,login_user, current_user, logout_user)
from flask_login import LoginManager,UserMixin,login_required, login_user, current_user,logout_user
import mongoengine as me



class User(me.Document,UserMixin):
    username = db.StringField()
    password = db.StringField()
    role = db.StringField()

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)

    def set_password(self, password):
    	self.password_hash = generate_password_hash(password)

    def check_password(self,  password):
        return check_password_hash(self.password_hash, password)  


class Order(me.Document):
    number = db.IntField()
    customer = Customer()
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