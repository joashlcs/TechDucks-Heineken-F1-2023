# import uuid
from pymongo import MongoClient
from bson import ObjectId



from flask import Flask, jsonify, request
from flask_cors import CORS


# BOOKS = [
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'On the Road',
#         'author': 'Jack Kerouac',
#         'read': True
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Harry Potter and the Philosopher\'s Stone',
#         'author': 'J. K. Rowling',
#         'read': False
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Green Eggs and Ham',
#         'author': 'Dr. Seuss',
#         'read': True
#     }
# ]

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
#
#
# def remove_book(book_id):
#     for book in BOOKS:
#         if book['id'] == book_id:
#             BOOKS.remove(book)
#             return True
#     return False
#
#
# # sanity check route
# @app.route('/ping', methods=['GET'])
# def ping_pong():
#     return jsonify('pong!')
#
#
# @app.route('/books', methods=['GET', 'POST'])
# def all_books():
#     response_object = {'status': 'success'}
#     print(response_object)
#     if request.method == 'POST':
#         post_data = request.get_json()
#         BOOKS.append({
#             'id': uuid.uuid4().hex,
#             'title': post_data.get('title'),
#             'author': post_data.get('author'),
#             'read': post_data.get('read')
#         })
#         response_object['message'] = 'Book added!'
#     else:
#         response_object['books'] = BOOKS
#     return jsonify(response_object)
#
#
# @app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
# def single_book(book_id):
#     print(request)
#     response_object = {'status': 'success'}
#     if request.method == 'PUT':
#         post_data = request.get_json()
#         remove_book(book_id)
#         BOOKS.append({
#             'id': uuid.uuid4().hex,
#             'title': post_data.get('title'),
#             'author': post_data.get('author'),
#             'read': post_data.get('read')
#         })
#         response_object['message'] = 'Book updated!'
#     if request.method == 'DELETE':
#         remove_book(book_id)
#         response_object['message'] = 'Book removed!'
#     return jsonify(response_object)


# @app.route('/qrcode', methods=['GET'])
# def check_qr_code():
#     qr_code = request.args.get('code')
#
#     # Query the database
#     result = collection.find_one({'code': qr_code})
#
#     if result:
#         # QR code exists
#         response = {"exists": True}
#         print("It exists, hooray")
#     else:
#         # QR code does not exist
#         response = {"exists": False}
#         collection.insert_one(qr_code)
#         print("Nope. Not existing")
#
#     return jsonify(response)

client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2')  # Establish a connection to the MongoDB server
db = client['clientbase']  # database
collection = db['users']

@app.route("/data", methods=["POST"])
def store_data():
    data = request.get_json()
    query = {
        "FirstName": data['FirstName'],
        "LastName": data['LastName'],
        "DOB": data['DOB'],
        "Contact": data['Contact'],
        "Email": data['Email'],
        "PW": data['PW']
    }

    result = collection.find_one(query, {'_id': 1})

    if result:
        # Data exists
        response = {"exists": True, "message": "document already exists", '_id': 1}
    else:
        # Data does not exist
        response = {"exists": False, "message": "adding document to collection", '_id': 1}
        collection.insert_one(query)

    return jsonify(response)

@app.route('/update-data', methods=['POST'])
def update_data():
    data = request.get_json()
    query = {
        "document_id": data["document_id"]
    }

    # query2 = {
    #     "FirstName": data['FirstName'],
    #     "LastName": data['LastName'],
    #     "DOB": data['DOB'],
    #     "Contact": data['Contact'],
    #     "Email": data['Email']
    # }

    # Query the database
    result = collection.find_one(ObjectId(query["document_id"]))

    if result:
        # Data exists, update it
        new_data = {
            "$set":
                {
            "FirstName": data['FirstName'],
            "LastName": data['LastName'],
            "DOB": data['DOB'],
            "Contact": data['Contact'],
            "Email": data['Email']
        }
        }

        collection.update_one({"_id": ObjectId(query["document_id"])}, new_data)

        cursor = collection.find()
        for record in cursor:
            print(record)

        response = {"message": "Data updated successfully"}

    else:
        # Data does not exist
        response = {"message": "Data not found, please sign up"}

    return jsonify(response)

@app.route('/delete-data', methods=['POST'])
def delete_data():
    data = request.get_json()
    query = {
        "document_id": data["document_id"]
    }

    # Delete the data from the database
    result = collection.find_one(ObjectId(query["document_id"]))

    if result:
        document = collection.delete_one({"_id": ObjectId(query["document_id"])})
        print({"message": "Document deleted"})
    else:
        print({"message": "Data not found"})

    if document.deleted_count > 0:
        # Data deleted successfully
        response = {"message": "Data deleted successfully"}
    else:
        # Data not found
        response = {"message": "Data deleted unsuccessfully"}

    return jsonify(response)

@app.route('/<document_id>/cup-count', methods=['POST'])
def cup_count(document_id):
    data = request.get_json()
    query = {
        "document_id": data["document_id"]
    }
    document = collection.find_one(ObjectId(document_id))

    if document:
        # Get the cup count
        cups = 0  # or any other initial value
        collection.update_one({"_id": ObjectId(query["document_id"])}, {"$set": {"cups": cups}})
        response = {'cups': cups}
        return jsonify(response)
    else:
        response = {"message": "Data not found, please sign up"}
        return jsonify(response)

@app.route('/<document_id>/cup-update', methods=['POST'])
def cup_update(document_id):
    data = request.get_json()
    query = {
        "document_id": data["document_id"]
    }

    # Find the document in MongoDB
    document = collection.find_one(ObjectId(document_id))

    if document:
        # Increment the cup count
        current_cups = document.get('cups', 0)
        new_cups = current_cups + 1

        # Update the document with the new cup count
        collection.update_one({"_id": ObjectId(query["document_id"])}, {"$set": {"cups": new_cups}})

        return jsonify({'message': 'Cup count updated successfully'})
    else:
        return jsonify({'error': 'Document not found'})

@app.route('/<document_id>/entries', methods=['POST'])
def reaction_time(document_id):
    data = request.get_json()

    query = {
        "document_id": data["document_id"]
    }
    # Find the document in MongoDB
    document = collection.find_one(ObjectId(document_id))

    if document:
        # Get the cup count
        time = data["time"]
        status = time > 0.6
        response = {"status": status}

        collection.update_one({"_id": ObjectId(query["document_id"])}, {"$set": {"status": status}})
        return jsonify({'message': 'Reaction Time updated successfully', 'status': status})

    else:
        return jsonify({'error': 'Document not found'})

    # Assuming your entry has a 'time' field that represents the time in seconds
    time = data.get('time', 0)

    # Determine if the entry is above 0.6 seconds
    is_above_threshold = time > 0.6

    # Save the entry to the MongoDB collection
    collection.insert_one({'time': time, 'is_above_threshold': is_above_threshold})

    return jsonify(response)



if __name__ == '__main__':
    app.run()
