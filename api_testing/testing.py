import requests
import json
from bson import ObjectId



# def post_request():
#     # set the URL of the API endpoint
#     url = "http://127.0.0.1:5000/books"
#
#     # set the JSON request payload
#     payload = {
#         "bot_id": 10
#     }
#
#     # convert the payload to a JSON string
#     json_payload = json.dumps(payload)
#
#     # set the headers of the request
#     headers = {
#         "Content-Type": "application/json"
#     }
#
#     # send the POST request with the JSON payload
#     response = requests.post(url, data=json_payload, headers=headers)
#
#     # get the response status code and content
#     if not response.ok:
#         return False
#     else:
#         return True

# def delete_request():
#     # URL of the API endpoint
#     url = 'http://127.0.0.1:5000/books/173ed8821adb420881e6c7691ee94fea'
#
#     # Data to be sent in the PUT request
#     put_data = {'title': 'On the Road', 'author': 'Jack Kerouac', 'read': False}
#
#     # Make the PUT request
#     response = requests.put(url, json=put_data)
#
#     # Print the response
#     print(response.json())
#
#     # Data to be sent in the DELETE request
#     delete_data = {}
#
#     # Make the DELETE request
#     response = requests.delete(url, json=delete_data)
#
#     # Print the response
#     print(response.json())

def db_request():
    url = "http://127.0.0.1:5000/data"

    # set the JSON req payload
    payload = {
        "FirstName": "Joash",
        "LastName": "Law",
        "DOB": 11022003,
        "Contact": 91500846,
        "Email": "joashlaw75@gmail.com",
        "PW": "xtyxcykthgfcgvk"
    }

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

# send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}") # f"Response Content: {content}")

def new_qr_code():
    url = "http://127.0.0.1:5000/new-qr-code"

    # set the JSON req payload
    payload = {
        "document_id": str(ObjectId("64663cd81b4fb124d27861c2")),
    }

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}")

def update_request():
    url = "http://127.0.0.1:5000/update-data"

    # set the JSON req payload
    payload = {
        "document_id": str(ObjectId("64663cd81b4fb124d27861c2")),
        "FirstName": "Joash",
        "LastName": "Law",
        "DOB": "11-02-2003",
        "Contact": 91500846,
        "Email": "joashlaw75@gmail.com",
        "PW": "xtyxcykthgfcgvk"
    }

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

# send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}") # f"Response Content: {content}")

def delete_request():
    url = "http://127.0.0.1:5000/delete-data"

    # set the JSON req payload
    payload = {
        "document_id": str(ObjectId("64663d651b4fb124d27861c3")),
    }

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

# send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}") # f"Response Content: {content}")

def getcup_request():  # first scan at kiosk

    payload = {
        "document_id": str(ObjectId("646658965fdece05d6082923"))
    }

    # set the JSON req payload
    url = f'http://127.0.0.1:5000/{payload["document_id"]}/cup-count'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}")

def updatecup_request():  # when they purchase a cup

    # set the JSON req payload
    payload = {
        "document_id": str(ObjectId("646658965fdece05d6082923"))
    }

    url = f'http://127.0.0.1:5000/{payload["document_id"]}/cup-update'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}")

def reaction_time():
    payload = {
        "document_id": str(ObjectId("646658965fdece05d6082923")),
        "time": 0.399
    }

    url = f'http://127.0.0.1:5000/{payload["document_id"]}/reaction-time'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}")

def bonus():
    payload = {
        "document_id": str(ObjectId("6469ac1e8cd8a56b8a1d6e43"))
    }

    url = f'http://127.0.0.1:5000/{payload["document_id"]}/bonus'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}")

def discount():
    payload = {
        "document_id": str(ObjectId("646658965fdece05d6082923"))
    }

    url = f'http://127.0.0.1:5000/{payload["document_id"]}/discount'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}")

def checkoutbutton():
    payload = {
        "document_id": str(ObjectId("646658965fdece05d6082923")),
        # "button_id": "discount_beer_button"
        "button_id": "free_drinkaid_button"
    }

    url = f'http://127.0.0.1:5000/{payload["document_id"]}/checkout'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}")

def checkoutbutton_fail():
    payload = {
        "document_id": str(ObjectId("646658965fdece05d6082923")),
        "button_id": "discount_drinkaid_button"
        # "button_id": "normal_beer_button"
    }

    url = f'http://127.0.0.1:5000/{payload["document_id"]}/check-out-false'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}")

def leaderboard():
    payload = {
        "button_id": "top_3"
        # "button_id": "normal_beer_button"
    }

    url = 'http://127.0.0.1:5000/leaderboard'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}")

def leaderboard_personal():
    payload = {
        "document_id": str(ObjectId("6469abbc8cd8a56b8a1d6e42"))
    }


    url = f'http://127.0.0.1:5000/leaderboard/{payload["document_id"]}'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    status_code = response.status_code
    # content = response.content
    print(f"Status Code: {status_code}")
# def post_request():
#     # set the URL of the API endpoint
#     url = "http://127.0.0.1:5000/db/insertrun"
#
#     # set the JSON request payload
#     payload = {
#         "bot_id": 10
#     }
#
#     # convert the payload to a JSON string
#     json_payload = json.dumps(payload)
#
#     # set the headers of the request
#     headers = {
#         "Content-Type": "application/json"
#     }
#
#     # send the POST request with the JSON payload
#     response = requests.post(url, data=json_payload, headers=headers)
#
#     # get the response status code and content
#     if not response.ok:
#         return InsertBotRunResponse(status=ResponseStatus.FAILED, data=InsertBotRunFail(json.loads(response.text)))
#     return InsertBotRunResponse(status=ResponseStatus.SUCCESS, data=InsertBotRunSuccess(json.loads(response.text)))
#
#
# def update_request(botrun_id):
#     # set the URL of the API endpoint
#     url = "http://127.0.0.1:5000/db/updaterun"
#
#     # set the JSON request payload
#     payload = {
#         "botrun_id": botrun_id,
#         "status": 1,
#         "remarks": ''
#     }
#
#     # convert the payload to a JSON string
#     json_payload = json.dumps(payload)
#
#     # set the headers of the request
#     headers = {
#         "Content-Type": "application/json"
#     }
#
#     # send the POST request with the JSON payload
#     response = requests.post(url, data=json_payload, headers=headers)
#
#     # get the response status code and content
#     status_code = response.status_code
#     content = response.content
#
#     # print the response status code and content
#     print(f"Response Status Code: {status_code}")
#     print(f"Response Content: {content}")




if __name__ == '__main__':
    pass
    # print(post_request())

    # db_request()
    # update_request()
    # delete_request()
    # getcup_request()
    # updatecup_request()
    # reaction_time()
    # bonus()
    # discount()
    checkoutbutton()
    # checkoutbutton_fail()
    # leaderboard()
    # leaderboard_personal()