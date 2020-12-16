import os
import unittest
import json
from pymongo import MongoClient
from backend.database.models import Student
from backend.database.db import CONNECTION_STRING

class StudentTestCase(unittest.TestCase):

    def test_success_create_new_student(self):
        response = self.client().post('/new_student',json={
            'name': 'rana',
            'email': 'rana@nti.com',
            'address': 'nasr city',
            'number': '201-10',
            'degree':'A',
            'age':25
        })
        data = json.loads(response.data)
        res = Student({
             'name': 'rana',
            'email': 'rana@nti.com',
            'address': 'nasr city',
            'number': '201-10',
            'degree':'A',
            'age':25
        }).save()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(res)

    
    def test_success_list_student(self):
        response = self.client().get('/students')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertNotEqual(len(data['data']), 0)


    def test_failure_list_student(self):
        response = self.client().get('/students')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(len(data['data']), 0)

    # def test_success_delete_student(self):
    #     response = self.client().get('/delete-student/<id>')

    #     student = Student.objects('id'==ObjectId(id)).first()
    #     data = student.delete()



       
