import os
import discord
from request import *
from replit import db


db["precioant"] = 0
client = discord.Client()

@client.event

async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$precioBTC'):
    precioant = float(db["precioant"])
    precio = float(get_price('BTC'))
    db["precioant"] = precio
    await message.channel.send(precio)
    print(precioant)
    if precioant == 0.0:
      return
    elif precioant  < precio:
      await message.channel.send("VAMOS A VIVIR")
    elif precioant > precio:
      await message.channel.send("VAMOS A MORIIIIR")
    elif precioant == precio:
      print(precio)
  elif message.content.startswith('$precioDOT'):
    precio = get_price('DOT')
    await message.channel.send(precio)
  elif message.content.startswith('$precioETH'):
    precio = get_price('ETH')
    await message.channel.send(precio)
  
client.run(os.getenv('TOKEN'))