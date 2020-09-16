
import discord
from discord.ext import commands

from pyowm import OWM

owm = OWM('afabf0004f3bdd44581bfa0c1a21a358')


mgr = owm.weather_manager()
observation = mgr.weather_at_place('Mariupol, Ukraine')
w = observation.weather

temp = w.temperature('celsius')['temp']
lol = "В городе сейчас "+ str(temp) + ' по цельсию'











client = commands.Bot(command_prefix='?')


@client.event
async def ready():
    print("БОТ ГОТОВ")


@client.command( pass_context = True )
async def hello(ctx):
    await ctx.send("Здравствуйте!Я WitherBot.Служу ботом для погоды в  Мариуполе!")


@client.command( pass_context = True )
async def weather(ltx):
    await ltx.send(lol)


token = "NzIyNzQzOTQxMDkwMzc3NzI4.Xunhvw.e9xF3OT9YsKL9lRgwUn6YJF4Ybs"
client.run(token)
