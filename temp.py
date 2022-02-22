import requests

url = "https://ctech-wordle-server.herokuapp.com/"
command = {"command": "newid"}

response = requests.post(url = url, data = command)
print(response.text)