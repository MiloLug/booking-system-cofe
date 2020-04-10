from app import db, login_manager
from datetime import datetime
from flask_login import LoginManager,UserMixin,login_required, login_user, current_user,logout_user
from mongoengine.fields import DateTimeField, DictField



class User(db.Document,UserMixin):
    username = db.StringField()
    password = db.StringField()
    role = db.StringField()

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)

class Order(db.Document):
    number = db.IntField()
    customer = db.IntField()
    table_id = db.IntField()
    date = DateTimeField()
    people_number = db.IntField()

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.number )

class Customer(db.Document):
    name = db.StringField()
    email = db.EmailField()
    visits =  db.IntField()
    phone = db.StringField()

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)

class Table(db.Document):
    number = db.IntField()
    place_count = db.IntField()
    figure =  db.StringField()
    coordinates = db.DictField()
    size = db.DictField()

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.number)

@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()


