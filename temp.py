import requests

url = "https://ctech-wordle-server.herokuapp.com/"
command = {"command": "newid"}

words = requests.post(url = url, data = command)
print(words.text)