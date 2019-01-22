import json
from pathlib import Path


def create_config(username: str, api_key: str):
    """
    Creates the configuration the Kaggle CLI needs, useful when trying to download a dataset from a Notebook
    :param username: Kaggle username
    :param api_key: A user generated API Key
    """
    config = {
        'username': username,
        'key': api_key
    }

    path = Path('~/.kaggle').expanduser()
    if not path.exists():
        path.mkdir()

    filename = path / 'kaggle.json'
    with filename.open('w') as file:
        json.dump(config, file)
    filename.chmod(0o600)
