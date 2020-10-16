import discord
from discord.ext import commands
from time import sleep


bot = commands.Bot(command_prefix='!')


@bot.command()
async def log(ctx):
    with open('server.log') as f:
        for line in f:
            pass
    last_line = line
    sleep (2)
    await ctx.send(last_line)
    sleep (2)
        
    
bot.run('bot-id')
