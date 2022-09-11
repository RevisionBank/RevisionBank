import requests

response = requests.get("https://www.physicsandmathstutor.com/").text
print(response)