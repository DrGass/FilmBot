import discord
from discord.ext import commands
import json
import time
import sys
import asyncio

sys.path.insert(0, "..\\Script")

from sortFilms import main as sort


class UpdateFilmListCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.dataDict = {}
        self.filmDict, self.filmList = sort()
        self.emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
        self.acceptedChannels = [1097826304797188177, 468600962538405888]
        self.filmPropositions = []
        self.filmsPath = ".\data\\films.json"
        self.dataPath = ".\data\data.json"
        self.messagesToDel = ["taki", "głosowanie", "usunięto", "dodano"]

    def saveFilms(self):
        with open(self.filmsPath, "w") as fp:
            json.dump(self.filmPropositions, fp)

    def loadFilms(self):
        with open(self.filmsPath, "rb") as fp:
            self.filmPropositions = json.load(fp)

    def loadData(self):
        with open(self.dataPath, "r") as openFile:
            self.dataDict = json.load(openFile)

    def saveData(self):
        with open(self.dataPath, "w") as saveFile:
            json.dump(self.dataDict, saveFile)

    # Starting bot, loading data
    @commands.Cog.listener()
    async def on_ready(self):
        self.loadData()
        self.loadFilms()
        print(
            f"We have logged in as {self.bot.user} and loaded Dict: \n {self.dataDict} \n and propositions : \n {self.filmPropositions}"
        )

    @commands.command()
    async def film(self, ctx: commands.Context):
        if ctx.message.channel.id not in self.acceptedChannels:
            return

        if self.dataDict["lastVoting"] == "0":
            await ctx.channel.send(
                f"<@&1097826568065265675> Zapraszam do głosowania, w dzisiejszym menu mamy: \n{self.filmList}"
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

            self.dataDict["lastVoting"] = "0"
            self.saveData()
            await ctx.channel.send(
                f"<@&1097826568065265675> Zapraszam do głosowania, w dzisiejszym menu mamy: \n{self.filmList}"
            )

        await ctx.message.delete()

    @commands.command()
    async def proposeadd(self, ctx: commands.Context):
        filmToAdd = str(ctx.message.content[11:])
        finalString = ""
        num = 1

        for film in self.filmPropositions:
            finalString += str(num) + ": " + film + "\n"
            num += 1

        # If no arguments were given
        if len(filmToAdd) == 0:
            await ctx.channel.send(f"Aktualna lista propozycji:\n{finalString}")
        else:
            for film in self.filmPropositions:
                if filmToAdd.lower() in str(film).lower():
                    await ctx.channel.send(f"Taki film już jest na liście")
                    return

            self.filmPropositions.append(filmToAdd)
            finalString += str(num) + ": " + filmToAdd + "\n"

            await ctx.channel.send(
                f"<@{ctx.message.author.id}>, dodano propozycję: {filmToAdd}, lista teraz prezentuje się tak: \n{finalString}"
            )
            self.saveFilms()

        await ctx.message.delete()

    @commands.command()
    async def propose(self, ctx: commands.Context):
        finalString = ""
        num = 1
        for film in self.filmPropositions:
            finalString += str(num) + ": " + film + "\n"
            num += 1

        await ctx.channel.send(f"Aktualna lista propozycji:\n{finalString}")

        await ctx.message.delete()

    @commands.command()
    async def proposedel(self, ctx: commands.Context):
        # take firt word in film name and convert it to str
        filmToDel = str((ctx.message.content[11:].split())[0])

        for film in self.filmPropositions:
            if filmToDel.lower() in str(film).lower():
                self.filmPropositions.remove(film)
                await ctx.channel.send(
                    f"<@{ctx.message.author.id}>, usunięto pozycję: {film}"
                )
                self.saveFilms()
                break

        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.channel.id not in self.acceptedChannels:
            return

        # print(self.dataDict, message.author, self.bot.user)
        if message.author == self.bot.user:
            # Voting message adding reactions
            if message.content.startswith("<@&"):
                for i in range(0, len(self.filmDict)):
                    await message.add_reaction(self.emojis[i])

                self.dataDict["lastVotingMessage"] = str(message.id)
                self.saveData()

            # Voting is running message
            elif self.messagesToDel in message.content.lower():
                await asyncio.sleep(5)
                await message.delete()


async def setup(bot):
    await bot.add_cog(UpdateFilmListCog(bot))
