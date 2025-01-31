import random

import discord
from discord.ext import commands
from random import choice, randint
import os 
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot is ready and online!")
    try:
        synced_commands = await bot.tree.sync()
        print(f"Synaced {len(synced_commands)} commands.")
    except Exception as e:
        print("An error with syncing application commands has occurred: ",e)

@bot.tree.command(name="los", description="Tutaj zadecyduje się twoje przeznaczenie!")
async def los(interaction: discord.Interaction):
    liczba = random.randint(1, 100)
    
    match liczba:
        case 1:
            kolor = discord.color.gold()
            opis = "**Krytyczny Sukces!**"
        case 4:
            kolor = discord.color.blue()
            opis = "**Błogosławieństwo!**"
        case 7:
            kolor = discord.color.red()
            opis = "**7 - Pech!**"
        case 8:
            kolor = discord.color.green()
            opis = "**8 - Szczęście**"
        case 12:
            kolor = discord.color.dark_gold()
            opis = "**12 - Siła!**"
        case 44:
            kolor = discord.color.dark_blue()
            opis = "**44 - Dar od Bogów**"
        case 69:
            kolor = discord.color.pink()
            opis = ":heart_eyes: **69 - Miłość!** :heart_eyes:"
        case 77:
            kolor = discord.color.dark_red()
            opis = "**77 - Klątwa Losa!**"
        case 88:
            kolor = discord.color.dark_green()
            opis = "**88 - Dar od Losa!**"
        case 100:
            kolor = discord.color.default()
            opis = "**100 - Krytyczna Porażka**"
        case default:
            kolor = discord.color.dark_gray()
            opis = f"**{liczba} - Nic się nie wydarzy**"

    embed = discord.Embed(
        title="Los przepowiedział",
        description=opis,
        color=kolor
    )
    await interaction.response.send_message(embed=embed)



bot.run(os.getenv('DISCORD_TOKEN'))