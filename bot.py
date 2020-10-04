from discord.channel import TextChannel
import discord.ext.commands as cmds
import api.nekobot.nekobot as nkb
import api.nekolife.nekolife as nkl
import discord
import dotenv, os

bot = cmds.Bot(os.getenv("PREFIX", "sh!"))

def load_env():
    path = "./.env"
    if os.path.isfile(path):
        dotenv.load_dotenv(path)
        print("LOAD")
    else:
        print("invalid path: "+ path)
        exit()

@bot.command()
async def nekolife(ctx: cmds.Context, *args: tuple):
    if isinstance(ctx.channel, TextChannel):
        if ctx.channel.is_nsfw():
            endpoint = "".join([i for i in args[0]])
            nkl_result = nkl.regenerate_embed(endpoint)
            await ctx.send(embed=nkl_result)
    else:
        await ctx.send("This isn't NSFW channel")

@bot.command()
async def nekobot(ctx: cmds.Context, *args: tuple):
    if isinstance(ctx.channel, TextChannel):
        if ctx.channel.is_nsfw():
            endpoint = "".join([i for i in args[0]])
            nkb_result = nkb.regenerate_embed(endpoint)
            await ctx.send(embed=nkb_result)
    else:
        await ctx.send("This isn't NSFW channel")

@bot.command()
async def setnsfw(ctx: cmds.Context, *args: tuple):
    if isinstance(ctx.channel, TextChannel):
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

def cli():
    flag = True
    while flag:
        i = input("> ")
        if i in ["server joined", "sv joined"]:
            for guild in bot.guilds:
                if isinstance(guild, discord.Guild):
                    print(guild.name+":")
                    print("+ ID: "+str(guild.id))
                    print("+ Member count: "+str(guild.member_count))
                    print("==========================")
        elif i in ["bot status", "status"]:
            print("Bot name: "+ bot.user.name)
            print("Total commands: " + str(len(bot.commands)) + " with prefix is " + bot.command_prefix)
            print("Total server joined: "+ str(len(bot.guilds)))


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(os.getenv("PREFIX")+"help"))
    print(bot.user.name+" is online with:")
    print("+ Prefix: " + os.getenv("PREFIX", "@mention "))
    print("+ Total servers joined: " + str(len(bot.guilds)))
    print("+ Total commands: " + str(len(bot.commands)))
    cli()

load_env()
bot.run(os.getenv("TOKEN"))