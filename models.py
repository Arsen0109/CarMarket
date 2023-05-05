from peewee import *

db = MySQLDatabase('carmarket', user='root', password='@rsen2003', host='localhost', port=3306)


class Car(Model):
    car_id = IntegerField(primary_key=True)
    make = CharField()
    model = CharField()
    price = IntegerField()
    year = IntegerField()
    image = CharField()

    class Meta:
        database = db
        table_name = 'cars'
