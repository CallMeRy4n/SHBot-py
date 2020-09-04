import api.nekolife.nekos as nk
import discord
import datetime
import pprint

def get_image(target: str) -> str:
    if target not in nk.get_valid_key():
        return "https://discordapp.com/assets/322c936a8c8be1b803cd94861bdfa868.png"
    else:
        return nk.img(target)

def regenerate_embed(target: str):
    url_image = get_image(target)
    embed = discord.Embed(title=target, colour=discord.Colour(0x8e3b87), url=url_image)
    embed.set_image(url=url_image)
    return embed
