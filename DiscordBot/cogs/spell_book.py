import discord
from discord.ext import commands
import difflib 
import os 
import sys
print (os.listdir())
sys.path.append('.\\cogs\\Processes')
from spell_gather import *

spellDict = spellGather()

class Spell_Book(commands.Cog):

    #On cog startup
    def __init__(self, client):
       self.client = client
       print('Ext. \'spellbook\' loaded')
       
    #Print spells
    @commands.command()
    async def spell(self, ctx, *, spell):
        #change SPELLing to be correct
        spell = difflib.get_close_matches(spell, spellDict.keys())
        embed = discord.Embed(title=spellDict[spell[0]]['Name'], colour=0x50caff)
        
        #manually print out spell details
        embed.add_field(name='Info\n', value = '**Source: **' + spellDict[spell[0]]['Source'] \
                            +'\n**Level: **'+ spellDict[spell[0]]['Level'] +'\n**Casting Time: **'+ spellDict[spell[0]]['Casting Time'] \
                            +'\n**Duration: **'+ spellDict[spell[0]]['Duration'] +'\n**School: **'+ spellDict[spell[0]]['School'] \
                            +'\n**Range: **'+ spellDict[spell[0]]['Range'], inline=False)
        
        #This is needed for large text, each one increasing in size to fit larger spell descriptions
        textName = 'Description'
        embed.add_field(name = textName, value = spellDict[spell[0]][textName][:1024], inline=False)
        if len(spellDict[spell[0]][textName]) > 1024:
            embed.add_field(name = '\u200b', value = spellDict[spell[0]][textName][1024:2048], inline=False)
        if len(spellDict[spell[0]][textName]) > 2048:
            embed.add_field(name = '\u200b', value = spellDict[spell[0]][textName][2048:], inline=False)
        
        #This is just the final command to output the last cat'
        embed.add_field(name = 'Spell Increase', value = spellDict[spell[0]]['Spell Increase'][:1024], inline=False)    
        #Display the embeded message
        await ctx.send(embed=embed)
        
    #Test command
    @commands.command()
    async def speak(self, ctx, *, message):
        await ctx.send(f'{message}')
def setup(client):
    client.add_cog(Spell_Book(client))
