from flask import Blueprint, request, jsonify
from models.test_data import db, TestData
import pandas as pd

admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/upload', methods=['POST'])
def upload_excel():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded!'}), 400

    file = request.files['file']
    df = pd.read_excel(file)

    records = df.to_dict(orient='records')

    for record in records:
        test_name_parts = record['Test name'].split('_')
        level = test_name_parts[0]
        testname = "_".join(test_name_parts[1:-1])
        attempt = int(test_name_parts[-1].replace('Attempt', '').strip())

        test_data_entry = {
            "name": record['Name'],
            "email": record['Email'],
            "mobile": record['Mobile'],
            "level": level,
            "testname": testname,
            "attempt": attempt,
            "batch": record['Batch'],
            "invites_time": record['Invites Time'],
            "invited": record['Invited'],
            "not_appeared": record['Not Appeared'],
            "appeared": record['Appeared'],
            "lowest_score": record['Lowest Score'],
            "highest_score": record['Highest Score'],
            "test_status": record['Test Status'],
            "submitted_date": record['Submitted Date']
        }

        if not TestData.query.filter_by(email=test_data_entry['email'], testname=test_data_entry['testname'], attempt=test_data_entry['attempt']).first():
            new_entry = TestData(**test_data_entry)
            db.session.add(new_entry)

    db.session.commit()
    return jsonify({'message': 'Data uploaded successfully!'}), 200

from flask import Blueprint, request, jsonify

admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email == "admin@example.com" and password == "admin123":
        return jsonify({'message': 'Admin login successful!'}), 200

    return jsonify({'message': 'Invalid credentials!'}), 401
