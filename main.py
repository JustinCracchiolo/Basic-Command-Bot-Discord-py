import discord

import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
   return
  if message.content.startswith('!info'):
    await message.channel.send("GDSC at St Johns University is a student run organization in association with Google")
  elif message.content.startswith('!commands'):
    await message.channel.send('!info, !drive, !schedule, !contacts')
  elif message.content.startswith('!drive'):
    await message.channel.send('url: https://drive.google.com/drive/folders/1fn2JlU4NRnPg4xhIr6szRlkG1A1RZur2?usp=drive_link')
  elif message.content.startswith('!schedule'):
    await message.channel.send('Schedule will be up soon')
  elif message.content.startswith('!contacts'):
    await message.channel.send('Email: justincracchiolo@gmail.com')



#run
client.run(os.environ['TOKEN'])

  