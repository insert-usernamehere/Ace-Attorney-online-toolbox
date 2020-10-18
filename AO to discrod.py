import discord
from discord.ext import commands
from time import sleep
import os

client = commands.Bot(command_prefix='!')


keepLooping = False

@client.event
async def on_message(message):
    global keepLooping
    if message.content.startswith("!log"):
        keepLooping = True
        while keepLooping:
                    with open('server.log') as f:
                            for line in f:
                                pass
                            last_line = line
                            m= open("lastline.txt","r")
                            oldline =m.read()
                            m.close() 
                            m= open("lastline.txt","w+")
                            m.write(last_line)
                            m.close()
                            if last_line == oldline:
                                pass
                            elif last_line !=oldline:
                                await message.channel.send(last_line)
    elif message.content.startswith("!stoplog"):
        keepLooping = False

    

    
client.run('botid')
