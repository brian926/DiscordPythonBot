import os
import random
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='!')


# Client Section
@client.event
async def on_ready():
    print(f'{client.user.name} the client has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
        )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '99!':
        response = '100'
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


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
    if isinstance(error, commands.error.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


bot.run(TOKEN)
client.run(TOKEN)