import discord
from discord.ext import commands
import random

try:
    with open("discord.token", 'r') as config:
        token = config.read()
except FileNotFoundError:
    print("File discord.token not found. Quitting...")
    exit(1)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# bot.katsete_arv = 5
# bot.computer_choice = random.randint(1, 100)
bot.games = {}

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


@bot.command()
async def guess(ctx, user_choice):
    player = ctx.author
    
    if player not in bot.games:
        bot.games[player] = {
            "computer_choice": random.randint(1, 100),
            "katsete_arv": 5
        }

    user_choice = int(user_choice)
    computer_choice = bot.games[player]["computer_choice"]
    if (computer_choice == user_choice):
        await ctx.send("You have won!")
        del bot.games[player]
    elif (computer_choice > user_choice):
        await ctx.send("My number is bigger")
    elif (computer_choice < user_choice):
        await ctx.send("My number is smaller")
    else:
        await ctx.send("Invalid input")

    bot.games[player]["katsete_arv"] -= 1
    await ctx.send(str(bot.games[player]["katsete_arv"]) + " guesses remained")

    if bot.games[player]["katsete_arv"] == 0:
        await ctx.send(f"You Lost. My number was {computer_choice}")
        del bot.games[player]

@bot.command()
async def purge(ctx, message_n):
    message_n = int(message_n)
    await ctx.channel.purge(limit=message_n)

bot.run(token)
