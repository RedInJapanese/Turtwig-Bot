from discord.ext import commands
import discord
import time
import random

BOT_TOKEN = 

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
    if str(message.channel) == 'turtwig':
        channel = bot.get_channel(message.channel.id)
        await channel.send(mes)
    return
bot.run(BOT_TOKEN)