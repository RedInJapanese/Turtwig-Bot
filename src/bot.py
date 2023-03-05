from discord.ext import commands
import discord
import time
import random

BOT_TOKEN = 'MTA4MjE3MTIwMzExMzk5NjM1OA.GycSNW.OgoZxVPb7tXiSr7mxeTo8UuSZa7RPd14dpIJd4'
CHANNEL_ID = 1082185743306326106

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():

    print('Turtwig bot is operational.')

@bot.event
async def on_message(message):
    if(message.author == bot.user):
        return
    mes = ''
    rand = random.randrange(0, 3)
    if rand == 0: 
        mes = 'turtwig!'
    else: 
        mes = 'twig!'
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(mes)
    return
bot.run(BOT_TOKEN)