#!/usr/bin/python3

#Importamos discord
import discord

#Importamos los comandos
from discord.ext import commands

#Creamos la variable bot y definimos el prefijo que tendrá el bot y los intents los declaramos en todos
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#Creamos un evento y funcion para cuando esté listo el bot
@bot.event
async def on_ready():
  #Imprimimos el nombre y el #
  print(f"I am {bot.user}")

#Declaramos el decorador para el comando de ping
@bot.command()
#El parametro es el contexto(saber en que canal está)
async def ping(ctx):
  #El bot responde en el canal con pong!
  await ctx.send("pong!")
  
#Para que el bot pueda leer los comandos usamos .run(token)
#El token ha sido cambiado por estar publico
bot.run("MTI0NTM4MzczNzgyMzQ2NTYwNA.GnXaJK.X6BA7tjAnEztcy17z3YHRyP_vrU7-mpia6eI2o")
