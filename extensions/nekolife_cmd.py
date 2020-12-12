from discord.ext import commands as cmds
import extensions.api.nekolife.nekolife as nekolife
import discord
class NekoLife_Cog(cmds.Cog):
    def __init__(self, bot: cmds.Bot):
        self.bot = bot

    @cmds.command()
    async def nekolife(self, ctx: cmds.Context, *args: tuple):
        if isinstance(ctx.channel, discord.channel.TextChannel):
            if ctx.channel.is_nsfw():
                endpoint = "".join([i for i in args[0]])
                nkl_result = nekolife.regenerate_embed(endpoint)
                await ctx.send(embed=nkl_result)
        else:
            await ctx.send("This isn't NSFW channel")

def setup(bot: cmds.Bot):
    bot.add_cog(NekoLife_Cog(bot))
    print("=> NekoLife library: LOADED")