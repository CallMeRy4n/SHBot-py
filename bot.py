import discord.ext.commands as cmds
import api.nekobot.nekobot as nkb
import api.nekolife.nekolife as nkl
import discord

bot = cmds.Bot("sh!")

@bot.command()
async def nekolife(ctx: cmds.Context, *args: tuple):
    if ctx.channel.is_nsfw():
        b = [i for i in args[0]]
        nkl_result = nkl.regenerate_embed(target="".join(b))
        await ctx.send(embed=nkl_result)
    else:
        await ctx.send("This isn't NSFW channel")

@bot.command()
async def nekobot(ctx: cmds.Context, *args):
    if ctx.channel.is_nsfw():
        b = [i for i in args[0]]
        nkb_result = nkb.regenerate_embed("".join(b))
        await ctx.send(embed=nkb_result)
    else:
        await ctx.send("This isn't NSFW channel")

@bot.command()

@bot.event
async def on_ready():
    print("Bot is ready")

bot.run("")