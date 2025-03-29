import requests
import hashlib
import dadesServer
from dadesServer import User, Child, Tap

url = "http://127.0.0.1:5000/tapatapp/getUserByCredentials"

dades = {
    "username": "mare",
    "password": "12345",
    "email": "prova@gmail.com"
}

TOKEN_VALID = "secret123"
token = hashlib.sha256(TOKEN_VALID.encode()).hexdigest()

header = {
    "Authorization": f"Bearer {token}"
}

response = requests.post(url, json=dades, headers=header)

if response.status_code == 200:
    data = response.json()

    print(f"Login successful")
    print(f"User: {data['username']}, Email: {data['email']}")
else:
    print(f"Error: {response.status_code}, {response.json()}")