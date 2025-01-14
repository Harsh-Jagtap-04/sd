from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
from models import db
from routes.admin_routes import admin_routes
from routes.user_routes import user_routes

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)

# Register Blueprints
app.register_blueprint(admin_routes, url_prefix='/admin')
app.register_blueprint(user_routes, url_prefix='/user')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
