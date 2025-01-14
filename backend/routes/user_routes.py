from flask import Blueprint, request, jsonify
from models.test_data import db, User
from werkzeug.security import generate_password_hash, check_password_hash

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    hashed_password = generate_password_hash(password, method='sha256')

    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Signup successful!', 'name': name}), 201

@user_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful!'}), 200

    return jsonify({'message': 'Invalid credentials!'}), 401