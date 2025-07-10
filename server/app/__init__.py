import os
from flask import *
from .routes.auth import auth_bp
from .extensions import db
from dotenv import load_dotenv


def create_app():

    load_dotenv()
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    app.secret_key = "1234"
    app.register_blueprint(auth_bp)

    return app