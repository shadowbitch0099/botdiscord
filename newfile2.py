import discord 

from discord.ext.commands import bot

from  discord.ext import commands

import time

import asyncio

bot = commands.Bot(command_prefix = '!')

@bot.event

async def on_ready():
	
      print ("Bot Is Online! And Ready To Spam")



@bot.command(pass_context=True)

async def spam(ctx):
	
      await bot.say("Salut !")
      time.sleep(2)
      await bot.say("Go spam !")
      for i in range (0,1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):

              await bot.say("H1cKByME")  
              await bot.say("H1cKByME")   
              await bot.say("H1cKByME")            
              await bot.say("H1cKByME")  
              await bot.say("H1cKByME")  
              await bot.say("H1cKByME")
              await bot.say("H1cKByME")
              await bot.say("H1cKByME")





bot.run("NTE5OTE2NDUyODA4MjI4ODY0.DumRhQ.WHpfYCh7jL86fLmbDbk0pNnO_p0")
