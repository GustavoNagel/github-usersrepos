"""Main app."""

from flask import Flask
from app.router import MainRouter
from app.database import mongo
from app.settings import Config


def create_app() -> Flask:
    """Generate a Flask application.

    :return: application itself to be started.
    """
    app = Flask(__name__)
    app.config.from_object(Config())
    mongo.init_app(app)
    MainRouter(app)
    return app
