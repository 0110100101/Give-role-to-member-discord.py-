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
bot = commands.Bot(command_prefix="-", owner_id=716707479005823036, intents=intents) # change owner id 
token = '' # PUT YOUR BOT TOKEN HERE

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


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
