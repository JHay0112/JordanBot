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

# -- Configuration --

bot = commands.Bot(command_prefix = "jbot ") # Create bot instance
key = open("key.txt", "r").readline() # Get key from text file
SHANNON = 190696762749616128 # Shannon's ID

# - Events -

# Run when bot is logged in
@bot.event
async def on_ready():

    print("Logged in!")

# On message process
@bot.event
async def on_message(ctx):

    global SHANNON

    # Add message reactions for images and embeds
    if ctx.attachments or ctx.embeds:
        await ctx.add_reaction("🔼")
        await ctx.add_reaction("🔽")

    await bot.process_commands(ctx)
    
    # Check if the message starts with jbot
    if ctx.content.startswith("jbot"):
        # If the user is shannon
        if ctx.author.id == SHANNON:
            await ctx.channel.send("Horatio")

# -- Main --

bot.load_extension("cogs") # Load the cogs
bot.run(key) # Run bot