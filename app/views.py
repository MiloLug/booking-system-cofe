from app import app
from flask_login import login_required, login_user,current_user, logout_user
from flask import request, redirect, render_template, url_for,flash,make_response,session
from forms import LoginForm
from utils import send_mail



#Сессия
@app.before_first_request
def before_first_request():
    session["users"]="visitor"
manager = Manager(app)











@manager.command
def fake():
    print("Fake data created!")

def shell_context():
    import os, sys
    return dict(app=app, os=os, sys=sys)

manager.add_command("shell", Shell(make_context=shell_context))



@app.route('/')
def index():
    today = datetime.datetime.today()
    return redirect("http://127.0.0.1:5000/" + today.strftime("%m-%d-%Y"))



@app.route('/<date>')
def handler_date(date):
    return render_template('index.html', current_date=date)



@app.route('/login', methods=['post','get'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = LoginForm()
    message = ''
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user != None and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('admin'))
        flash("Invalid username/password", 'error')
        return redirect(url_for('login'))
    return render_template('login.html', message=message, form=form)



@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('login'))



@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')



if __name__ == "__main__":
    manager.run()