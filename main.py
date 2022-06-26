from keep_alive import keep_alive
import discord
import time
from discord import DMChannel
from discord.ext import commands, tasks
import os
from discord import Intents
from discord import Embed

os.system('clear')

intents = Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="-", owner_id=716707479005823036, intents=intents)
token = '' # PUT YOUR BOT TOKEN HERE

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
  
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.author == message.author:
      channel = bot.get_channel(989610111632805999)
      chn = message.channel
      nwor = ['nig','n1g','wigg']
      kys = ['kys', 'kill yourself']
      mean = ['bitch', 'fag', 'stfu', 'shut the']
      nameo = message.author
      mess = message.content
      mes = mess.lower()
      emb = Embed(
        description = f'{nameo}: {mes}'
      )
      emb.set_footer(text=f'{chn} ({message.channel.id})')
      await channel.send(embed=emb)
      fluf = await bot.fetch_user('716707479005823036')
      if fluf is not None:
             if fluf.dm_channel is None:
                 await fluf.create_dm()
             if any(word in mes for word in nwor):
                 emb.title = "🔴 N-Word 🔴"
                 await DMChannel.send(fluf, embed=emb)
             elif any(word in mes for word in kys):
                 emb.title = "🔴 Someone said kys! 🔴"
                 await DMChannel.send(fluf, embed=emb)



@tasks.loop(seconds=40)
async def task():
    await bot.wait_until_ready()
    guild = bot.get_guild(921366728016011324)
    fluf = bot.get_user(716707479005823036) # me
    chn = bot.get_channel(990590309710823444)
    for member in guild.members: # checks every user from discord server
      if member.activity and member.activity.name:
        role = discord.utils.find(lambda r: r.name == 'Supporter', member.guild.roles)
        if member.activities and 'discord.gg/floofi' in member.activities[0].name:
                  print(f"{member} ✅")
                  if role in member.roles:
                      continue
                  else:
                      await member.add_roles(discord.Object(id=921720262217568268))
                      await chn.send(f'gave supporter role to {member}')
        elif member.activities and 'discord.gg/floofi' not in member.activities[0].name:
                  print(f"{member} ❌")
                  if role not in member.roles:
                      continue
                  else:
                      await member.remove_roles(discord.Object(id=921720262217568268))
                      await chn.send(f'removed supporter role from {member}')

keep_alive() # from another file called 'keep_alive'
task.start()
bot.run(token)
