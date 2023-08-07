import discord
from discord.ext import commands
from database import save, load
import asyncio

class DeleteListenerCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.messagesToDel = ["taki", "głosowanie", "usunięto", "dodano", "trwa"]

    # This file is responsible for deleting messages that aren't supposed to be there. (Not sure if i'm gonna use it tho)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):

        data = load([channel])
        channel = data[0]

        if message.channel.id != channel or message.author != self.bot.user:
            return

        # Voting is running message
        if message.content.lower() in self.messagesToDel:
            await asyncio.sleep(4)
            await message.delete()

async def setup(bot:commands.Bot):
    await bot.add_cog(DeleteListenerCog(bot))

