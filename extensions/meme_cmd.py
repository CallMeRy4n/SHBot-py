import discord
from discord.ext import commands as cmds
from discord.ext.commands.core import Group

class Meme(cmds.Cog):
    meme = Group(name="MEME", invoke_without_command=True)
    def __init__(self, bot: cmds.Bot):
        self.bot = bot

    @meme.command()
    def ok(self):
        pass
    
    @meme.command()
    def woman(self):
        pass

def setup(bot: cmds.Bot):
    bot.add_cog(Meme(bot))
    print("=> Meme library: LOADED")