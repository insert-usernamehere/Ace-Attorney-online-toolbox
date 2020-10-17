import discord
from discord.ext import commands
from time import sleep


bot = commands.Bot(command_prefix='!')


@bot.command()
async def log(ctx):
    while True:
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
        else:
            await ctx.send(last_line)
            
        
    
bot.run('NzY2NzUyNDY0ODM2NzU1NDY3.X4n74Q.bFMVRsAjiB4TofJ5z02fYQy5zpw')
