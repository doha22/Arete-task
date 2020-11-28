# from database.db import initialize_db
from flask import Flask, request, abort, jsonify 
from database.models import Student
from database.db import CONNECTION_STRING
from flask_cors import CORS
from bson.objectid import ObjectId
import json
# import bson.objectid


# from bson.objectid import ObjectId
# from bson import ObjectId
# from pymongo.objectid import ObjectId

from pymongo import MongoClient



app = Flask(__name__)

client = MongoClient(CONNECTION_STRING)
# db = client.lin_flask
# db = client.['ARETE_task']
db = client.ARETE_task

# initialize_db(app)
# from flask_mongoalchemy import MongoAlchemy

cors = CORS(app, resources={r"/*": {"origin": "*"}})

 # Use the after_request decorator to set Access-Control-Allow

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods',
                             'GET, PATCH, POST, DELETE, OPTIONS')
    return response


@app.route('/new_student', methods=['POST'])
def create_student():

    body = request.get_json()
    if not body:
      abort(400)
    
    Student(
        name= body.get('name'),
        email= body.get('email'),
        age = body.get('age'),
        grade = body.get('grade'),
        number = body.get('number'),
        address = body.get('address')
        ).save()


    return jsonify({
        "success": True ,
        "message":"inserted "
       
      })




@app.route('/students', methods=['GET'])
def All_students():

    collection = db.Student
    # students =[doc for doc in Student.objects().all()]


    data = []
    for i in Student.objects().all():
     dataJson = i.to_json()
     res = json.loads(dataJson)
     data.append(res)

   
    cur = collection.find()
    if cur.count()==0: 
        # no data exist
        return jsonify({
                    "success": False ,            
        },404)
      
    else:
        return jsonify({
                    "success": True ,
                    "data": data   
        })
   
   




@app.route('/modify_students/<id>', methods=['PUT'])
def modify_students(id):

#   students = db.Student.updateMany({},"_id": "ObjectId(5fbfff680c01b1c38339394a)")
  
#   students = Student.objects(grade="A").first()
#   students.updateMany({})
  body = request.get_json()
#   _id= request.url
#   print(_id)
 
 
 #### add condition if id not exist or false , abort(404)

#   student = Student.objects().first()
  
  collection = db.Student

#   date= {
#         'name': body.get('name'),
#         'email': body.get('email'),
#         'age' : body.get('age'),
#         'grade' : body.get('grade'),
#         'number' : body.get('number'),
#         'address' : body.get('address')
#      } 
# 




  updated_data= collection.update_many(
       {"id":ObjectId(id)},
       {"$set":{
        'name': body.get('name'),
        'email': body.get('email'),
        'age' : body.get('age'),
        'grade' : body.get('grade'),
        'number' : body.get('number'),
        'address':body.get('address')
       }
       })
#   data = Student.objects('id'==ObjectId(id))  
#   updated_data= data.update(
#      {"id":ObjectId(id)},
#     {'$set':{
#         'name': body.get('name'),
#         'email': body.get('email'),
#         'age' : body.get('age'),
#         'grade' : body.get('grade'),
#         'number' : body.get('number'),
#        }})
     
  
  
  if updated_data: 
    return jsonify({
                    "success": True ,
                    "message":"successed"     
                })
  
      



@app.route('/delete-student/<id>', methods=['Delete'])
def delete_student(id):
    student = Student.objects('id'==ObjectId(id)).first()
    data = student.delete()
    return jsonify({
                "success": True ,
                "message":"Deleted"  
      })
    

#check that link
#  https://stackoverflow.com/questions/8109122/how-to-sort-mongodb-with-pymongo
@app.route('/sort-data/', methods=['GET'])
def sort_student():
    collection = db['Student']
    collection.find().sort('UserName', -1)  #asce
    collection.find().sort('UserName', 1)   #desce

    # Order by ascending date
# blogs = BlogPost.objects().order_by('date')    # equivalent to .order_by('+date')

# Order by ascending date first, then descending title
# blogs = BlogPost.objects().order_by('+date', '-title')





@app.route("/")
def home():
    return "Hello, World!"

    

    
if __name__ == "__main__":
    app.run(debug=True)