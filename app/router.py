"""Main Router."""

from flask import Flask
from app.user import users_bp

class MainRouter:

    def __init__(self, app: Flask) -> None:
        app.register_blueprint(users_bp)
