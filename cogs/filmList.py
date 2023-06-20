import discord
from discord.ext import commands
import json
import time
import sys
import asyncio
from database import save, load

sys.path.insert(0, "..\\Script")

from sortFilms import main as sort


class UpdateFilmListCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.dataDict = {}
        self.filmDict, self.filmList = sort()
        self.emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
        self.acceptedChannels = []
        self.messagesToDel = ["taki", "głosowanie", "usunięto", "dodano", "trwa"]
        self.pingRole = 0

    # What bot does at startup
    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"We have logged in as {self.bot.user} and loaded Dict: \n {self.dataDict} \n and propositions : \n {self.filmPropositions}"
        )

    @commands.command()
    async def film(self, ctx: commands.Context):
        if ctx.message.channel.id not in self.acceptedChannels:
            return

        if self.dataDict["lastVoting"] == "0":
            pingMsg = (
                f"<@&{self.pingRole}>" if self.pingRole is not None else "Moi drodzy,"
            )
            await ctx.channel.send(
                f"{pingMsg} zapraszam do głosowania, w dzisiejszym menu mamy: \n{self.filmList}"
            )
            self.dataDict["lastVoting"] = "1"
            self.saveData()

        else:
            print("hi")
            async for msg in ctx.channel.history(limit=10):
                print(msg.id, self.dataDict["lastVotingMessage"])
                if str(msg.id) == self.dataDict["lastVotingMessage"]:
                    await msg.reply(
                        f"Głosowanie już trwa -> <@{ctx.message.author.id}> <-"
                    )

                    await asyncio.sleep(3)
                    await ctx.message.delete()
                    return

        await ctx.message.delete()

    # Rewrite adding, showing and removing propositions and add same solutions to film list (if someone won't be using app, then it'll be more accesible c: )

    # Moved to propositionList.py

    # @commands.command()
    # async def padd(self, ctx: commands.Context):
    #     filmToAdd = str(ctx.message.content[11:])
    #     finalString = ""
    #     num = 1

    #     for film in self.filmPropositions:
    #         finalString += str(num) + ": " + film + "\n"
    #         num += 1

    #     # If no arguments were given
    #     if len(filmToAdd) == 0:
    #         await ctx.channel.send(f"Aktualna lista propozycji:\n{finalString}")
    #     else:
    #         for film in self.filmPropositions:
    #             if filmToAdd.lower() in str(film).lower():
    #                 await ctx.channel.send(f"Taki film już jest na liście")
    #                 return

    #         self.filmPropositions.append(filmToAdd)
    #         finalString += str(num) + ": " + filmToAdd + "\n"

    #         await ctx.channel.send(
    #             f"<@{ctx.message.author.id}>, dodano propozycję: {filmToAdd}, lista teraz prezentuje się tak: \n{finalString}"
    #         )
    #         self.saveFilms()

    #     await ctx.message.delete()

    # @commands.command()
    # async def p(self, ctx: commands.Context):
    #     finalString = ""
    #     num = 1
    #     for film in self.filmPropositions:
    #         finalString += str(num) + ": " + film + "\n"
    #         num += 1

    #     await ctx.channel.send(f"Aktualna lista propozycji:\n{finalString}")

    #     await ctx.message.delete()

    # @commands.command()
    # async def pdel(self, ctx: commands.Context):
    #     # take firt word in film name and convert it to str
    #     filmToDel = str((ctx.message.content[11:].split())[0])

    #     for film in self.filmPropositions:
    #         if filmToDel.lower() in str(film).lower():
    #             self.filmPropositions.remove(film)
    #             await ctx.channel.send(
    #                 f"<@{ctx.message.author.id}>, usunięto pozycję: {film}"
    #             )
    #             self.saveFilms()
    #             break

    #     await ctx.message.delete()
    
    # Moved to deleteListener.py

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


async def setup(bot):
    await bot.add_cog(UpdateFilmListCog(bot))
