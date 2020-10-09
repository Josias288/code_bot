import discord
from discord.ext import commands

bot = commands.Bot(commands_prefix = "!", description ="Bot d'acceuil")

@bot.event
async def on_ready():
    print("Ready !")


bot.run("NzY0MjI0Mjg0MTYzNDQwNjUw.X4DJUw.atq9op0aiaIo3danuZKA7UdXSgw")