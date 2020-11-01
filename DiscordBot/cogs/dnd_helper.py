import discord
from discord.ext import commands, tasks
iniTracker = dict()

#Class for all misc dnd help 
class Dnd_Helper(commands.Cog):
    #On cog startup
    def __init__(self, client):
       self.client = client
       print('Ext. \'DnDHelper\' loaded')

    #Adds a dict for each player to the iniTracker
    @commands.command()
    async def addInit (self, ctx, roll = 1):
        temp = dict()
        temp['Name'] = str(ctx.message.author)
        temp['Value'] = roll
        flag = True
        for i in range (0, len(iniTracker)):
            if temp['Name'] == iniTracker[f'{i}']['Name']:
                iniTracker[f'{i}'] = temp
                flag = False
        if flag:
                iniTracker[f'{len(iniTracker)}'] = temp
        await ctx.send ('Initiative added for ' + ctx.message.author.mention)

    #Starts an initiative roll
    @commands.command()
    async def init(self, ctx):
        embed = discord.Embed(title='Initiative', colour=0xff133)
        #Smol sort 
        if len(iniTracker) > 1:
            for i in range (0, len(iniTracker)):
                for j in range(i+1, len(iniTracker)):
                    if iniTracker[f'{i}']['Value'] < iniTracker[f'{j}']['Value']:
                        temp = iniTracker[f'{i}']
                        iniTracker[f'{i}'] = iniTracker[f'{j}']
                        iniTracker[f'{j}'] = temp
        embedText = ''
        #Print everything as usual
        if len(iniTracker) >= 1:
            for i in range (0, len(iniTracker)):
                embedText = embedText + iniTracker[f'{i}']['Name'] +': '+ str(iniTracker[f'{i}']['Value'])  +'\n'
            embed.add_field(name = '\u200b', value = embedText, inline = False)
            await ctx.send(embed = embed)
        else:
            await ctx.send('Initiative Tracker is empty')

    #Removes all initiative
    @commands.command()
    async def voidInit(self, ctx):
        global iniTracker
        iniTracker = dict()
        await ctx.send('Initiative has been reset.')
def setup(client):
    client.add_cog(Dnd_Helper(client))
