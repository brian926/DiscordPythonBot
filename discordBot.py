import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import dnd

# Load Token and Guild ID
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Start Bot
# Intents will be discontinued after August 31, 2022
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Classes for Dropdown
class Dropdown(discord.ui.Select):
    def __init__(self, resources):
        self.resources = resources

        # Set the options that will be presented inside the dropdown
        option = []

        for item in resources:
            option.append(discord.SelectOption(label=item.capitalize()))

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='Choose your favourite colour...', min_values=1, max_values=1, options=option)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's 
        # selected options. We only want the first one.
        response = dnd.get_endpoints(self.values[0])
        await interaction.response.send_message(response)


# Class for View to add Select to
class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

# Bot Section
@bot.event
async def on_ready():
    print(f'{bot.user.name} the bot has connected to Discord!')

@bot.command(name='24', help='Test run of the help comand')
async def twenty_four(ctx):
    resources = dnd.list_endpoints()
    view = DropdownView().add_item(Dropdown(resources))

    # Sending a message containing our view
    await ctx.send('Pick your favourite colour:', view=view)


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