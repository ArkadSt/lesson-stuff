import discord
from discord.ext import commands
import random

# here goes the token 

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

# !play scissors

# scissors on kasutaja_valik
# arvuti valib suvaliselt: rock, paper või scissors - see on arvuti_valik
# võrdleb kasutaja valiku arvuti valikuga
# Vastab kas kasutaja on võitnud/kaotanud/viik

@bot.command()
async def play(ctx, user_choice):
    valikud = ["rock", "paper", "scissors"]

    if not user_choice in valikud:
        await ctx.send("Invalid choice. Correct choices are: " + valikud)
        return

    computer_choice = random.choice(valikud)
    if user_choice == "paper" and computer_choice == "rock" or \
    user_choice == "scissors" and computer_choice == "paper" or \
        user_choice == "rock" and computer_choice == "scissors":
        await ctx.send("You have won!")
    elif user_choice == computer_choice:
        await ctx.send("Draw!")
    else:
        await ctx.send("Computer has won.")

    await ctx.send("Computer choice was: " + computer_choice)




bot.run(token)
