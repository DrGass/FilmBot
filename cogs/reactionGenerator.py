import discord
from discord.ext import commands
import sys
import json
from sortFilms import main as sort
from database import save, load

sys.path.insert(0, "..\\Script")


class ReactionGeneratorCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
    
    # Most probably finishied, needs to be checked

    @commands.Cog.listener()
    async def on_reaction_add(
        self, reaction: discord.Reaction, user: discord.Member | discord.User
    ):
        id = reaction.guild.id

        data = load(id,[winner,lastVotingMessage,role,acceptedChannel,lastVoting])

        self.filmDict, self.filmList = sort(id)
        winner = data[0]
        lastVotingMessage = data[1] 
        role = data[2]
        acceptedChannel = data[3]
        lastVoting = data[4]
        amountOfMembers = reaction.guild.roles.cache.get(id)
        amountOfMembers = amountOfMembers.memebers.size

        if (
            user == self.bot.user
            or reaction.message.id != lastVotingMessage
            or reaction.count < amountOfMembers // 2
            or reaction.channel != acceptedChannel
        ):
            return
    
        winner = str(reaction)
        lastVoting = 0 
        save(id,lastVoting)

        await reaction.message.delete()

        swapped_dict = {v: k for k, v in self.filmDict.items()}
        winning_number = str(self.emojis.index(str(reaction)) + 1)
        winner = swapped_dict[winning_number]

        # voting time is used to mark time when voting started
        # Add ending voting after certain time? maybe

        votingTime = str(
            discord.utils.snowflake_time(lastVotingMessage)
        )
        votingTime = votingTime[: (votingTime.find(":") - 2)]

        await reaction.message.channel.send(
            f"{role}! W głosowaniu z \
                {str(votingTime)} wygrał film numer {winning_number} : {winner}"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(ReactionGeneratorCog(bot))
