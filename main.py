import os
import discord
from discord.ext import commands
import asyncio
import schedule
import time

from waifu import fetch_waifu

from dotenv import load_dotenv

load_dotenv()

# Get the bot token
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN is not set in the environment variables")

# Intents are required for the bot to receive certain events
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

# Initialize the bot
bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1332106969200328794

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    bot.loop.create_task(schedule_messages())

async def send_daily_message():
    """Send a daily message to a specific channel."""
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        print(f"Sending message to {channel}")
        waifu_url = await fetch_waifu()
        await channel.send(waifu_url)
    else:
        print("Target channel not found.")

def schedule_tasks():
    """Schedule tasks."""
    # Schedule a message at 9:00 AM
    schedule.every().day.at("09:00").do(
        lambda: asyncio.run_coroutine_threadsafe(send_daily_message(), bot.loop)
    )
    # Schedule a message at 3:50 PM
    schedule.every().day.at("15:50").do(
        lambda: asyncio.run_coroutine_threadsafe(send_daily_message(), bot.loop)
    )

async def schedule_messages():
    """Run the scheduled tasks in an asynchronous loop."""
    schedule_tasks()
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)  # Wait for 1 second between checks


# Run the bot (replace YOUR_TOKEN_HERE with your bot's token)
bot.run(TOKEN)
