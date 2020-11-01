import discord
from discord.ext import commands
import difflib 
import os 
import sys
import random
from random import randint as rand
print (os.listdir())
sys.path.append('.\\cogs\\Processes')
uwuTarget= 0
from uwu import *
class Memes(commands.Cog):
    
    #On cog startup
    def __init__(self, client):
       self.client = client
       print('Ext. \'memes\' loaded')

    #Cursed repeat
    @commands.Cog.listener()
    async def on_message(self, message):
        if int(message.author.id) == uwuTarget:
            uwu = receive(str(message.content))
            channel = self.client.get_channel(message.channel.id)
            await channel.send(uwu)
    #Set target for repeat
    @commands.command()
    async def setTarget(self, ctx, member : discord.Member):
        global uwuTarget
        uwuTarget = int(member.id)
    #Set target for repeat
    @commands.command()
    async def delTarget(self, ctx):
        global uwuTarget
        uwuTarget = 0

    #Spams a given user
    @commands.command()
    @commands.has_role("DJ")
    async def annoy(self, ctx, member : discord.Member):
        for i in range (4):
            await ctx.send('Hey'+ '<@' + str(member.id)+'>'+'!')
        await ctx.send(f'{ctx.message.author} wants you')

    #My friend's code for UwU speech
    @commands.command()
    async def uwu(self, ctx, *, message):
        uwu = receive(message)
        await ctx.send(uwu)
    
    #Coin toss
    @commands.command()
    async def flip(self, ctx):
        import random
        num = random.randint(1,2)
        embed = discord.Embed(title='Coin Flip', colour=0xff133)
        if num == 1:
            embed.add_field(name = '\u200b', value = 'Heads', inline = False)
        if num == 2:
            embed.add_field(name = '\u200b', value = 'Tails', inline = False)
        await ctx.send(embed = embed)

    #Random 8Ball thing
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]

        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


def setup(client):
    client.add_cog(Memes(client))
