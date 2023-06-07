import discord
from discord.ext import commands


class JoinReactionCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Hej {member.display_name}, nie zapominaj, pierdol się :)")


async def setup(bot: commands.Bot):
    await bot.add_cog(JoinReactionCog(bot))
