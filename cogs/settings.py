import discord
from discord.ext import commands


class SettingCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name = "Choose role")
    async def role(self, ctx:commands.Context):
        await ctx.send("template command")

    @commands.command(name = "Choose channel")
    async def channel(self, ctx:commands.Context):
        await ctx.send("template command")

    @commands.command(name = "Auto Setting")
    async def auto(self, ctx:commands.Context):
        await ctx.send("template command")

async def setup(bot:commands.Bot):
    await bot.add_cog(SettingCog(bot))