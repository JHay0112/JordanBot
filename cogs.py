'''

    cogs.py

    Author: Jordan Hay
    Date: 2020-08-03

    JordanBot Cogs

'''

# -- Import --

from discord.ext import commands # Import discord commands
import subprocess
import sys

# -- Cogs --

# Main command functions etc
class Main(commands.Cog):

    # Cog initialisation
    def __init__(self, bot):
        self.bot = bot

    # Ping bot
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Latency: {round((self.bot.latency * 1000), 1)}ms")

    # Vote on previous message in channel
    @commands.command()
    async def vote(self, ctx):

        # get the previous message
        prev_message = await ctx.channel.history(limit = 2).flatten()
        prev_message = prev_message[-1]

        # delete the message that called this command
        await ctx.message.delete()

        # Add reactions
        await prev_message.add_reaction("🔼")
        await prev_message.add_reaction("🔽")

    # Ask JordanBot to fix something
    @commands.command()
    async def fix(self, ctx, *, arg):

        await ctx.send(f"'{arg}' aye? If it ain't broke, don't fix it")

# Jordan only commands
class Jordan(commands.Cog):

    JORDAN = 306566109040082944 # ID of Jordan

    # Cog initialisation
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):

        # Only authorise Jordan
        if(ctx.author.id == self.JORDAN):
            return(True)
        else:
            return(False)

    # Rebuild and reload code
    @commands.command()
    async def reload(self, ctx):

        await ctx.send("JordanBot may go down temporarily")

        subprocess.call("./reload.sh")

        sys.exit()

    # Nuke a channel with the brazil flag
    @commands.command()
    async def nuke(self, ctx):

        await ctx.send("I apologise in advance for what I am about to do")

        async for message in ctx.channel.history():

            try:
                await message.add_reaction("🇧🇷")
            except:
                pass

# -- Setup --

def setup(bot):

    bot.add_cog(Main(bot)) # Load main cog
    bot.add_cog(Jordan(bot)) # Load Jordan cog