from flask import Blueprint, current_app
from app.github_client import list_repositories
from app.connect_db import get_old_entries, save

cmd_bp = Blueprint('cmd', __name__)


@cmd_bp.cli.command('update_entries')
def update_entries():
    """Command to update old entries."""
    for entry in get_old_entries(days=3):
        repositories = list_repositories(entry['user'])
        save(entry['user'], repositories)
        current_app.logger.info('Database entry was updated for user %s', entry['user'])
