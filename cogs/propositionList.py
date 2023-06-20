import discord
from discord.ext import commands


class CogName(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
# Here will be logic about propositions

    # Rewrite adding, showing and removing propositions and add same solutions to film list (if someone won't be using app)

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
    

def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))