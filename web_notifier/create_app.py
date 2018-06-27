from flask import Flask
from .admin import admin
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    admin.init_app(app)
    db.init_app(app)

    @app.route("/")
    def index():
        return "Hello world"

    return app