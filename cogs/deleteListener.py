import discord
from discord.ext import commands

# This file will be responsible for deleting messages that aren't supposed to be there. (Not sure if i'm gonna use it tho)

    # @commands.Cog.listener()
    # async def on_message(self, message: discord.Message):
    #     if message.channel.id not in self.acceptedChannels:
    #         return

    #     # print(self.dataDict, message.author, self.bot.user)
    #     if message.author == self.bot.user:
    #         # Voting message adding reactions
    #         if message.content.startswith("<@&"):
    #             for i in range(0, len(self.filmDict)):
    #                 await message.add_reaction(self.emojis[i])

    #             self.dataDict["lastVotingMessage"] = str(message.id)
    #             self.saveData()

    #         # Voting is running message
    #         elif self.messagesToDel in message.content.lower():
    #             await asyncio.sleep(5)
    #             await message.delete()

def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))