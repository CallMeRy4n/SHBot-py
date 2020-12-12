from discord.channel import TextChannel
import discord.ext.commands as cmds
import extensions.api.nekobot.nekobot as nkb
import extensions.api.nekolife.nekolife as nkl
import discord, dotenv, os

bot = cmds.Bot("sh#")

def load_env():
    path = "./.env"
    if os.path.isfile(path):
        dotenv.load_dotenv(path)
        print("LOAD")
    else:
        print("invalid path: "+ path)
        exit()

def load_library():
    for filename in os.listdir("./extensions"):
        if filename.endswith(".py"):
            bot.load_extension(f'extensions.{filename[:-3]}')
            
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("sh#help as python bot :))"))
    print(bot.user.name+" is online with:")
    print("+ Prefix: " + os.getenv("PREFIX", "@mention "))
    print("+ Total servers joined: " + str(len(bot.guilds)))
    print("+ Total commands: " + str(len(bot.commands)))
    load_library()

load_env()
bot.run(os.getenv("TOKEN"))