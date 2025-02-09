
import discord
import random
import os
from dotenv import load_dotenv
import requests
import json


# Load environment variables from .env
load_dotenv()

# Get token from .env file
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
hello_list = ['$hi', '$hello', '$hey', '$hola']
hello_list_response = ['$hi there!', '$hello there!', '$hey!', '$hola amigo!']

def getQuote()->str: 
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    author = json_data[0]['a']

    msg = quote + ' -' + author
    return msg


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return
    if any(msg.lower().startswith(h) for h in hello_list):
        await message.channel.send(random.choice(hello_list_response))

    if (msg.lower().startswith('$encourage')):
        quote= getQuote()
        await message.channel.send(quote)

client.run(TOKEN)