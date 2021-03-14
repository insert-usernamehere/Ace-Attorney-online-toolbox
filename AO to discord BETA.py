import discord
from discord.ext import commands
from time import sleep
import os
import datetime


m= open("logs/lastline.txt","w+")
m.close()

client = commands.Bot(command_prefix='!')


keepLooping = False

@client.event
async def on_message(message):
    global keepLooping
    if message.content.startswith("!log"):
        await message.channel.send("logging started")
        keepLooping = True
        while keepLooping:
                        with open("logs/server.log") as f:
                            lines = f.readlines()
                            lastline = lines[-1]
                        m= open("logs/lastline.txt","r")
                        oldline =m.read()
                        m.close() 
                        m= open("logs/lastline.txt","w+")
                        m.write(lastline)
                        m.close()
                        if lastline == oldline:
                                pass
                        elif lastline !=oldline:
                          await message.channel.send(lastline)
                          await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="logging"))
    elif message.content.startswith("!stoplog"):
            await message.channel.send("stopped logging (this may take a couple of seconds)")
            keepLooping = False

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="logging"))
    

    
client.run('\botid')
