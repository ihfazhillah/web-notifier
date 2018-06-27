from flask import Flask
from .admin import admin

def create_app():
    app = Flask(__name__)
    admin.init_app(app)

    @app.route("/")
    def index():
        return "Hello world"

    return app