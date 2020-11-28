from flask import Flask
import pymongo
# import mongoengine
from mongoengine import connect

from pymongo import MongoClient


CONNECTION_STRING = "mongodb+srv://admin:1234@cluster0.09j4d.mongodb.net/ARETE_task?retryWrites=true&w=majority"
# mongo = pymongo.MongoClient(CONNECTION_STRING,connect=False)

# db = pymongo.database.Database(mongo, 'Student')
# col = pymongo.collection.Collection(db, 'mycollection')

connect(host=CONNECTION_STRING)



