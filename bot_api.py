import requests
import os
import discord

import discord
import random

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_NAME = 'BHB_Server'

TOPICS = ['AI', 'Artificial Intelligence', 'ML', 'Machine Learning']

client = discord.Client()


class CustomClient(discord.Client):

    async def on_message(self, message):
        if message.author == client.user:
            return

        brooklyn_99_quotes = [
            'Mamba Mentality',
            'No breaks.'
        ]

        if message.content == 'Mamba':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)

    async def on_ready(self):
        guild = discord.utils.get(self.guilds, name=SERVER_NAME)
        print(
            f'{self.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        # guild members below
        for member in guild.members:
            print(member)
        # print(guild.members)

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
        )

    async def on_error(event, *args, **kwargs):
        with open('err.log', 'a') as f:
            if event == 'on_message':
                f.write(f'Unhandled message: {args[0]}\n')
            else:
                raise Exception


client = CustomClient()
client.run(TOKEN)
