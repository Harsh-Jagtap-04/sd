from flask_sqlalchemy import SQLAlchemy
from config import DB_CONFIG

db = SQLAlchemy()

# Additional manual DB connection setup if needed
import pymysql

def create_connection():
    connection = pymysql.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database']
    )
    return connection
