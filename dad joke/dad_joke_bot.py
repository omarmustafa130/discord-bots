import discord
import requests
import json
from dotenv import load_dotenv
import os 

def get_joke():
    url = 'https://icanhazdadjoke.com/'
    response = requests.get(url=url, headers={'Accept': 'application/json'})
    joke = response.json()['joke']
    return joke

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    msg = message.content
    if client.user == message.author:
        return
    if msg.lower().startswith('$joke'):
        joke = get_joke()
        embed = discord.Embed(title='Dad Joke', description=joke, color=discord.Color.blue())
        await message.channel.send(embed=embed)

client.run(TOKEN)