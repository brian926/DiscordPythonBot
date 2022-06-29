import os
import random
import hikari
import lightbulb
from dotenv import load_dotenv
import dnd

# Load Token and Guild ID
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Start Bot
bot = lightbulb.BotApp(token=TOKEN, prefix="!", default_enabled_guilds=961761430728736858)

@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartingEvent) -> None:
    print('Bot has started!')

@bot.command()
@lightbulb.command("24", "Test run of the help comand")
@lightbulb.implements(lightbulb.PrefixCommand)
async def twenty_four(ctx: lightbulb.Context) -> None:
    resources = dnd.list_endpoints()
    view = DropdownView().add_item(Dropdown(resources))

    # Sending a message containing our view
    await ctx.send('Pick your favourite colour:', view=view)

@bot.command()
@lightbulb.option('number_of_dice', 'The number of dices', type=int)
@lightbulb.option('number_of_sides', 'The number of sides', type=int)
@lightbulb.command("roll_dice", "Simulates rolling dice.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def roll(ctx: lightbulb.Context) -> None:
    dice = [
        str(random.choice(range(1, ctx.options.number_of_sides +1)))
        for _ in range(ctx.options.number_of_dice)
        ]
    await ctx.respond(', '.join(dice))

@bot.command()
@lightbulb.option('test', 'The number of dices', type=int)
@lightbulb.command("resources", "List out the different Resources to use")
@lightbulb.implements(lightbulb.SlashCommand)
async def list_options(ctx: lightbulb.Context) -> None:
    print("Printing Resources")
    response = dnd.list_endpoints()
    await ctx.respond(response)

@bot.command()
@lightbulb.option('test2', 'The number of dices', type=int)
@lightbulb.command("options", "List out the different options for a resource")
@lightbulb.implements(lightbulb.SlashCommand)
async def list_options2(ctx: lightbulb.Context) -> None:
    print("Printing Options")
    response = dnd.get_endpoints(endpoint)
    await ctx.respond(response)

@bot.command()
@lightbulb.option('test3', 'The number of dices', type=int)
@lightbulb.command("details", "Get details on an Option from the Resources")
@lightbulb.implements(lightbulb.SlashCommand)
async def list_options3(ctx: lightbulb.Context) -> None:
    print("Printing Details")
    response = dnd.get_details(resource, option)
    await ctx.respond(response)

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

bot.run()