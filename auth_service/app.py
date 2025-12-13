from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password are required!'}), 400

    if data['username'] in users:
        return jsonify({'message': 'User already exists!'}), 400

    hashed_password = generate_password_hash(data['password'], method='sha256')
    users[data['username']] = hashed_password
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = users.get(data['username'])

    if not user or not check_password_hash(user, data['password']):
        return jsonify({'message': 'Invalid credentials!'}), 401

    token = jwt.encode({'user': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
    return jsonify({'token': token})

@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing!'}), 403

    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    except:
        return jsonify({'message': 'Token is invalid!'}), 403

    return jsonify({'message': f'Welcome {data["user"]}!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)