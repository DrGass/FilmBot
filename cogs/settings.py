import discord
from discord.ext import commands


class SettingCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.role(name = "Choose role")
    async def  role(self, ctx:commands.Context):
        await ctx.send("template command")

    @commands.channel(name = "Choose channel")
    async def  channel(self, ctx:commands.Context):
        await ctx.send("template command")

    @commands.auto(name = "Auto Setting")
    async def  auto(self, ctx:commands.Context):
        await ctx.send("template command")

def setup(bot:commands.Bot):
    bot.add_cog(SettingCog(bot))