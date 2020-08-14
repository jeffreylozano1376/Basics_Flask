import requests

# Base URL
BASE = "http://127.0.0.1:5000/"

# Send 'get' request to the specified URL + parameter/s
response = requests.get(BASE + "helloworld/ken")
print(response.json())