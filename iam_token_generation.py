import requests
def create_new_token():
    """Создание нового токена"""
    metadata_url = "http:"
    headers = {"Metadata-Flavor": "Google"}
    response = requests.get(metadata_url, headers=headers)
    token = response.json()["access_token"]
    return token
