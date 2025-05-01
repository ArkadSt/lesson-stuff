import discord
from discord.ext import commands

token = ""

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def add(ctx, arg1, arg2):
    await ctx.send(int(arg1) + int(arg2))

bot.run(token)
