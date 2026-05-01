import discord
from discord.ext import commands, tasks
import logging
from dotenv import load_dotenv
import os
import datetime
from datetime import datetime
import webserver
import requests


current_time = datetime.now() 
formatted_time = current_time.strftime("%H:%M:%S")

# Download the full word list
url = "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"
response = requests.get(url)

print(response)
# Split into words, strip any whitespace just in case, and filter 5-letter words
wordle_words = [word.lower().strip() for word in response.text.split("\n") if len(word.strip()) == 5]

print(wordle_words[:10])  # see the first 10 words

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

CHANNEL_ID = 1484739321121734666

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "time" in message.content.lower():
        await message.channel.send(f"{message.author.mention} the time is: {formatted_time}. Let's Go!  🕗")

    await bot.process_commands(message)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    send_time.start()  # starts the loop

webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
