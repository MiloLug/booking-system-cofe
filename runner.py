import os
from app import app, db
from app.models import User, Order, Customer, Table
from flask_script import Manager, Shell
from mongoengine import *
import datetime
import random


manager = Manager(app)

# эти переменные доступны внутри оболочки без явного импорта
def make_shell_context():
    return dict(app=app, db=db, User=User, Order=Order, Customer=Customer)

manager.add_command('shell', Shell(make_context=make_shell_context))

@manager.command
def make_demo():
    #create def admin
    user_admin = User(username="root", password="pass",role="admin");
    #create fake tables
    for item in range(random.randint(2, 5)):
        table = Table(number=item,place_count=random.randint(2, 4),figure=random.choice(["square","circle"]),coordinates={'left':200,'top':200}, size={'w':10,'h':20}).save()
    #create fake customer
    for _ in range(random.randint(6, 17)):
        table = Customer(name="Alex",email="demo@example.com",visits=random.randint(1, 10), phone="1111demophone1111").save()
    #create fake orders
    for item in range(random.randint(3, 16)):
        customer_for_order_fake = Customer.objects.all()
        table_for_order_fake = Table.objects.all()
        ttday = datetime.datetime.today()
        table = Order(customer=customer_for_order_fake[random.randint(0, Customer.objects.count())],table_id=table_for_order_fake[random.randint(0,  Table.objects.count())],date=ttday.strftime("%m-%d-%Y"),people_number=random.randint(1, 4)).save()
    print("foo command executed")





if __name__ == '__main__':
    manager.run()