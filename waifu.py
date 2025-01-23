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

async def fetch_waifu_image():
    """Fetch a random waifu image URL."""
    waifu_api_url = 'https://api.waifu.im/search'
    params = {'is_nsfw': False}  # Ensure the request is SFW

    try:
        response = requests.get(waifu_api_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()  # Parse the JSON response

        if 'images' in data and len(data['images']) > 0:
            return data['images'][0]['url']
        return "No images were found. Try again later."
    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching the waifu image: {e}"
