import json
import requests

response =  requests.get('https://v2.jokeapi.dev/joke/Any').json()
print(response)