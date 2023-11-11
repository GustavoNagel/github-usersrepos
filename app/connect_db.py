from datetime import datetime, timedelta
from app.database import mongo


def save(user: str, repositories: list[dict]):
    """Saves repositories for a giver user, replacing older entry if it already exist."""
    mongo.db.repositories.find_one_and_update(
        {'user': user},
        {"$set": {'created_at': datetime.now(), 'repositories': repositories}},
        upsert=True,
    )


def get_old_entries(days: int):
    """Get entries based on number of days that they were created."""
    date_old = datetime.now() - timedelta(days=days)
    return mongo.db.repositories.find({'created_at': { '$lte': date_old }})
