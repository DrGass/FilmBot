import discord
from discord.ext import commands


class CogName(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name = "Choose role")
    async def  commandName(self, ctx:commands.Context):
        await ctx.send("template command")

    @commands.command(name = "Choose channel")
    async def  commandName(self, ctx:commands.Context):
        await ctx.send("template command")

    @commands.command(name = "Choose role")
    async def  commandName(self, ctx:commands.Context):
        await ctx.send("template command")

def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))