import discord
from discord.ext import commands
from database import save, load

class PropositionListCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
# Here will be logic about propositions

    # Rewrite adding, showing and removing propositions and add same solutions to film list (if someone won't be using app)

    @commands.command()
    async def padd(self, ctx: commands.Context):
      
        data = load([propositions,channel])

        channel = data[1]
        if ctx.channel.id != channel:
            return

        propositions = data[0]


        id = ctx.guild.id 

        filmToAdd = str(ctx.message.content[11:])
        finalString = ""

        for i in range(len(propositions)):
            finalString += str(i) + ": " + propositions[i] + "\n"

        # If no arguments were given
        if len(filmToAdd) == 0:
            await ctx.channel.send(f"Aktualna lista propozycji:\n{finalString}")
        else:
            for film in propositions:
                if filmToAdd.lower() in str(film).lower():
                    await ctx.channel.send(f"Taki film już jest na liście")
                    return

            propositions.append(filmToAdd)
            finalString += str(len(propositions)) + ": " + filmToAdd + "\n"

            await ctx.channel.send(
                f"<@{ctx.message.author.id}>, dodano propozycję: {filmToAdd}, lista teraz prezentuje się tak: \n{finalString}"
            )
            save({"propositions":propositions})

        await ctx.message.delete()

    @commands.command()
    async def p(self, ctx: commands.Context):
        data = load([propositions,channel])

        channel = data[1]
        if ctx.channel.id != channel:
            return
        
        propositions = data[0]
        
        finalString = ""

        for i in range(len(propositions)):
            finalString += str(i) + ": " + str(propositions) + "\n"

        await ctx.channel.send(f"Aktualna lista propozycji:\n{finalString}")

        await ctx.message.delete()

    @commands.command()
    async def pdel(self, ctx: commands.Context):
        data = load([propositions,channel])

        channel = data[1]
        if ctx.channel.id != channel:
            return
    
        propositions = data[0]
        
        # take firt word in film name and convert it to str
        filmToDel = str((ctx.message.content[11:].split())[0])

        for film in propositions:
            if filmToDel.lower() in str(film).lower():
                propositions.remove(film)
                await ctx.channel.send(
                    f"<@{ctx.message.author.id}>, usunięto pozycję: {film}"
                )
                save({"propositions":propositions})
                break

        await ctx.message.delete()
    

def setup(bot:commands.Bot):
    bot.add_cog(PropositionListCog(bot))