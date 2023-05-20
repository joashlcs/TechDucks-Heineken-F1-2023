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

table = db['bonus']
# data = [
#     {'glass 1': 10},
#     {'glass 2': 12},
#     {'glass 3': 15},
#     {'glass 4': 18},
#     {'glass 5^': 25},
#
#     {'le 150ms': 2},
#     {'le 250ms': 1.6},
#     {'le 400ms': 1.35},
#     {'le 600ms': 1.10},
#
#     {'drinkaid': 0.5},
#     {'penalty': 0.7}
# ]
#
# # Insert the document into the collection
# table.insert_many(data)


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

    if not data["document_id"]:
        response = {"error": "Invalid payload. Missing 'document_id'."}
        return jsonify(response), 400

    query = {
        "document_id": data["document_id"]
    }
    document = collection.find_one({"_id": ObjectId(document_id)})

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

@app.route('/<document_id>/reaction-time', methods=['POST'])
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
        status = time < 0.6
        if status:
            response = {"status": "passed"}
        else:
            response = {"status": "failed"}

        collection.update_one({"_id": ObjectId(query["document_id"])}, {"$set": {"status": status, "time": time}})
        return jsonify(response)

    else:
        return jsonify({'error': 'Document not found'})

@app.route('/<document_id>/bonus', methods=['POST'])
def bonus_chart(document_id):
    data = request.get_json()
    table = db['bonus']

    query = {
        "document_id": data["document_id"]
    }

    document = collection.find_one(ObjectId(document_id))
    if document:
        current_cups = document.get('cups', 0)
        time = document.get('time', 0)
        table = db['bonus']

        def check_timing(time, table):
            if time < 0.150:
                pt1 = None
                q1 = {"le 150ms": {'$exists': True}}
                cur1 = table.find(q1)

                r1 = []
                for doc1 in cur1:
                    r1.append(doc1)

                if r1:
                    pt1 = r1[0].get("le 150ms")
                return pt1

            elif 0.151 <= time <= 0.250:
                pt2 = None
                q2 = {"le 250ms": {'$exists': True}}
                cur2 = table.find(q2)

                r2 = []
                for doc2 in cur2:
                    r2.append(doc2)

                if r2:
                    pt2 = r2[0].get("le 250ms")
                return pt2

            elif 0.251 <= time <= 0.400:
                pt3 = None
                q3 = {"le 400ms": {'$exists': True}}
                cur3 = table.find(q3)

                r3 = []
                for doc3 in cur3:
                    r3.append(doc3)

                if r3:
                    pt3 = r3[0].get("le 400ms")
                return pt3

            elif 0.401 <= time <= 0.600:
                pt4 = None
                q4 = {"le 600ms": {'$exists': True}}
                cur4 = table.find(q4)

                r4 = []
                for doc4 in cur4:
                    r4.append(doc4)

                if r4:
                    pt4 = r4[0].get("le 600ms")
                return pt4
            else:
                return 0

        def cup():
            points = None
            points_6 = None

            if current_cups in range(1, 5):
                glass_name = f'glass {current_cups}'
                query = {glass_name: {'$exists': True}}
                cursor = table.find(query)
                result = []
                points = 0
                for doc in cursor:
                    result.append(doc)

                if result:
                    points = result[0].get(glass_name)

            elif current_cups >= 6:
                c = table.find({"glass 5^": 25})
                results = []
                points_6 = 0
                for docs in c:
                    results.append(docs)

                if results:
                    points_6 = results[0].get('glass 5^')

            if points or points_6:
                bonus_multiplier = check_timing(time, table)
                if points is not None:
                    final = bonus_multiplier * points
                    return final
                else:
                    final = bonus_multiplier * points_6
                    return final

        fpoint = document.get('final_point', 0)
        if fpoint is not 0:  # there is alr a prev record
            pt_update = cup()
            final = fpoint + pt_update
            collection.update_one({"_id": ObjectId(query["document_id"])}, {"$set": {"final_point": final}})

        else:
            final = cup()
            collection.update_one({"_id": ObjectId(query["document_id"])}, {"$set": {"final_point": final}})

    response = {"message": f"you have {final} points"}
    return jsonify(response)


if __name__ == '__main__':
    app.run()
