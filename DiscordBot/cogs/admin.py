import discord
from discord.ext import commands

class Admin_Commands(commands.Cog):
    #On cog startup
    def __init__(self, client):
       self.client = client
       print('Ext. \'admin\' loaded')

    #Quickly deletes messages
    @commands.command(aliases=['snap'])
    @commands.has_role("ADMIN")
    async def clear(self, ctx, arg=2):
        await ctx.channel.purge(limit = int(arg))
    
    #kick
    @commands.command()
    @commands.has_role("ADMIN")
    async def exile(self, ctx, member : discord.Member, *, reason = None):
        print(f'{member} kicked')
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been exiled')

    #Ban
    #member : discord.Member takes in an @mention and allows the member fuction to be used
    @commands.command()
    @commands.has_role("ADMIN")
    async def banish(self, ctx, member  : discord.Member, *, reason=None):
        print(f'{member} banned')
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banished to the shadow realm')


    #Unban
    #@client.command()
    #@commands.has_role("ADMIN")
    #async def unbanish(ctx, *, member):
    #	banned_users = await ctx.guid.bans()
def setup(client):
    client.add_cog(Admin_Commands(client))
