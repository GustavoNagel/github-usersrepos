"""Github client."""

import requests


DESIRED_KEYS = ('name', 'html_url', 'description', 'language')

def list_repositories(username: str):
    """List 5 respositories from a given username."""
    response = requests.get(url=f'https://api.github.com/users/{username}/repos', params={'per_page': 5})
    response.raise_for_status()
    return [{key: repo[key] for key in DESIRED_KEYS} for repo in response.json()]
