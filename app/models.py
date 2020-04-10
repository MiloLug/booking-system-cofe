from app import db, login_manager
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



@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()