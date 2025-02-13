import discord
import os
from dotenv import load_dotenv
import requests
import json

#load env variables
load_dotenv()

TOKEN = os.getenv("DISCOR_BOT_TOKEN")

print(TOKEN)

intents = discord.Intents.default()
intents.message_content=True

client=discord.Client(intents=intents)

def get_meme():
    url = 'https://meme-api.com/gimme'
    response = json.loads(requests.request("GET", url).text)
    meme_large = response['preview'][-1]
    subreddit = response['subreddit']

    return meme_large, subreddit