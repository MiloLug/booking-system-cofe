from app import db, login_manager
from datetime import datetime
from flask_login import LoginManager,UserMixin,login_required, login_user, current_user,logout_user
from mongoengine.fields import DateTimeField, DictField,ReferenceField



class User(db.Document,UserMixin):
    username = db.StringField(required=True,max_length=10)
    password = db.StringField(required=True,max_length=10)
    role = db.StringField()

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)




class Customer(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True)
    visits =  db.IntField()
    phone = db.StringField()

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)

class Table(db.Document):
    number = db.IntField(required=True)
    place_count = db.IntField(required=True)
    figure =  db.StringField(required=True)
    coordinates = db.DictField(required=True)
    size = db.DictField(required=True)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.number)



class Order(db.Document):
    customer = ReferenceField(Customer, required=True)
    table_id = ReferenceField(Table, required=True)
    date = DateTimeField(required=True)
    people_number = db.IntField()

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.number )


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()


