#Written By: Gavin Bernard
#Date: 1/11/2023

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

url = "mongodb+srv://admin:admin@cluster0.pqamvhe.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

alice = {
    "student_id": "1007",
    "first_name": "Alice",
    "last_name": "Amora",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "3.5",
            "start_date": "June 5, 2023",
            "end_date": "August 30, 2023",
            "courses": [
                {
                    "course_id": "CH-115-S1",
                    "description": "General Chemistry I",
                    "instructor": "Ms. Echo",
                    "grade": "95"
                },
                {
                    "course_id": "CH-306-S2",
                    "description": "Biochemistry",
                    "instructor": "Mr. Davidson",
                    "grade": "92"
                }
            ]
        }
    ]
}

bob = {
    "student_id": "1008",
    "first_name": "Bob",
    "last_name": "Billy",
    "enrollments": [
        {
            "term": "Fall",
            "gpa": "3.2",
            "start_date": "August 30, 2023",
            "end_date": "December 18, 2023",
            "courses": [
                {
                    "course_id": "CJUS-335",
                    "description": "Crime in America",
                    "instructor": "Dr. Jones",
                    "grade": "83"
                },
                {
                    "course_id": "HI-110",
                    "description": "World History I",
                    "instructor": "Prof. Thomas",
                    "grade": "84"
                }
            ]
        }
    ]
}

charlie = {
    "student_id": "1009",
    "first_name": "Charlie",
    "last_name": "Clinton",
    "enrollments": [
        {
            "term": "Winter",
            "gpa": "4.0",
            "start_date": "December 18, 2023",
            "end_date": "March 15, 2024",
            "courses": [
                {
                    "course_id": "AR-204",
                    "description": "Introduction to Painting",
                    "instructor": "Dr. Sarah",
                    "grade": "100"
                },
                {
                    "course_id": "CH-115-S1",
                    "description": "General Chemistry I",
                    "instructor": "Ms. Echo",
                    "grade": "98"
                }
            ]
        }
    ]
}

try:
    client.admin.command('ismaster')
    print("Success.")
except ConnectionFailure:
    print("Server not available.")

students = db.students

print("\n  -- INSERT STATEMENTS --")
alice_student_id = students.insert_one(alice).inserted_id
print("  Inserted student record Alice Amora into the students collection with document_id " + str(alice_student_id))

bob_student_id = students.insert_one(bob).inserted_id
print("  Inserted student record Bob Billy into the students collection with document_id " + str(bob_student_id))

charlie_student_id = students.insert_one(charlie).inserted_id
print("  Inserted student record Charlie Clinton into the students collection with document_id " + str(charlie_student_id))

input("\n\n  End of program, press any key to exit... ")
