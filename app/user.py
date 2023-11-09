"""User views."""

from flask import Blueprint
from markupsafe import escape

users_bp = Blueprint('user', __name__, url_prefix='/user')


@users_bp.route('/<name>', methods=('GET',))
def get(name: str):
    return f'Hello {escape(name)}'
