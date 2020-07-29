'''

    bot.py

    Author: Jordan Hay
    Date: 2020-07-29

    JordanBot: A Discord Bot

'''

# -- Import --

from discord.ext import commands # Import discord for running discord bot

# -- Configuration --

bot = commands.Bot(command_prefix = "jbot ") # Create bot instance
key = open("key.txt", "r").readline() # Get key from text file

# -- Functions --

# Run when bot is logged in
@bot.event
async def on_ready():
    print("Logged in!")

# Ping bot
@bot.command(name = "ping")
async def ping(ctx):
    await ctx.send(f"Latency: {round((bot.latency * 1000), 1)}ms")

# -- Main --

bot.run(key) # Run bot