# Techducks x Heineken F1 2023

## DESCRIPTION
### Theme: Digital Empowerment

#### This marketing campaign has been developed to encourage f1-goers to enjoy their beer in a responsible way! By getting to know their limit through our fun & interactive reaction test, they wil begin to be more conscious of their drinking limits. As a result, they will become much safer when drinking!

Check out our live version & give it a try [here](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs)!

## SETTING UP

1. Clone this project into your preferred IDE

2. Run the server-side Flask app in one terminal window:

    ```sh
    $ cd server
    $ python3 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ flask run --port=5000
    ```

    Flask Server is now running on [http://localhost:5000](http://localhost:5173)


3. Download MongoDB as database. 

   If you are on MacOS:

   - install [Homebrew](https://brew.sh)
   - install MongoDB through this [link](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)

   If you are on Windows:

   - install MongoDB through this [link](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)


4. Run the client-side Vue app in a different terminal window:

    ```sh
    $ cd client
    $ npm install
    $ npm run dev
    ```

    Navigate to [http://localhost:5173](http://localhost:5173) to begin your fun!

## RUNNING TESTS
### "store_data"
_Function: Create a user profile in the database_

##### To test "store_data" endpoint:

1. Send a POST request with valid user data and verify that the data is stored in the test database.
2. Send a POST request with existing user data and verify that the response indicates the document already exists.

### "get_qr"
_Function: Create a new QR Code for user + Fetch an existing QR code for user (if previously created)_

##### To test "get_qr" endpoint:

1. Send a POST request with a valid document ID and verify that a QR code is generated and returned.
2. Send a POST request with an invalid document ID and verify that an appropriate response is returned.

### "update_data" 
_Function: Update a user profile in the database_

##### To test "update_data" endpoint:

1. Send a POST request with a valid document ID and updated user data and verify that the data is updated in the test database.
2. Send a POST request with an invalid document ID and verify that an appropriate response is returned.

### "delete_data" 
_Function: Delete a user profile in the database_

##### To test "delete_data" endpoint:

1. Send a POST request with a valid document ID and verify that the corresponding document is deleted from the test database.
2. Send a POST request with an invalid document ID and verify that an appropriate response is returned.

### "cup_count" 
_Function: Fetch the cup count in the user's profile_

##### To test "cup_count" endpoint:

1. Send a POST request with a valid document ID and verify that the cup count is retrieved from the test database.
2. Send a POST request with an invalid document ID and verify that an appropriate response is returned.

### "cup_update" 
_Function: Fetch the cup count in the user's profile_

##### To test "cup_update" endpoint:

1. Send a POST request with a valid document ID and verify that the cup count is incremented in the test database.
2. Send a POST request with an invalid document ID and verify that an appropriate response is returned.

### "reaction_time" 
_Function: Check for pass/fail status based on reaction time_

##### To test "reaction_time" endpoint:

1. Send a POST request with a valid document ID and reaction time data and verify that the status is updated in the test database.
2. Send a POST request with an invalid document ID and verify that an appropriate response is returned.

### "bonus_chart"
_Function: Calculate total points based on cup count and reaction time_

##### To test "bonus_chart" endpoint:

1. Send a POST request with a valid document ID and verify that the bonus points are calculated correctly based on the cup count and reaction time.
2. Send a POST request with an invalid document ID and verify that an appropriate response is returned.

### "discount"
_Function: Verify if user is eligible for discount based on the cup count and pass/fail status for reaction time_

##### To test "discount" endpoint:

1. Send a POST request with a valid document ID and verify that the discount

### "check_out"
_Function: Free DrinkAid or Discounted Beer for users who have a pass status for reaction time_

##### To test "check_out" endpoint:

###### Check Out with Free Drinkaid Button:
1. Send a POST request to /checkout/<document_id> endpoint with valid document_id. 
2. Include the following JSON data in the request body:
        `{
           "button_id": "free_drinkaid_button"
         }`
3. Verify that the response JSON contains a "message" field with the value "Checked out successfully with discounted drinkaid".
4. Verify that the response status code is 200.

###### Check Out with Discounted Beer Button:
1. Send a POST request to /checkout/<document_id> endpoint with valid document_id.
2. nclude the following JSON data in the request body:
`{
  "button_id": "discount_beer_button"
}`
3. Verify that the response JSON contains a "message" field with the value "Checked out successfully with beer discount".
4. Verify that the response status code is 200.

###### Invalid Data Check Out Request:
1. Send a POST request to /checkout/<document_id> endpoint with valid document_id.
2. Include invalid or missing JSON data in the request body.
3. Verify that the response JSON contains an "error" field indicating invalid data.
4. Verify that the response status code is 400.

### "check_out_false"
_Function: Discounted DrinkAid for users who have a fail status for reaction time_

##### To test "check_out_false" endpoint:

###### Check Out with Normal Beer Button:
1. Send a POST request to /checkout/<document_id> endpoint with valid document_id. 
2. Include the following JSON data in the request body:
`{
  "button_id": "normal_beer_button"
}`
3. Verify that the response JSON contains a "message" field with the value "Checked out successfully with NO discounted beer".
4. Verify that the response status code is 200.

###### Check Out with Discounted Drinkaid Button:
1. Send a POST request to /checkout/<document_id> endpoint with valid document_id. 
2. Include the following JSON data in the request body:
`{
  "button_id": "discount_drinkaid_button"
}`
3. Verify that the response JSON contains the following fields:
   1. **"discount_percentage"** with the discount percentage value.
   2. **"final_price"** with the calculated final price.
4. Verify that the response status code is 200.

###### Invalid Data Check Out Request:
1. Send a POST request to /<document_id>/check-out-false endpoint with valid document_id.
2. Include invalid or missing JSON data in the request body.
3. Verify that the response JSON contains an "error" field indicating invalid data.
4. Verify that the response status code is 400.

### "leaderboard"
_Function: Fetch Top 3 users in the leaderboard based on total points accumulated_

##### To test "leaderboard" endpoint:

1. Send a POST request to /leaderboard endpoint.
2. Include the following JSON data in the request body:
`{
  "button_id": "top_3"
}`
3. Verify that the response JSON contains the top 3 ranked users' information, each with their respective position.
4. Verify that the response status code is 200.

### "leaderboard_personal"
_Function: Fetch user's position in the leaderboard based on total points accumulated_

##### To test "leaderboard_personal" endpoint:

1. Send a POST request to /leaderboard/<document_id> endpoint with valid document_id.
2. Verify that the response JSON contains a "user_rank" field with the user's rank in the leaderboard.
3. Verify that the response status code is 200.

## AUTHORS AND ACKNOWLEDGEMENT
_This Python project is created by **@JoashLaw75** and **@jiaxuane** in collaboration._


## LICENSE

[MIT](https://choosealicense.com/licenses/mit/)