import discord
from discord.ext import commands, tasks

class BotTasks(commands.Cog):

    #On cog startup
    def __init__(self, client):
       self.client = client
       print('Ext. \'tasks\' loaded')
    


def setup(client):
    client.add_cog(Item_Shop(client))
