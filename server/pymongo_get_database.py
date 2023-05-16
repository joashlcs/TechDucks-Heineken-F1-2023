from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2')  # Establish a connection to the MongoDB server
db = client['clientbase']  #database
c = client.list_database_names()
print(c)


if db in c:
    print("inserted")
else:
    print("nope")
collection = db['users']  #db.users