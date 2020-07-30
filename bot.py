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
async def vote_on(ctx):

    await ctx.add_reaction("🔼")
    await ctx.add_reaction("🔽")

# - Events -

# Run when bot is logged in
@bot.event
async def on_ready():

    print("Logged in!")

# On message process
@bot.event
async def on_message(ctx):

    # Add message reactions for images and embeds
    if ctx.attachments or ctx.embeds:
        vote_on(ctx)

    await bot.process_commands(ctx)

# - Commands -

# Ping bot
@bot.command()
async def ping(ctx):
    await ctx.send(f"Latency: {round((bot.latency * 1000), 1)}ms")

# Vote on previous message in channel
@bot.command()
async def vote(ctx):

    # get the previous message
    prev_message = await ctx.channel.history(limit = 2).flatten()
    prev_message = prev_message[-1]

    # delete the message that called this command
    await ctx.ctx.delete()

    # Add reactions
    await vote_on(prev_message)

# Rebuild and reload code
@bot.command()
async def reload(ctx):

    if ctx.author.id in admins:

        await ctx.send("JordanBot may go down temporarily")

        subprocess.call("./reload.sh")

        sys.exit()

    else:
        await ctx.send(f"{ctx.author.name} is not authorised to use this command")

# -- Main --

bot.run(key) # Run bot