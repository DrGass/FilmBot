import discord
from discord.ext import commands


class dbSetting(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    # Setting channel and stuff



def setup(bot:commands.Bot):
    bot.add_cog(dbSetting(bot))