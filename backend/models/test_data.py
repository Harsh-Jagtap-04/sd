from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TestData(db.Model):
    __tablename__ = 'test_data'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    mobile = db.Column(db.String(15))
    level = db.Column(db.String(50))
    testname = db.Column(db.String(100))
    attempt = db.Column(db.Integer)
    batch = db.Column(db.String(50))
    invites_time = db.Column(db.String(50))
    invited = db.Column(db.Integer)
    not_appeared = db.Column(db.Integer)
    appeared = db.Column(db.Integer)
    lowest_score = db.Column(db.Float)
    highest_score = db.Column(db.Float)
    test_status = db.Column(db.String(50))
    submitted_date = db.Column(db.String(50))
    

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))