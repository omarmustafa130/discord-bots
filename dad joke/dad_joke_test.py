import requests
import json
url = 'https://icanhazdadjoke.com/'

def get_joke():
    response = requests.get(url=url, headers={'Accept': 'application/json'})
    joke = response.json()['joke']
    print(joke)

get_joke()