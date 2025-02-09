#https://zenquotes.io/api/random

import requests
import json

def getQuote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    author = json_data[0]['a']

    print(quote + ' -' + author)

getQuote()