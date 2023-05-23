import requests
import json
from bson import ObjectId

def db_request():
    url = "http://127.0.0.1:5000/data"

    # set the JSON req payload
    payload = {
        "Usermame": "joashlaw",
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

def get_qr_code():
    url = "http://127.0.0.1:5000/get/qr-code"

    # set the JSON req payload
    payload = {
        "document_id": str(ObjectId("6469ac1e8cd8a56b8a1d6e43")),
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
        "document_id": str(ObjectId("646658965fdece05d6082923")),
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
    url = f'https://techducks-api-app-drhnv.ondigitalocean.app/{payload["document_id"]}/cup-count'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    data = response.json

    print(data)

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
        "time": 0.929
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
        "document_id": str(ObjectId("646658965fdece05d6082923"))
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

    url = f'http://127.0.0.1:5000/checkout/{payload["document_id"]}'

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
    }

    url = 'http://127.0.0.1:5000/leaderboard'

    headers = {
        "Content-Type": "application/json"
    }

    # convert the payload to a JSON string
    json_payload = json.dumps(payload)

    # send the POST request with the JSON payload
    response = requests.post(url, data=json_payload, headers=headers)

    data = response.json()

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


if __name__ == '__main__':
    pass
    # print(post_request())

    # db_request()  # create profile
    # get_qr_code()  # get qr code / create new qr code
    # update_request()  # update profile details
    # delete_request()  # delete profile
    getcup_request()  # get cup count
    # updatecup_request()  # increase cup count by 1
    # reaction_time()  # get reaction time, status: pass/fail
    # bonus()  # total points
    # discount()  # if pass: discounts for nth cup
    # checkoutbutton()  # if pass: check out
    # checkoutbutton_fail()  # if fail: check out
    # leaderboard()  # top3 leaderboard
    # leaderboard_personal()  # personal position