
## Getting Started

### Installing Dependencies

#### Python 3.7


#### Dependencies


```bash
pip install -r requirements.txt
or
conda install -r requirements.txt
```

## Running the server

To run the server, execute:

```bash

conda create -n [environment name] python
conda env list
activate [environment name]


set FLASK_APP=app
set FLASK_ENV=development
flask run
```

## Tasks

 - apply curd (post , get , update , delete) 
 - sort data in table by header of table



## Endpoints 

#####  Post '/new_student'
```
   Sample
   curl http://127.0.0.1:5000/new_student -X POST -H "Content-Type: application/json" -d '{"name": "ali","email":"ali20@gmail.com","address":"naser city","number":"201-152","grade":"A","age":25}'

    - Returns: 
    {
          "success": True ,
        "message":"inserted "
      }


```

#####  GET /students
    Sample
    curl http://127.0.0.1:5000/students
      - return all students
      
      - output will be :
      {
            "success": True ,
            "data": {
                "name": "ali",
                "email":"ali20@gmail.com",
                "address":"naser city",
                "number":"201-152",
                "grade":"A",
                "age":25}

            }
      }





##### DELETE /delete-student/<id>

    Sample
    curl http://127.0.0.1:5000/delete-student/5fc190d538401f1d29150334 -X DELETE
      - delete student record  by  id 
      - return 
      
      {
         "success": True ,
         "message":"Deleted"  
     }

##### PUT /modify_students/<id>
     
     Sample
     curl http://127.0.0.1:5000/modify_students/5fc190d538401f1d29150334 -X PUT -H "Content-Type: application/json" -d '{"number":"202-152","grade":"A+"}'
      - return 
      
      {
        "success": True ,
        "message":"successed"     
    }
    
 
    
   

## Testing
To run the tests,
 run
python test.py
