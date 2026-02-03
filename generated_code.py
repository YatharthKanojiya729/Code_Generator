```python
# Importing required libraries
from flask import Flask, request, jsonify

# Creating a new instance of the Flask class
app = Flask(__name__)

# Sample route to test the application
@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'

# Sample route to handle POST requests
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    if 'name' in data and 'email' in data:
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'message': 'Invalid request'}), 400

# Sample route to handle GET requests with query parameters
@app.route('/users', methods=['GET'])
def get_users():
    name = request.args.get('name')
    email = request.args.get('email')
    if name and email:
        return jsonify({'message': f'User {name} with email {email} found'}), 200
    else:
        return jsonify({'message': 'Invalid request'}), 400

# Sample route to handle PUT requests
@app.route('/update_user', methods=['PUT'])
def update_user():
    data = request.json
    if 'id' in data and 'name' in data and 'email' in data:
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'message': 'Invalid request'}), 400

# Sample route to handle DELETE requests
@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    return jsonify({'message': 'User deleted successfully'}), 200

# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

To run the code, save it in a file named `app.py` and execute it using the following command:

```bash
python app.py
```

Then, you can test the routes using a tool like `curl` or a REST client like Postman.