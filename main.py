import random

import discord
from discord.ext import commands
from random import choice, randint
import os # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
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
    if liczba == 1:
        kolor = discord.Color.gold()
        opis = "**1 - Krytyczny Sukces!**"
    elif liczba == 4:
        kolor = discord.Color.blue()
        opis = "**4 - Błogosławieństwo!**"
    elif liczba == 7:
        kolor = discord.Color.red()
        opis = "**7 - Pech!**"
    elif liczba == 8:
        kolor = discord.Color.green()
        opis = "**8 - Szczęście!**"
    elif liczba == 12:
        kolor = discord.Color.dark_gold()
        opis = "**12 - Siła!**"
    elif liczba == 44:
        kolor = discord.Color.dark_blue()
        opis = "**44 - Dar od Bogów!**"
    elif liczba == 69:
        kolor = discord.Color.pink()
        opis = ":heart_eyes:**69 - Miłość!**:heart_eyes:"
    elif liczba == 77:
        kolor = discord.Color.dark_red()
        opis = "**77 - Klątwa Losa!**"
    elif liczba == 88:
        kolor = discord.Color.dark_green()
        opis = "**88 - Dar od Losa!**"
    elif liczba == 100:
        kolor = discord.Color.default()
        opis = "**100 - Krytyczna Porażka!**"
    else:
        kolor = discord.Color.dark_gray()
        opis = f"**{liczba} - Nic się nie wydarzy!**"

    embed = discord.Embed(
        title="Los przepowiedział",
        description=opis,
        color=kolor
    )
    await interaction.response.send_message(embed=embed)



bot.run(os.getenv('DISCORD_TOKEN')) # run the bot with the token