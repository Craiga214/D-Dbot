import discord
from discord.ext import commands
import os 
from os import path
import difflib 
import sys
print (os.listdir())
sys.path.append('.\\cogs\\Processes')
from item_gather import *
from coin_gather import *
itemDict = itemGather()


class Item_Shop(commands.Cog):

    #On cog startup
    def __init__(self, client):
       self.client = client
       print('Ext. \'item_shop\' loaded')
    @commands.command()
    async def shop(self, ctx):
        ctx.send("The shop is fully stocked.")
    
    @commands.command()
    async def item(self, ctx, *, item):
        #change Spelling to be correct for the item
        item = difflib.get_close_matches(item, itemDict.keys())
        #Create embed object
        embed = discord.Embed(title=itemDict[item[0]]['Name'], colour=0xff133)

        #Display critical info
        textName = 'Description'
        embed.add_field(name='Info\n', value = '**Source: **' + itemDict[item[0]]['Source'] \
                            +'\n**Rarity: **'+ itemDict[item[0]]['Rarity'] +'\n**Type: **'+ itemDict[item[0]]['Type'] \
                            +'\n**Attunement: **'+ itemDict[item[0]]['Attunement'] +'\n**Properties: **'+ itemDict[item[0]]['Properties'] \
                            +'\n**Weight: **'+ itemDict[item[0]]['Weight'] +'\n**Value: **'+ itemDict[item[0]]['Value'] \
                            +'\n\n**Description: **' , inline=False)
        #Display discription in footer
        embed.set_footer(text = itemDict[item[0]][textName][:2048])

        #Print the embed to discord
        await ctx.send(embed=embed)
    
    #Voiding an inventory
    @commands.command()
    async def voidInv(self, ctx, character = 1):
        #I didn't really need a function here but whatever
        voidFile(f'{ctx.message.author.id}_{str(character)}_inventory.csv')
        voidFile(f'{ctx.message.author.id}_{str(character)}_bank.csv')
        await ctx.send("https://tenor.com/view/dont-need-you-angry-throw-trash-garbage-gif-15769455")

    #Adding to player inventory
    @commands.command()
    @commands.has_role("Dungeon Master")
    async def give(self, ctx, member : discord.Member, character = 1, qty = 1, *, item):
        item = difflib.get_close_matches(item, itemDict.keys())
        #Check if the file is there
        if path.isfile(f'.\\cogs\\Processes\\item_storage\\{member.id}_{str(character)}_inventory.csv'):
            #gather items from inventory
            invDict = invGather(f'{member.id}_{str(character)}_inventory.csv')
            invDict = addItem(invDict, qty, item[0])
            toFile(invDict, f'{member.id}_{str(character)}_inventory.csv')
            #Output text
            await ctx.send('You have given '+member.mention+f' ({qty})'+item[0])
        else:
            await ctx.send('This person does not have an inventory. Ask them to create one with <+inv>')
    #Adding to player inventory (Homebrew)
    @commands.command()
    @commands.has_role("Dungeon Master")
    async def giveUnknown(self, ctx, member : discord.Member, character = 1, qty = 1, *, item):
        #Check if the file is there
        if path.isfile(f'.\\cogs\\Processes\\item_storage\\{member.id}_{str(character)}_inventory.csv'):
            #gather items from inventory
            invDict = invGather(f'{member.id}_{str(character)}_inventory.csv')
            invDict = addItem(invDict, qty, item)
            toFile(invDict, f'{member.id}_{str(character)}_inventory.csv')
            #Output text
            await ctx.send('You have given '+member.mention+f' ({qty})'+item)
        else:
            await ctx.send('This person does not have an inventory. Ask them to create one with <+inv>')

    #Player dropping items
    @commands.command()
    async def drop(self, ctx, character, qty, *, item):
        qty = int(qty)
        if qty >= 0:
            item = difflib.get_close_matches(item, itemDict.keys())
            if path.isfile(f'.\\cogs\\Processes\\item_storage\\{ctx.message.author.id}_{str(character)}_inventory.csv'):
                invDict = invGather(f'{ctx.message.author.id}_{str(character)}_inventory.csv')
                invDict = addItem(invDict, -(qty), item[0])
                toFile(invDict, f'{ctx.message.author.id}_{str(character)}_inventory.csv')
                await ctx.send(f'You have dropped ({qty}) '+item[0])
            else:
                await ctx.send('You do not have an inventory. Create one with <+inv>')
        else:
            await ctx.send('The items you drop must be > 0.')

    #Getting player inventory and getting rid of all qty 0 items
    @commands.command()
    async def inv(self, ctx, character=1):
        if path.isfile(f'.\\cogs\\Processes\\item_storage\\{ctx.message.author.id}_{str(character)}_inventory.csv') and path.isfile(f'.\\cogs\\Processes\\item_storage\\{ctx.message.author.id}_{str(character)}_bank.csv'):
            #gather the items from the given player's inventory
            invDict = invGather(f'{ctx.message.author.id}_{str(character)}_inventory.csv')
            #gather the money from the given player's bank
            coinDict = coinGather(f'{ctx.message.author.id}_{str(character)}_bank.csv')

            #embed the items
            embed = discord.Embed(title=str(ctx.message.author)+'\'s Inventory', colour=0x001e69)
            embedString = ''
            max = len(invDict)
            if max > 0:
                for i in range (0, max):
                    #Check the new length to make sure we arent going out of index and print to file
                    if i == max:
                        toFile(invDict, f'{ctx.message.author.id}_{str(character)}_inventory.csv')
                        break
                    #Removing an item if qty is 0
                    if invDict[f'{i}']['Qty'] == '0':
                        invDict = removeItem(invDict, i)
                        max = max - 1
                    #Check the new length to make sure we arent going out of index and print to file
                    if i == max:
                        toFile(invDict, f'{ctx.message.author.id}_{str(character)}_inventory.csv')
                        break
                    embedString = embedString + invDict[f'{i}']['Qty'] +' '+ invDict[f'{i}']['Name']+'\n'
                
                #Creating string for coins
                coinString = '**CP**: ' + coinDict['cp'] + '\n'  + '**SP**: ' + coinDict['sp']+'\n'+\
                '**GP**: '+ coinDict['gp'] +'\n'+ '**PP**: '+ coinDict['pp']
                
                

                #Add the embed field to the embed using the string we made
                if embedString != '':   
                    embed.add_field(name = 'Packpack', value = embedString, inline = False)
                embed.add_field(name = 'Coin Pouch', value = coinString, inline = False)
                #Print the embed to discord
                await ctx.send(embed=embed)
            else:
                #If inventory is empty, just print the coins.
                embedString = '**CP**: ' + coinDict['cp'] + '\n'  + '**SP**: ' + coinDict['sp']+'\n'+\
                '**GP**: '+ coinDict['gp'] +'\n'+ '**PP**: '+ coinDict['pp']
                embed.add_field(name = 'Coin Purse', value = embedString, inline = False)
                await ctx.send(embed=embed)
                await ctx.send('Inventory is empty :cry:')
        else:
            #Create new files if the others do not exist. Since they are created together, everything else should work fine.
            with open(f'.\\cogs\\Processes\\item_storage\\{ctx.message.author.id}_{str(character)}_inventory.csv', 'w') as file:
                file.write('Index&Name&Qty')
                file.flush()
            with open(f'.\\cogs\\Processes\\item_storage\\{ctx.message.author.id}_{str(character)}_bank.csv', 'w') as file:
                file.write('cp&sp&gp&pp\n0&0&0&0')
                file.flush()
            await ctx.send('Inventory created, call again to see it.')

    #Spend command to take money
    @commands.command()
    async def spend(self, ctx, character=1, cp = 0, sp = 0, gp = 0, pp = 0):
        if cp < 0 or sp < 0 or gp < 0 or pp < 0:
            await ctx.send('Please enter a value greater than 0')
            return
        coinDict = coinGather(f'{ctx.message.author.id}_{str(character)}_bank.csv')
        #Subtract all coins
        coinDict['cp'] = str(int(coinDict['cp']) - cp)
        coinDict['sp'] = str(int(coinDict['sp']) - sp)
        coinDict['gp'] = str(int(coinDict['gp']) - gp)
        coinDict['pp'] = str(int(coinDict['pp']) - pp)
        coinToFile(f'{ctx.message.author.id}_{str(character)}_bank.csv', coinDict)
        await ctx.send('Money well spent')
        return
    #Earn command to get money
    @commands.command()
    @commands.has_role("Dungeon Master")
    async def deposit(self, ctx, member : discord.Member, character=1, cp = 0, sp = 0, gp = 0, pp = 0):
        coinDict = coinGather(f'{member.id}_{str(character)}_bank.csv')
        #Subtract all coins
        coinDict['cp'] = str(int(coinDict['cp']) + cp)
        coinDict['sp'] = str(int(coinDict['sp']) + sp)
        coinDict['gp'] = str(int(coinDict['gp']) + gp)
        coinDict['pp'] = str(int(coinDict['pp']) + pp)
        coinToFile(f'{member.id}_{str(character)}_bank.csv', coinDict)
        #Output success message
        await ctx.send('Coins deposited')
        return

def setup(client):
    client.add_cog(Item_Shop(client))