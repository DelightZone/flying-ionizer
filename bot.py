import os
import discord
from discord.ext import commands

# Get token from environment variable
TOKEN = os.environ.get("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Flying Ionizer is online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def say(ctx, *, message: str):
    await ctx.send(message)

@bot.command()
async def ionize(ctx):
    await ctx.send("💥 IONIZATION COMPLETE 💥")

bot.run(TOKEN)
