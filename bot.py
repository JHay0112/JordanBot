'''

    bot.py

    Author: Jordan Hay
    Date: 2020-07-29

    JordanBot: A Discord Bot

'''

# -- Import --

import discord # Import discord for running discord bot

# -- Configuration --

bot = discord.Client() # Create bot instance
key = open("key.txt", "r").readline() # Get key from text file

# -- Functions --

# Run when bot is logged in
@bot.event
async def on_ready():
    print("Logged in!")

# -- Main --

bot.run(key) # Run bot