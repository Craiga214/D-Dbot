import discord
import time
import datetime
from discord.ext import commands, tasks
import asyncio
import os
from dotenv import load_dotenv

#TOKEN = Token goes here
client = commands.Bot(command_prefix  = '>')

alarm_time = '18:03'#24hrs

#All events and commands here will only be used for startup and basic actions
#Events-----------------------------------------------------------------
#When the bot starts up, this runs once
@client.event 
async def on_ready():
	channel = client.get_channel(729023862615834644)
	await channel.send('Booted and ready!')
	await channel.send('https://tenor.com/view/stitch-roger-gif-8331093')
	await channel.send('All extensions loaded.')
	print('Bot is ready')

#When a member joins
@client.event 
async def on_member_join(member):
	print(f'{member} has joined a server')
	channel = client.get_channel(626162254244610049)
	await channel.send('Welcome to the uwindsor tabletop community ' + ('<@'+ str(member.id) +'>') +'!')
	await channel.send('Please nickname yourself so we know who you are')

#When a member leaves
@client.event
async def on_member_remove(member):
	print(f'{member} has been removed from the server.')

#Commands-----------------------------------------------------------------
#Just a ping check
@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! ({round(client.latency * 1000)}ms)')
	if (round(client.latency*1000) >= 100):
		await ctx.send('Ouchie, that is a bit high....')

#Use this as a basis, it checks who sent the message/command
#@client.command()
#async def name(ctx):
#	await ctx.send('Your name is ' + format(ctx.message.author.mention))

#Disconnects the bot for restart
@client.command()
@commands.has_role("DJ")
async def disconnect(ctx):
	channel = client.get_channel(729023862615834644)
	await channel.send('Disconnecting...')
	await channel.send('https://tenor.com/view/puppy-gif-5441491')
	await client.logout()

#Running extensions
@client.command()
async def open(ctx, extension):
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f'Opened {extension}')
@client.command()
async def close(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	await ctx.send(f'Closed {extension}')
@client.command()
async def restart(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f'Restarted {extension}')
#start all extensions
for filename in os.listdir('.\\cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')
#2020-07-06 18:22:52.605618

#async def checkReminders():
#	while not client.is_closed():
#		await asyncio.sleep(5)
#		current_time = str(datetime.datetime.now())
#		current_time = current_time.split(' ')
#		date = datetime.datetime.today().weekday()
#		
#		print(current_time[1])
#		print(date)

#client.loop.create_task(checkReminders())
client.run(TOKEN)
