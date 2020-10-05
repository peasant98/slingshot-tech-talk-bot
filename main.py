import os
import random
import numpy as np

from discord.ext import commands
from dotenv import load_dotenv
import constants as C
from tech_talk_controller import TechTalkNewsController

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

tech_talk_controller = TechTalkNewsController()

@bot.command(name='tech_news', help='Get some cool tech news!')
async def find_tech_news(ctx):
    print("here")
    topic = np.random.choice(C.TECH_TOPICS)
    url, title, desc = tech_talk_controller.get_tech_news(topic)
    response = f"""
                **{title}**:\n{desc}\n{url}
                """
    print(response)
    await ctx.send(response)

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice.')
@commands.has_role('admin')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')



bot.run(TOKEN)

