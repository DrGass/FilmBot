import discord
from discord.ext import commands
from database import save, load

class PropositionListCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
# Logic about propositions

    @commands.command()
    async def padd(self, ctx: commands.Context):
        
        id = ctx.guild.id 

        data = load(id,['propositions','channel'])

        channel = data[1]
       
        print(data)

        if ctx.channel.id != channel:
            return

        propositions = data[0]

        print(data)

        if propositions == None:
            propositions = []
        
        print(propositions)

        filmToAdd = str(ctx.message.content[11:])
        finalString = ""

        for i in range(len(propositions)):
            finalString += str(i) + ": " + propositions[i] + "\n"

        # If no arguments were given
        if len(filmToAdd) == 0:
            await ctx.channel.send(f"Nie podano filmu,\n Aktualna lista propozycji:\n{finalString}")
        else:
            for film in propositions:
                if filmToAdd.lower() in str(film).lower():
                    await ctx.channel.send(f"Taki film już jest na liście")
                    return

            propositions.append(filmToAdd)
            finalString += str(len(propositions)) + ": " + filmToAdd + "\n"

            print (propositions)

            await ctx.channel.send(
                f"<@{ctx.message.author.id}>, dodano propozycję: {filmToAdd}, lista teraz prezentuje się tak: \n{finalString}"
            )
            save({"propositions":propositions})

        await ctx.message.delete()

    @commands.command()
    async def p(self, ctx: commands.Context):
        id = ctx.guild.id 

        print(id)
      
        data = await load(id,['propositions','channel'])

        print(data, type(data))

        channel = data[1]

        if ctx.channel.id != channel:
            return
        
        print('pp')

        propositions = data[0]

        if propositions == None:
            await ctx.channel.send(f"No films on the proposition list, add them using !padd film name")
        else:
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
    

async def setup(bot:commands.Bot):
    await bot.add_cog(PropositionListCog(bot))