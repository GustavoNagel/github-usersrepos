"""User views."""

from requests import HTTPError
from flask import Blueprint, render_template, redirect, url_for, abort, current_app
from app.github_client import list_repositories
from app.save_user import save

users_bp = Blueprint('user', __name__)


@users_bp.route('/user/<name>/', methods=('GET',))
def get_user(name: str):
    try:
        repositories = list_repositories(name)
    except HTTPError as err:
        abort(code=err.response.status_code)
    else:
        current_app.logger.info('Repositories retrieved from github! Saving in database.')
        save(name, repositories)
        return render_template('user.html', username=name, repositories=repositories)


@users_bp.route('/user/', methods=('GET',))
def home():
    return render_template('user.html')


@users_bp.route('/', methods=('GET',))
def index():
    return redirect(url_for('user.home'))
