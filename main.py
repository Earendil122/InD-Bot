import random

import discord
from discord.ext import commands
from random import choice, randint
import os 
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

RUNE_MAP = {
    'A': 'ᚠ',
    'B': 'ᛜ',
    'C': 'ᚦ',
    'D': 'ᚨ',
    'E': 'ᛊ',
    'F': 'ᚲ',
    'G': 'ᚷ',
    'H': 'ᚺ',
    'I': 'ᛞ',
    'J': 'ᛇ',
    'K': 'ᚻ',
    'L': 'ᛁ',
    'M': 'ᛏ',
    'N': 'ᚢ',
    'O': 'ᛒ',
    'P': 'ᛖ',
    'Q': 'ᛗ',
    'R': 'ᚾ',
    'S': 'ᛟ',
    'T': 'ᛈ',
    'U': 'ᛉ',
    'W': 'ᚱ',
    'X': 'ᛋ',
    'Y': 'ᚹ',
    'Z': 'ᛃ'
}

REVERSE_RUNE_MAP = {
    'ᚠ': 'A',
    'ᛜ': 'B',
    'ᚦ': 'C',
    'ᚨ': 'D',
    'ᛊ': 'E',
    'ᚲ': 'F',
    'ᚷ': 'G',
    'ᚺ': 'H',
    'ᛞ': 'I',
    'ᛇ': 'J',
    'ᚻ': 'K',
    'ᛁ': 'L',
    'ᛏ': 'M',
    'ᚢ': 'N',
    'ᛒ': 'O',
    'ᛖ': 'P',
    'ᛗ': 'Q',
    'ᚾ': 'R',
    'ᛟ': 'S',
    'ᛈ': 'T',
    'ᛉ': 'U',
    'ᚱ': 'W',
    'ᛋ': 'X',
    'ᚹ': 'Y',
    'ᛃ': 'Z',
}

def translate_to_runes(text: str) -> str:
    """Funkcja zamienia litery z tekstu na odpowiadające im runy.
       Litery zamieniane są niezależnie od wielkości (wszystko na uppercase).
       Pozostałe znaki pozostają bez zmian."""
    result = ""
    for ch in text:
        upper_ch = ch.upper()
        if upper_ch in RUNE_MAP:
            result += RUNE_MAP[upper_ch]
        else:
            result += ch
    return result

def detranslate_from_runes(text: str) -> str:
    """Funkcja zamienia runy na odpowiadające im litery.
       Znaki, które nie są runami, pozostają bez zmian."""
    result = ""
    for ch in text:
        if ch in REVERSE_RUNE_MAP:
            result += REVERSE_RUNE_MAP[ch]
        else:
            result += ch
    return result




@bot.event
async def on_ready():
    print("bot is ready and online!")
    try:
        synced_commands = await bot.tree.sync()
        print(f"Synaced {len(synced_commands)} commands.")
    except Exception as e:
        print("An error with syncing application commands has occurred: ",e)

@bot.tree.command(name="translator", description="Tłumaczy z naszego na starożytny")
async def translator(interaction: discord.Interaction, text: str):
    translated = translate_to_runes(text)
    await interaction.response.send_message(f"{translated}")

@bot.tree.command(name="detranslator", description="Tłumaczy z starożytnego na nasze")
async def detranslator(interaction: discord.Interaction, text: str):
    translated = detranslate_from_runes(text)
    await interaction.response.send_message(f"{translated}")

@bot.tree.command(name="loss", description="Is this Loss?")
async def loss(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Loss przepowiedział",
        description="~~:.|:;~~",
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="staty", description="Rzucaj tym sobie na statystyki.")
async def staty(interaction: discord.Interaction):

    numbers = [6 + random.randint(1, 6) + random.randint(1, 6) for _ in range(6)]

    embed = discord.Embed(
        title="Oto twoje statystyki, przydzielaj mądrze.",
        description=f"**{numbers}**",
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="los", description="Tutaj zadecyduje się twoje przeznaczenie!")
async def los(interaction: discord.Interaction):
    liczba = random.randint(1, 100)
    
    match liczba:
        case 1:
            kolor = discord.Color.gold()
            opis = "**1 - Krytyczny Sukces!**"
        case 4:
            kolor = discord.Color.blue()
            opis = "**4 - Błogosławieństwo!**"
        case 7:
            kolor = discord.Color.red()
            opis = "**7 - Pech!**"
        case 8:
            kolor = discord.Color.green()
            opis = "**8 - Szczęście**"
        case 12:
            kolor = discord.Color.dark_gold()
            opis = "**12 - Siła!**"
        case 44:
            kolor = discord.Color.dark_blue()
            opis = "**44 - Dar od Bogów**"
        case 69:
            kolor = discord.Color.pink()
            opis = ":heart_eyes: **69 - Miłość!** :heart_eyes:"
        case 77:
            kolor = discord.Color.dark_red()
            opis = "**77 - Klątwa Losa!**"
        case 88:
            kolor = discord.Color.dark_green()
            opis = "**88 - Dar od Losa!**"
        case 100:
            kolor = discord.Color.default()
            opis = "**100 - Krytyczna Porażka**"
        case default:
            kolor = discord.Color.dark_gray()
            opis = f"**{liczba} - Nic się nie wydarzy**"

    embed = discord.Embed(
        title="Los przepowiedział",
        description=opis,
        color=kolor
    )
    await interaction.response.send_message(embed=embed)



bot.run(os.getenv('DISCORD_TOKEN'))