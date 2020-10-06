import os
import random
import discord
import numpy as np

from discord.ext import commands
from dotenv import load_dotenv
import constants as C
from tech_talk_controller import TechTalkNewsController

if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    bot = commands.Bot(command_prefix='!')

    tech_talk_controller = TechTalkNewsController()
    client = discord.Client()

    # decorator if needed for roles
    # @commands.has_role('admin')

    @client.event
    async def on_ready():
        topic = np.random.choice(C.TECH_TOPICS)
        url, title, desc = tech_talk_controller.get_tech_news(topic)
        response = f"""
                    **Topic: {topic}**\n***{title}***:\n{desc}\n{url}
                    """
        channel_id = None
        for guild in client.guilds:
            if guild.name == 'SLINGSHOT':
                break
        for channel in guild.channels:
            if channel.name == 'mentors':
                channel_id = channel.id
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        await client.get_channel(channel_id).send(response)

        exit()


    # @bot.command(name='tech_news', help='Get some cool tech news!')
    # async def find_tech_news(ctx):
    #     print("here")
    #     topic = np.random.choice(C.TECH_TOPICS)
    #     url, title, desc = tech_talk_controller.get_tech_news(topic)
    #     response = f"""
    #                 **{title}**:\n{desc}\n{url}
    #                 """
    #     print(response)
    #     await ctx.send(response)

    #     response = random.choice(brooklyn_99_quotes)
    #     await ctx.send(response)

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.errors.CheckFailure):
            await ctx.send('You do not have the correct role for this command.')

    client.run(TOKEN)
