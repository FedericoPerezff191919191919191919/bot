import os
import discord
from discord.ext import commands

# Usamos intents para poder leer mensajes
intents = discord.Intents.default()
intents.message_content = True

# Prefijo de comandos
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'🤖 Bot conectado como {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Token desde variable de entorno
bot.run(os.getenv('TOKEN'))
