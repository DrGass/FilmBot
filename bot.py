# bot.py
import os
import sort
import shutil
import time

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

osList = os.listdir(".\Filmy")

myIntents = discord.Intents.default()
myIntents.messages=True
myIntents.message_content=True
myIntents.reactions=True
bot = discord.Client(intents=myIntents)

def saveToFile(fileName, file):
    f = open(f'data\{fileName}.txt','w', encoding="utf-8")
    f.write(file)
    f.close()

def readFromFile(fileName, file):
    f = open(f'data\{fileName}.txt','r', encoding="utf-8")
    file = f.read()
    f.close()
    return file

@bot.event
async def on_ready():
     print(f"We have logged in as {bot.user}")
    
        
@bot.event
async def on_message(message,):
    lastVoting = ""
    lastVotingMessage = ""
    winner = ""

    winner = readFromFile('winner',winner)
    lastVoting = readFromFile('lastVoting',lastVoting)
    lastVotingMessage = readFromFile('lastVotingMessage',lastVotingMessage)

    print(f'1: {winner} 2: {lastVoting} 3:{lastVotingMessage}')
    
# Creating reactions to !films message 
    user_message = str(message.content)
    filmList,filmCount = sort.main()
    emojis = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']


    if lastVoting == '1' and user_message.startswith('!film'):
        async for msg in message.channel.history(limit=100):
            if str(msg.id) == lastVotingMessage:
                await msg.reply(f'Głosowanie już trwa -> <@{message.author.id}> <-')
            else:
                lastVoting = '0'
                saveToFile('lastVoting',lastVoting)
        await message.delete()
        return

    if message.author == bot.user and user_message.startswith("<") and lastVoting == '0':
            # adding reactions
            for i in range(0,filmCount - 1):
                await message.add_reaction(emojis[i])
            
            # saving voting value
            lastVoting = '1'
            saveToFile('lastVoting',lastVoting)
            
            # saving last value 
            lastVotingMessage = str(message.id) 
            saveToFile('lastVotingMessage',lastVotingMessage)
            return
    
   
    
    if message.author == bot.user and user_message.startswith("Głosowanie już trwa"):
        time.sleep(5)
        await message.delete()
        return

# !film command for creating message with list of films 
    if user_message.startswith("!film") and lastVoting == '0':  
        await message.channel.send(f'<@&1097826568065265675> Zapraszam do głosowania, w dzisiejszym menu mamy: \n{filmList}')
        return

    if message.author == bot.user:
        return 
    
    if message.author.name == 'Dr Gass':
        if user_message.startswith("!delete"):
            arguments = user_message[7:].split()
            for film in osList:
                if arguments[0] in film.lower():
                    shutil.rmtree(f"D:\Pobrane\Filmy\{film}")
                    await message.channel.send(f'Usunięto film {film}')
                    return
                
    elif user_message.startswith("!delete") and message.author.name != 'Dr Gass':
        await message.channel.send(f'Nie masz uprawnień do usuwania, {message.author.name}')
        return

# Taking winner considering reactions or time (to add)
@bot.event
async def on_reaction_add(reaction, user):
    # print('hi')

    lastVoting = lastVotingMessage = ""
    lastVoting = readFromFile('lastVoting',lastVoting)
    lastVotingMessage = readFromFile('lastVotingMessage',lastVotingMessage)
    # print(reaction,type(reaction),str(reaction))

    if user == bot.user:
        return
    
    if str(reaction.message.id) == lastVotingMessage and reaction.count >= 2:

        winner = str(reaction)
        saveToFile('winner',winner)
        lastVoting = '0'
        saveToFile('lastVoting',lastVoting)
        
        # add creating winner message 
        await reaction.message.delete()

        numberDict = {
        "1" : ":one:",
        "2" : ":two:",
        "3" : ":three:",
        "4" : ":four:",
        "5" : ":five:",
        "6" : ":six:",
        "7" : ":seven:",
        "8" : ":eight:",
        "9" : ":nine:"
        }
        emojis = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
        filmList,filmCount = sort.main()
        winner = numberDict.get(f'{str(emojis.index(winner) + 1)}')

        # Crop Film out of list
        winnerLine = filmList[filmList.find(winner):]
        winnerLine = winnerLine[winnerLine.find(" "):]
        winnerLine = winnerLine[:winnerLine.find("\n")]

        await reaction.message.channel.send(f'Drodzy <@&1097826568065265675>! Wygrał film numer {winner} : {winnerLine}')
        return


bot.run(TOKEN)
