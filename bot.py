import discord.ext.commands as cmds
import api.nekobot.nekobot as nkb
import api.nekolife.nekolife as nkl
import discord
import dotenv, os

bot = cmds.Bot("sh!")

def load_env():
    path = "./.env"
    if os.path.isfile(path):
        dotenv.load_dotenv(path)
        print("LOAD")
    else:
        print("invalid path: "+ path)

@bot.command()
async def nekolife(ctx: cmds.Context, *args: tuple):
    if ctx.channel.is_nsfw():
        b = [i for i in args[0]]
        nkl_result = nkl.regenerate_embed(target="".join(b))
        await ctx.send(embed=nkl_result)
    else:
        await ctx.send("This isn't NSFW channel")

@bot.command()
async def nekobot(ctx: cmds.Context, *args: tuple):
    if ctx.channel.is_nsfw():
        b = [i for i in args[0]]
        nkb_result = nkb.regenerate_embed("".join(b))
        await ctx.send(embed=nkb_result)
    else:
        await ctx.send("This isn't NSFW channel")

@bot.command()
async def setnsfw(ctx: cmds.Context, *args: tuple):
    if ctx.channel.is_nsfw():
        await ctx.send("This already a NSFW channel")
    else:
        if not args or args == ():
            await ctx.channel.edit(nsfw=True)
            await ctx.send("<#{}> now is NSFW channel".format(str(ctx.channel.id)))
        else:
            id_channel = "".join([char for char in args[0]])
            if int(id_channel) != 0:
                channel = ctx.guild.get_channel(int(id_channel))

                if type(channel) == discord.TextChannel:
                    await channel.edit(nsfw=True)
                    await ctx.send("<#{}> now is NSFW channel".format(str(id_channel)))
            else:
                await ctx.send("Invalid id channel")

@bot.event
async def on_ready():
    print("Bot is ready")

load_env()
bot.run(os.getenv("TOKEN"))