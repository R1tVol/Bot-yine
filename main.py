import discord
from discord.ext import commands
from bot_token import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def detect(ctx):
    await ctx.send("Syncing")
    if ctx.message.attachments:
        await ctx.send ("Photo detected")
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            file_path = f"img/{file_name}"
            await attachment.save(file_path)
            await ctx.send ("Resim kaydedildi")

    else:
        await ctx.send("Please insert a photo")
bot.run(token)
