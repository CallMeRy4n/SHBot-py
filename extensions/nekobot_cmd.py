import discord
from discord.ext import commands as cmds
import extensions.api.nekobot.nekobot as nekobot

class NekoBot_Cogs(cmds.Cog):
    def __init__(self, bot: cmds.Bot):
        self.bot = bot

    @cmds.command()
    async def nekobot(self, ctx: cmds.Context, *args: tuple):
        if isinstance(ctx.channel, discord.channel.TextChannel):
            if ctx.channel.is_nsfw():
                endpoint = "".join([i for i in args[0]])
                nkb_result = nekobot.regenerate_embed(endpoint)
                await ctx.send(embed=nkb_result)
        else:
            await ctx.send("This isn't NSFW channel")
    
def setup(bot: cmds.Bot):
    bot.add_cog(NekoBot_Cogs(bot))
    print("=> NekoBot library: LOADED")