import logging
import os
import random

import discord

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)


client = discord.Client()
# bot_name = client.user.name

embed = discord.Embed(title="hello", description="world!")


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith("test"):
        await message.channel.send("received")
        await message.channel.send(embed=embed)


discord_bot_token = os.getenv("DISCORD_BOT_TOKEN")

client.run(discord_bot_token)
