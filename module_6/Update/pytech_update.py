#Written By: Gavin Bernard
#Date: 1/16/2023

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

url = "mongodb+srv://admin:admin@cluster0.pqamvhe.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})

try:
    client.admin.command('ismaster')
    print("Connection Successful.")
except ConnectionFailure:
    print("Server not available.")


print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Anita"}})

alice = students.find_one({"student_id": "1007"})

print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

print("  Student ID: " + alice["student_id"] + "\n  First Name: " + alice["first_name"] + "\n  Last Name: " + alice["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")
