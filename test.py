import requests

BASE = "http://127.0.0.1:5000/" #local host address

response = requests.get(BASE+"helloworld")
print(response.json())