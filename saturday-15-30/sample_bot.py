import discord
from discord.ext import commands
import json

with open("discord_config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

token = config["token"]

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == config["message_id"]:

        guild = client.get_guild(payload.guild_id)

        try:
            role = guild.get_role(config["roles"][str(payload.emoji)])
        except KeyError:
            return

        member = guild.get_member(payload.user_id)

        if role not in member.roles:
            await member.add_roles(role)
            print(f"Assigned {role.name} to {member.name}")


client.run(token)
