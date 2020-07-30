'''

    bot.py

    Author: Jordan Hay
    Date: 2020-07-29

    JordanBot: A Discord Bot

'''

# -- Import --

from discord.ext import commands # Import discord commands
import discord # Import the actualy discord
import random # Used to randomly select things
import time
import subprocess
import sys

# -- Configuration --

bot = commands.Bot(command_prefix = "jbot ") # Create bot instance
key = open("key.txt", "r").readline() # Get key from text file
admins = [306566109040082944] # User ID of admins

# -- Functions --

# Add reactions for users to vote on a message
async def vote_on(message):

    await message.add_reaction("🔼")
    await message.add_reaction("🔽")

# - Events -

# Run when bot is logged in
@bot.event
async def on_ready():

    print("Logged in!")

# On message process
@bot.event
async def on_message(message):

    # Add message reactions for images and embeds
    if message.attachments or message.embeds:
        vote_on(message)

    await bot.process_commands(message)

# - Commands -

# Ping bot
@bot.command(name = "ping")
async def ping(message):
    await message.send(f"Latency: {round((bot.latency * 1000), 1)}ms")

# Vote on previous message in channel
@bot.command(name = "vote")
async def vote(message):

    # get the previous message
    prev_message = await message.channel.history(limit = 2).flatten()
    prev_message = prev_message[-1]

    # delete the message that called this command
    await message.message.delete()

    # Add reactions
    await vote_on(prev_message)

# Rebuild and reload code
@bot.command(name = "reload")
async def reload(message):

    if message.author.id in admins:

        await message.send("Getting new code from Github and reloading")

        subprocess.call("./reload.sh")

        sys.exit()

    else:
        await message.send(f"{message.author.name} is not an admin!")

# -- Main --

bot.run(key) # Run bot