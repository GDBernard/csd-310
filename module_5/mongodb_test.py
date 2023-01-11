#Written By: Gavin Bernard
#Date: 1/10/2023

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

url = "mongodb+srv://admin:admin@cluster0.pqamvhe.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

try:
    client.admin.command('ismaster')
    print("Success.")
except ConnectionFailure:
    print("Server not available.")

print("-- Pytech Collection List --")
print(db.list_collection_names())
input("End of program, press any key to exit...")
