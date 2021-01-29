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

m= open("logs/lastline.txt","w+")
m.close()

client = commands.Bot(command_prefix='!')


keepLooping = False

@client.event
async def on_message(message):
    global keepLooping
    if message.content.startswith("!log"):
        keepLooping = True
        while keepLooping:
                        fileHandle = open ( 'logs/server.log',"r" )
                        lineList = fileHandle.readlines()
                        fileHandle.close()
                        print lineList
                        m= open("logs/lastline.txt","r")
                        oldline =m.read()
                        m.close() 
                        m= open("logs/lastline.txt","w+")
                        m.write(lastline)
                        m.close()
                        if lastline == oldline:
                                pass
                        elif lastline !=oldline:
                          await message.channel.send(last_ine)
    elif message.content.startswith("!stoplog"):
            keepLooping = False

    

    
client.run('botid')
