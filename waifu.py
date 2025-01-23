import requests
import json

import discord
from discord.ext import commands

#https://docs.waifu.im/
async def fetch_waifu():
    """Fetch a random waifu image URL."""
    waifu_url = 'https://api.waifu.im/search'

    params = {
        'is_nsfw': False,
    }

    response = requests.get(waifu_url, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data['images'][0]['url']
    return "Failed to fetch waifu image."