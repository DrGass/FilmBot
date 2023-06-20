import discord
from discord.ext import commands
import sys
import json
from sortFilms import main as sort

sys.path.insert(0, "..\\Script")


class ReactionGeneratorCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
        self.filmDict, self.filmList = sort()
        self.dataDict = {}
        self.acceptedChannels = [1097826304797188177, 468600962538405888]

    def loadData(self):
        with open(".\data\data.json", "r") as openFile:
            self.dataDict = json.load(openFile)

    def saveData(self):
        with open(".\data\data.json", "w") as saveFile:
            json.dump(self.dataDict, saveFile)

    
    # It probably needs to be rewritten 

    @commands.Cog.listener()
    async def on_reaction_add(
        self, reaction: discord.Reaction, user: discord.Member | discord.User
    ):
        if (
            user == self.bot.user
            or reaction.message.channel.id not in self.acceptedChannels
        ):
            return

        self.loadData()

        if (
            str(reaction.message.id) == self.dataDict["lastVotingMessage"]
            and reaction.count >= 2
        ):
            self.dataDict["winner"] = str(reaction)
            self.dataDict["lastVoting"] = "0"
            self.saveData()

            await reaction.message.delete()

            swapped_dict = {v: k for k, v in self.filmDict.items()}
            winning_number = str(self.emojis.index(str(reaction)) + 1)
            winner = swapped_dict[winning_number]

            votingTime = str(
                discord.utils.snowflake_time(int(self.dataDict["lastVotingMessage"]))
            )
            votingTime = votingTime[: (votingTime.find(":") - 2)]

            await reaction.message.channel.send(
                f"Drodzy <@&1097826568065265675>! W głosowaniu z {str(votingTime)} wygrał film numer {winning_number} : {winner}"
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(ReactionGeneratorCog(bot))
