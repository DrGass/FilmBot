import discord
from discord.ext import commands
from database import save, load


class FilmListCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
    @commands.command()
    async def fadd(self, ctx: commands.Context):
      
        data = load([films,channel])

        channel = data[1]
        if ctx.channel.id != channel:
            return

        films = data[0]


        id = ctx.guild.id 

        filmToAdd = str(ctx.message.content[11:])
        finalString = ""

        for i in range(len(films)):
            finalString += str(i) + ": " + films[i] + "\n"

        # If no arguments were given
        if len(filmToAdd) == 0:
            await ctx.channel.send(f"Aktualna lista propozycji:\n{finalString}")
        else:
            for film in films:
                if filmToAdd.lower() in str(film).lower():
                    await ctx.channel.send(f"Taki film już jest na liście")
                    return

            films.append(filmToAdd)
            finalString += str(len(films)) + ": " + filmToAdd + "\n"

            await ctx.channel.send(
                f"<@{ctx.message.author.id}>, dodano propozycję: {filmToAdd}, lista teraz prezentuje się tak: \n{finalString}"
            )
            save({"films":films})

        await ctx.message.delete()

    @commands.command()
    async def f(self, ctx: commands.Context):
        data = load([films,channel])

        channel = data[1]
        if ctx.channel.id != channel:
            return
        
        films = data[0]
        
        finalString = ""

        for i in range(len(films)):
            finalString += str(i) + ": " + str(films) + "\n"

        await ctx.channel.send(f"Aktualna lista propozycji:\n{finalString}")

        await ctx.message.delete()

    @commands.command()
    async def fdel(self, ctx: commands.Context):
        data = load([films,channel])

        channel = data[1]
        if ctx.channel.id != channel:
            return
    
        films = data[0]
        
        # take firt word in film name and convert it to str
        filmToDel = str((ctx.message.content[11:].split())[0])

        for film in films:
            if filmToDel.lower() in str(film).lower():
                films.remove(film)
                await ctx.channel.send(
                    f"<@{ctx.message.author.id}>, usunięto pozycję: {film}"
                )
                save({"films":films})
                break

        await ctx.message.delete()

async def setup(bot:commands.Bot):
    await bot.add_cog(FilmListCog(bot))

