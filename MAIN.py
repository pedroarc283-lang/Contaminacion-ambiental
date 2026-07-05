import discord
from discord.ext import commands
import random
import requests
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command()
async def information(ctx):
    await ctx.send('La contaminación ambiental es la introducción de sustancias químicas, físicas o biológicas nocivas en un entorno natural o artificial. Estos agentes alteran el equilibrio de los ecosistemas, volviéndolos inseguros y provocando graves daños en la salud de los seres humanos, la flora y la fauna. La contaminación puede ser causada por diversas actividades humanas, como la industria, el transporte, la agricultura y la deforestación. Los principales tipos de contaminación incluyen la contaminación del aire, del agua, del suelo y la contaminación acústica. Es fundamental tomar medidas para reducir la contaminación ambiental y proteger nuestro planeta para las generaciones futuras.')

@bot.command()
async def tips(ctx):
    await ctx.send('Aquí tienes algunos consejos para reducir la contaminación ambiental:\n'
                   '1. Reduce, reutiliza y recicla: Minimiza el desperdicio y recicla materiales siempre que sea posible.\n'
                   '2. Usa transporte sostenible: Camina, usa bicicleta o transporte público en lugar de vehículos privados.\n'
                   '3. Ahorra energía: Apaga luces y electrodomésticos cuando no los uses y utiliza bombillas de bajo consumo.\n'
                   '4. Planta árboles: Los árboles ayudan a limpiar el aire y proporcionan hábitats para la fauna.\n'
                   '5. Evita productos químicos nocivos: Utiliza productos de limpieza ecológicos y evita pesticidas dañinos.\n'
                   '6. Educa a otros: Comparte información sobre la importancia de cuidar el medio ambiente.')

@bot.command()
async def videos(ctx):
    ambiental_videos = [
        'https://youtu.be/D5NKrsDkQ00?si=xj36owtkvCoKypqF',
        'https://youtu.be/bIn8MHc7VT0?si=A5sCYMde3AnopmQZ',
        'https://youtu.be/RTRxZvVcjfM?si=EecFQAmp04jL12AI'
    ]
    randomchoice = random.choice(ambiental_videos)
    await ctx.send(f'Aquí tienes un video sobre la contaminación ambiental: {randomchoice}')


@bot.command()
async def infografias(ctx):
    img = random.choice(os.listdir('IMAGES'))
    with open(f'IMAGES/{img}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
