import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
token = "your bot token!"
bump_channel = 123456789 # but your id instead
bump_bots = [123456789, 5541254, 5225415] # put here ids of bump bots you want block!
@bot.event
async def on_ready():
    for i in range(5):
        print("code by epickejclovek, idea by netext")
@bot.event
async def on_message(message):
    if message.channel.id == bump_channel and message.author.id in bump_bots:
        await message.delete()
    else:
        bot.process_commands(message)
bot.run(token)