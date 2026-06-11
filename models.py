from peewee import SqliteDatabase, Model, IntegerField, CharField

db = SqliteDatabase('mft.db')


class Student(Model):
    sname = CharField(max_length=20)
    sfamily = CharField(max_length=25)
    age = IntegerField()
    
    class Meta:
        database = db


db.create_tables([Student])