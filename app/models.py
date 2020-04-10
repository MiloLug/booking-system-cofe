from app import db, login_manager
from datetime import datetime
from flask_login import LoginManager,UserMixin,login_required, login_user, current_user,logout_user
from mongoengine.fields import DateTimeField



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

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


