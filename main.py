import discord
from discord.ext import commands
import logging
import calculator



intents = discord.Intents.all()

bot = commands.Bot(command_prefix='uwu', intents = intents)


@bot.event
async def on_ready():
    print("The bot's done, working gud")




@bot.command()
async def calculate(ctx, *, expression: str):
    try:
        result = calculator.calculate_expression(expression)
        await ctx.send(f"Result: {result}")
    except Exception as e:
        await ctx.send(f"Error in calculation: {e}")

    







with open('token.txt', 'r') as f:
    token = f.read().strip()

bot.run(token)










