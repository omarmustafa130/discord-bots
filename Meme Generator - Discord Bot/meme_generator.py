import discord
import os
from dotenv import load_dotenv
import requests
import json


def get_meme():
    url = 'https://meme-api.com/gimme'
    response = json.loads(requests.request("GET", url).text)
    meme_large = response['preview'][-1]
    subreddit = response['subreddit']

    return meme_large, subreddit


#load env variables
load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content=True

client=discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    msg=message.content
    if client.user == message.author:
        return
    if msg.lower().startswith('$meme'):
        meme, subreddit = get_meme()
        embed = discord.Embed(title='Meme', description=f'From r/{subreddit}', color=discord.Color.blue())
        embed.set_image(url=meme)
        await message.channel.send(embed=embed)

client.run(TOKEN)
