# build-a-REST-API-with-FLASK

# Flask REST API - User Management

This is a simple REST API built with Flask to demonstrate the fundamentals of API development. The API supports basic CRUD operations (Create, Read, Update, Delete) for managing users stored in memory.

---

##  Features

-  List all users (GET `/users`)
-  Get a specific user by ID (GET `/users/<id>`)
-  Create a new user (POST `/users`)
-  Update an existing user (PUT `/users/<id>`)
-  Delete a user (DELETE `/users/<id>`)

---

##  Tech Stack

- Python 3.x
- Flask
- Postman or `curl` (for testing)

---

##  Project Structure
- app.py
- requirements.txt


---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/build-a-REST-API-with-FLASK.git
cd build-a-REST-API-with-FLASK


 ## Install Dependencies
pip install -r requirements.txt

## Run the flask app

python app.py


## API Endpoints


## GET All Users

GET /users

## GET User by ID

GET /users/<id>


## Create User

POST /users
Content-Type: application/json

{
  "name": "Alice",
  "email": "alice@example.com"
}


## Update User

PUT /users/<id>
Content-Type: application/json

{
  "name": "Updated Name"
}


## Delete User


DELETE /users/<id>


## requirements.txt
flask

Generate this using:

pip freeze > requirements.txt

 License
This project is licensed under the MIT License - free to use and modify.

Author
Made by Reddy Ramanjaneyulu
---










