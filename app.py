from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory list to store user data
users = [
  {"id": 1, "name": "RAM", "email": "reddyramanjaneyulu123@gmail.com"},
  {"id": 2, "name": "reddy", "email": "reddy@example.com"}
]

# Home route
@app.route('/')
def index():
    return jsonify({"message": "User Management API"})


# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user)


# POST create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        abort(400, description="Missing 'name' or 'email'")
    
    new_user = {
        "id": users[-1]['id'] + 1 if users else 1,
        "name": data['name'],
        "email": data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201


# PUT update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        abort(404, description="User not found")

    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return jsonify(user)


# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    if not any(u['id'] == user_id for u in users):
        abort(404, description="User not found")
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": f"User {user_id} deleted"})


if __name__ == '__main__':
    app.run(debug=True)
