import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize bot with command prefix
bot = commands.Bot(command_prefix=os.getenv('COMMAND_PREFIX'))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN'))