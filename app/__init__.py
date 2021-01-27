from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config['SECRET_KEY'] = 'SUPER SECRET'

    return app