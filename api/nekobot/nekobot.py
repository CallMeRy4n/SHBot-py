import requests
from pprint import pprint
import discord
# https://docs.nekobot.xyz/#image-endpoints-image

def get_image(endpoint: str) -> str:
    BASE_URL = "https://nekobot.xyz/api/image?type="
    r = requests.get(BASE_URL + endpoint)
    if r.status_code == 200:
        return r.json()["message"]
    return "https://discordapp.com/assets/322c936a8c8be1b803cd94861bdfa868.png"

def regenerate_embed(endpoint: str):
    url_image = get_image(endpoint)
    embed = discord.Embed(title=endpoint, colour=discord.Colour(0x8e3b87), url=url_image)
    embed.set_image(url=url_image)
    return embed
