from .db import *
from mongoengine import Document, StringField, FloatField,IntField

# class Student(db.Document):
#     name = db.StringField(required=True, unique=True)
#     age = db.IntegerField()


    
class Student(Document):
    name = StringField(required=True)
    age = IntField()
    email = StringField()
    grade = StringField(max_lenght=2)
    number = StringField()
    address = StringField()
    meta = {'collection':'Student'}

    # def __init__(self, name, age, email, grade,number,address):
    #     self.name=name
    #     self.age= age
    #     self.email=email
    #     self.grade= grade
    #     self.number=number
    #     self.address=address

    

 