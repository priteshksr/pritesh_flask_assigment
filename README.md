# pritesh_flask_assigment

wesite is available after running "make run" at http://127.0.0.1:5000/





Entity : Student
API methods
1. GET: http://127.0.0.1:5000/student
OUTPUT: return all students from database
2. GET:http://127.0.0.1:5000/student?id=1
OUTPUT: return student with specific id from database
3. POST:http://127.0.0.1:5000/student
body(content type: json)
{
  "name": "RAM"
  "Class_id": ""
}
OUTPUT: add sudent to database
4. PUT:http://127.0.0.1:5000/student
body(content type: json)
{
  "id": 1
  "name": "SHYAM"
  "Class_id": 2
}
please note that there should be class present with the specific id
OUTPUT: return updated student with id 
5. DELETE:http://127.0.0.1:5000/student?id=1
OUTPUT:delete student from database


Entity : CLASS
API methods
1. GET: http://127.0.0.1:5000/class
OUTPUT: return all classes from database
2. GET:http://127.0.0.1:5000/class?id=1
OUTPUT: return class with specific id from database
3. POST:http://127.0.0.1:5000/class
body(content type: json)
{
  "name": "CLASS V"
  "Class_leader": ""
}
OUTPUT: add sudent to database
4. PUT:http://127.0.0.1:5000/student
body(content type: json)
{
  "id": 1
  "name": "CLASS VI"
  "Class_leader": 1
}
please note that there should be student present with the specific id
OUTPUT: return updated class with id=1 
5. DELETE:http://127.0.0.1:5000/class?id=1
OUTPUT:delete class from database
