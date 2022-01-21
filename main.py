import os
import discord
from request import *



client = discord.Client()

@client.event

async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$precioBTC'):
    precio = get_price('BTC')
    await message.channel.send(precio)
  elif message.content.startswith('$precioDOT'):
    precio = get_price('DOT')
    await message.channel.send(precio)
  elif message.content.startswith('$precioETH'):
    precio = get_price('ETH')
    await message.channel.send(precio)
  
client.run(os.getenv('TOKEN'))