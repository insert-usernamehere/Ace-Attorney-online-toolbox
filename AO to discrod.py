import discord
from discord.ext import commands
from time import sleep
import os
import datetime


if os.path.exists("logs/server.log"):
    Current_Date = datetime.datetime.today().strftime(" %d %m %Y %H %M")
    os.rename('logs/server.log','logs/old server log' + str(Current_Date) + '.log')
else:
    pass

client = commands.Bot(command_prefix='!')


keepLooping = False

@client.event
async def on_message(message):
    global keepLooping
    if message.content.startswith("!log"):
        keepLooping = True
        while keepLooping:
                    with open('logs/server.log') as f:
                            for line in f:
                                pass
                            last_line = line
                            m= open("logs/lastline.txt","r")
                            oldline =m.read()
                            m.close() 
                            m= open("logs/lastline.txt","w+")
                            m.write(last_line)
                            m.close()
                            if last_line == oldline:
                                pass
                            elif last_line !=oldline:
                                await message.channel.send(last_line)
    elif message.content.startswith("!stoplog"):
        keepLooping = False

    

    
client.run('botid')
