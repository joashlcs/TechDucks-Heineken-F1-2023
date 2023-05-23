from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import base64
import json

import qrcode

from pymongo import MongoClient
from bson import ObjectId
from flask import Flask, jsonify, request
from flask_cors import CORS
import time


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder


# instantiate the app
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})



uri = "mongodb+srv://joashlaw75:ZYBr2Mz755fjfKsy@techduckss.djmyure.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['clientbase']
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
#     {'penalty': 0.7},
#
#     {'beer disc1': 0.9},
#     {'beer disc2': 0.85},
#     {'beer disc3^': 0.8}
#
# ]
# #
# # # Insert the document into the collection
# table.insert_many(data)


@app.route("/data", methods=["POST"])
def store_data():
    data = request.get_json()
    query = {
        "Username": data['Username'],
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

@app.route('/get/qr-code', methods=['POST'])
def get_qr():
    data = request.get_json()
    query = {
        'document_id' : data['document_id']
    }

    result = collection.find_one({"_id": ObjectId(query['document_id'])}, {'qr_img': 1})

    if result and 'qr_img' in result:
        qr_img = result['qr_img']

        return jsonify({'qr_code_id': str(qr_img)}), 200

    else:  #make a qr code
        qrc = qrcode.QRCode(version=1, box_size=10, border=4)
        qrc.add_data(query)
        qrc.make(fit=True)
        qr_img = qrc.make_image(fill='black', back_color='white')
        qr_img_byte_array = qr_img.get_image().tobytes()
        qr_img_base64 = base64.b64encode(qr_img_byte_array).decode('utf-8')

        qr_img.save(f"{query['document_id']}_qr.png")

        collection.update_one({"_id": ObjectId(query['document_id'])}, {"$set": {'qr_img': qr_img_base64}})

        return jsonify({'qr_code_id': str(qr_img_base64)}), 200

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
        cups = document.get('cups', 0)
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
        time2 = data["time"]
        status = time2 < 0.6
        if status:
            response = {"status": "passed"}
        else:
            response = {"status": "failed"}

        collection.update_one({"_id": ObjectId(query["document_id"])}, {"$set": {"status": status, "time": time2}})
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
        time2 = document.get('time', 0)
        table = db['bonus']

        def check_timing(time2, table):
            if time2 < 0.150:
                pt1 = None
                q1 = {"le 150ms": {'$exists': True}}
                cur1 = table.find(q1)

                r1 = []
                for doc1 in cur1:
                    r1.append(doc1)

                if r1:
                    pt1 = r1[0].get("le 150ms")
                return pt1

            elif 0.151 <= time2 <= 0.250:
                pt2 = None
                q2 = {"le 250ms": {'$exists': True}}
                cur2 = table.find(q2)

                r2 = []
                for doc2 in cur2:
                    r2.append(doc2)

                if r2:
                    pt2 = r2[0].get("le 250ms")
                return pt2

            elif 0.251 <= time2 <= 0.400:
                pt3 = None
                q3 = {"le 400ms": {'$exists': True}}
                cur3 = table.find(q3)

                r3 = []
                for doc3 in cur3:
                    r3.append(doc3)

                if r3:
                    pt3 = r3[0].get("le 400ms")
                return pt3

            elif 0.401 <= time2 <= 0.600:
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
                return 1

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

            elif current_cups >= 5:
                c = table.find({"glass 5^": 25})
                results = []
                points_5 = 0
                for docs in c:
                    results.append(docs)

                if results:
                    points_5 = results[0].get('glass 5^')

            if points or points_5:
                bonus_multiplier = check_timing(time2, table)
                if points is not None:
                    final = bonus_multiplier * points
                    final = round(final, 2)

                    return final, bonus_multiplier
                else:
                    final = bonus_multiplier * points_5
                    final = round(final, 2)
                    return final, bonus_multiplier

        final, discount_percentage = cup()
        if final and discount_percentage is not None:
            collection.update_one({"_id": ObjectId(query["document_id"])}, {"$set": {"final_point": final}})
            for i in range(5):
                check = collection.find_one({"_id": ObjectId(query["document_id"])}, {"final_point": 1})
                if check == final:
                    break
                else:
                    time.sleep(1)
                    continue


    response = {"message": f"{final}"}
    return jsonify(response)

@app.route('/<document_id>/discount', methods=['POST'])
def discount(document_id):
    data = request.get_json()
    beer_discount = None
    beer_discount1 = None

    # Find the document in MongoDB
    document = collection.find_one(ObjectId(document_id))
    price = 10
    if document:
        status = document.get('status', 0)
        if status:
            cup_count = document.get('cups', 0)
            cup_count = cup_count + 1
            if cup_count in [1, 2]:
                beer_disc = f'beer disc{cup_count}'
                query = {beer_disc: {'$exists': True}}
                cursor = table.find(query)
                result = []
                beer_discount1 = 0
                for doc in cursor:
                    result.append(doc)

                if result:
                    beer_discount1 = result[0].get(f'{beer_disc}')

            elif cup_count >= 3:
                beer_disc = table.find({"beer disc3^": 0.8})
                results = []
                beer_discount = 0
                for b in beer_disc:
                    results.append(b)

                if results:
                    beer_discount = results[0].get('beer disc3^')

            if beer_discount or beer_discount1:
                if beer_discount1 is not None:
                    final1 = price * beer_discount1
                    final1 = round(final1, 2)
                    dd1 = round((1 - beer_discount1) * 100, 2)
                    response = {
                        "discount_percentage": dd1,
                        "final_price": final1
                    }

                    return jsonify(response)

                else:
                    final = price * beer_discount
                    final = round(final, 2)
                    dd = round((1 - beer_discount) * 100, 2)
                    response = {
                        "discount_percentage": dd,
                        "final_price": final
                    }
                    return jsonify(response)

        else:
            response = {'message': 'there is no discount available'}
            return jsonify(response)


@app.route('/checkout/<document_id>', methods=['POST'])
def check_out(document_id):
    data = request.get_json()

    button = data.get("button_id")

    document = collection.find_one({"_id": ObjectId(document_id)})

    if document and button == 'free_drinkaid_button':
        da = document.get('current_drinkaid', 0)
        nda = da + 1

        collection.update_one({"_id": ObjectId(document_id)}, {"$set": {"current_drinkaid": nda}})
        responseaidfree = {"message": "Checked out successfully with discounted drinkaid"}

        return jsonify(responseaidfree), 200

    elif document and button == 'discount_beer_button':
        responsebeer = {"message": "Checked out successfully with beer discount"}
        return jsonify(responsebeer), 200
    else:
        response400 = {"error": "Invalid data received"}
        return jsonify(response400), 400


@app.route('/<document_id>/check-out-false', methods=['POST'])
def check_out_fail(document_id):
    data = request.get_json()

    button = data.get("button_id")

    document = collection.find_one({"_id": ObjectId(document_id)})

    if document and button == 'normal_beer_button':
        responsenorm = {"message": "Checked out successfully with NO discounted beer"}
        return jsonify(responsenorm), 200

    elif document and button == 'discount_drinkaid_button':

        da = document.get('current_drinkaid', 0)
        nda = da + 1
        collection.update_one({"_id": ObjectId(document_id)}, {"$set": {"current_drinkaid": nda}})

        da_disc = table.find({"drinkaid": 0.5})
        resultsaid = []
        da_discount = 0
        price = 3.20
        for o in da_disc:
            resultsaid.append(o)

        if resultsaid:
            da_discount = resultsaid[0].get('drinkaid')

        if da_discount is not None:
            finald = price * da_discount
            ddd = round((1 - da_discount) * 100, 2)

            responseaid = {
                "discount_percentage": ddd,
                "final_price": finald
            }

            return jsonify(responseaid), 200
    else:
        response401 = {"error": "Invalid data received"}
        return jsonify(response401), 400


@app.route('/leaderboard', methods=['POST'])
def leaderboard():
    data = request.get_json()
    button = data.get("button_id")

    if button == "top_3":
        result = collection.find().sort("final_point", -1).limit(3)

        # Clear existing ranks
        collection.update_many({}, {'$unset': {'rank': 1}})

        top3 = []
        rank = 0
        for document in result:
            document_id = str(document['_id'])
            rank += 1
            collection.update_one({'_id': ObjectId(document_id)}, {'$set': {'rank': rank}})
            top3.append(document)

        response = {}
        if len(top3) >= 1:
            first = top3[0]
            first['_id'] = str(first['_id'])
            response["first"] = first

        if len(top3) >= 2:
            second = top3[1]
            second['_id'] = str(second['_id'])
            response["second"] = second

        if len(top3) >= 3:
            third = top3[2]
            third['_id'] = str(third['_id'])
            response["third"] = third

        return jsonify(response)


@app.route('/leaderboard/<document_id>', methods=['POST'])
def leaderboard_personal(document_id):
    data = request.get_json()

    document = collection.find_one(ObjectId(document_id))
    if document:
        # sort_criteria = [('FirstName', 1), ('LastName', 1), ('final_point', 1)]
        result_ranks = collection.find().sort('final_point', -1)
        rank = 0
        for documents in result_ranks:
            document_ids = documents['_id']
            rank += 1
            collection.update_one({'_id': ObjectId(document_ids)}, {'$set': {'rank': rank}})

        collect_rank = collection.find_one(ObjectId(document_id), {'rank': 1,'final_point': 1})

        if collect_rank and 'rank' in collect_rank and 'final_point' in collect_rank:
            rankie = collect_rank['rank']
            pointie = collect_rank['final_point']

            response = {'user_rank': f"{rankie}",
                        'user_point': f"{pointie}"}

        return jsonify(response)

if __name__ == '__main__':
    app.run()
