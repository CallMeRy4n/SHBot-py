import discord
from discord.ext import commands as cmds

class MainBot(cmds.Cog):
    def __init__(self, bot: cmds.Bot):
        self.bot = bot

    @cmds.command()
    async def setnsfw(self, ctx: cmds.Context, *args: tuple):
        if isinstance(ctx.channel, discord.channel.TextChannel):
            if ctx.channel.is_nsfw():
                await ctx.send("This already a NSFW channel")
            else:
                if not args or args == ():
                    await ctx.channel.edit(nsfw=True)
                    await ctx.send("<#{}> now is NSFW channel".format(str(ctx.channel.id)))
                else:
                    id_channel = "".join([char for char in args[0]])
                    
                    if int(id_channel) != 0:
                        if isinstance(ctx.guild, discord.Guild):
                            channel = ctx.guild.get_channel(int(id_channel))
                            if type(channel) == discord.TextChannel:
                                await channel.edit(nsfw=True)
                                await ctx.send("<#{}> now is NSFW channel".format(str(id_channel)))
                    else:
                        await ctx.send("Invalid id channel")

def setup(bot: cmds.Bot):
    bot.add_cog(MainBot(bot))
    print("=> Main library: LOADED")