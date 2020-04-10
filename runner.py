import os
from app import app, db
from app.models import User, Order, Customer
from flask_script import Manager, Shell
from elizabeth import Personal

manager = Manager(app)

# эти переменные доступны внутри оболочки без явного импорта
def make_shell_context():
    return dict(app=app, db=db, User=User, Order=Order, Customer=Customer)

manager.add_command('shell', Shell(make_context=make_shell_context))

@manager.command
def make_demo():
    person = Personal('is')
    for _ in range(0, 3):
        fake_user = Customer(name='ross@example.com', first_name='Ross', last_name='Lawley').save()
    print("foo command executed")






if __name__ == '__main__':
    manager.run()