from peewee import   *
from os import  path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection,"MyCollege.db"))

class Users(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    class Meta:
        database = db
Users.create_table(fail_silently=True)
try:
   Users.create(name = "Temwa",email = "Temwa2@gmail.com",password = "temwa123")
   print("user saved successfully")
except IntegrityError:
   print("Saved user failed email already exist")

users = Users.select()
for user in  users:
    print(user.email)


class Products(Model):
      name = CharField()
      qtty = CharField()
      price =CharField()
      discount = CharField()
      class Meta:
          database = db
Products.create_table(fail_silently=True)
Products.create(name = "Sugar",qtty = "1kg",price ="Ksh100",discount = "Ksh10.00")
products = Products.select()
for product in products:
    print(product.name)