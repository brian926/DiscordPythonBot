import os
import random
import discord
import dnd
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

# Bot Section
@bot.event
async def on_ready():
    print(f'{bot.user.name} the bot has connected to Dsicord!')

@bot.command(name='24', help='Test run of the help comand')
async def twenty_four(ctx):
    response = '25'
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides +1)))
        for _ in range(number_of_dice)
        ]
    await ctx.send(', '.join(dice))

@bot.command(name='Resources', help='List out the different Resources to use')
async def list_options(ctx):
    print("Printing Resources")
    response = dnd.list_endpoints()
    await ctx.send(response)

@bot.command(name='Options', help='List out the different options for a resource')
async def list_options(ctx, endpoint: str):
    print("Printing Options")
    response = dnd.get_endpoints(endpoint)
    await ctx.send(response)

@bot.command(name='Details', help='Get details on an Option from the Resources')
async def list_options(ctx, resource: str, option: str):
    print("Printing Details")
    response = dnd.get_details(resource, option)
    await ctx.send(response)


@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel : {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)