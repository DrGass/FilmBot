# bot.py rewritten
# reading stuff
import os
from dotenv import load_dotenv

# async
import asyncio

# discord
import discord
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

myIntents = discord.Intents.default()
myIntents.messages = True
myIntents.message_content = True
myIntents.reactions = True
myIntents.guilds = True

bot = commands.Bot(command_prefix="!", intents=myIntents, help_command=None)


async def loadCogs():
    for filename in os.listdir(".\cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    await loadCogs()
    await bot.start(TOKEN)


asyncio.run(main())
