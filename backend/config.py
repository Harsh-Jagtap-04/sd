DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "excel_data",
}

class Config:
    SECRET_KEY = "your_secret_key"
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}/{DB_CONFIG['database']}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
