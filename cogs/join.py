import discord
from discord.ext import commands
import psycopg2
from dbconfig import config

class JoinReactionCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    # po dołączeniu do serwera utworzyć nową pozycję w bazie danych, pod warunkiem, że nie istnieje (w wypadku ponownego dołączenia do serwera)
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """ Save all the data to database """
        conn = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            
            # create a cursor
            cur = conn.cursor()

            cur.execute(f'INSERT INTO guilds(id,name) VALUES({guild.id,str(guild.name)})')            
            conn.commit()

        # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

async def setup(bot: commands.Bot):
    await bot.add_cog(JoinReactionCog(bot))
