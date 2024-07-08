import discord
from discord.ext import commands
from discord.ext.commands import has_role, MissingRole
import random
import os

# Reemplaza con el token de tu bot
TOKEN = 'MTI1OTIzMDY2NzMzMDU1NTk0NA.G2yTqc.4slec65CrEXGcXyTdOxSXd0aPV1czAgZE21nKA'

# Configurar los intents
intents = discord.Intents.default()
intents.message_content = True

# Lista de IDs de servidores permitidos
ALLOWED_GUILDS = [1237936412851048581]  # Reemplaza con tus IDs de servidor permitidos


# Color morado oscuro en formato hexadecimal
COLOR_MORADO_OSCURO = 0x6A0DAD

# Prefijo para los comandos del bot
bot = commands.Bot(command_prefix='m!', intents=intents)

# Evento cuando el bot se conecta
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Función para enviar mensajes en formato de embed morado
async def enviar_mensaje_embed(ctx, title, description):
    embed = discord.Embed(title=title, description=description, color=COLOR_MORADO_OSCURO)
    embed.set_footer(text="Moon Generator")
    await ctx.reply(embed=embed)  # Responder al mensaje original del usuario

# Función para leer elementos de un archivo .txt y seleccionar uno aleatoriamente
def obtener_elemento_aleatorio(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        elementos = file.readlines()
        return random.choice(elementos).strip()  # Selecciona un elemento aleatorio y quita el salto de línea

# Comando para enviar mensaje directo basado en la categoría
@bot.command(name='gen')
@has_role('Gen Acces')
async def send_md(ctx, categoria: str):
    """Envía un mensaje directo al autor del comando basado en la categoría"""
    if ctx.channel.name != "◞﹕🌑﹕moon・gen":
        await enviar_mensaje_embed(ctx, "Error", "Este comando solo puede ser usado en el canal ◞﹕🌑﹕moon・gen.")
        return
    
    categoria = categoria.lower()  # Convertir a minúsculas para manejar caso insensible
    file_path = f'{categoria}.txt'  # Nombre del archivo basado en la categoría
 
    try:
        # Verificar si existe el archivo para la categoría especificada
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No se encontró el archivo para la categoría {categoria}.")
        
        elemento = obtener_elemento_aleatorio(file_path)  # Obtener elemento aleatorio del archivo
        embed = discord.Embed(title="MOON GENERATOR", description=f"Tu cuenta de {categoria.capitalize()} es:", color=COLOR_MORADO_OSCURO)
        embed.add_field(name=categoria.capitalize(), value=elemento, inline=False)
        embed.set_footer(text="Moon Generator | Created by stevieww_")
        
        await ctx.author.send(embed=embed)
        await enviar_mensaje_embed(ctx, "MOON GENERATOR", f"{ctx.author.mention}, tu cuenta ha sido generada y enviada a tu MD, revisa tus mensajes.")

    except FileNotFoundError as e:
        await enviar_mensaje_embed(ctx, "Error", str(e))

    except Exception as e:
        await enviar_mensaje_embed(ctx, "Error", f"Ocurrió un error al procesar la solicitud: {e}")

# Manejar errores de categoría no encontrada
@send_md.error
async def gen_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await enviar_mensaje_embed(ctx, "Error", "Por favor especifica una categoría válida.")

# Comando con embed para mostrar el stock
@bot.command(name='stock')
@has_role('Gen Acces')
async def embed_stock(ctx):
    if ctx.channel.name != "◞﹕🧾﹕stock・gen":
        await enviar_mensaje_embed(ctx, "Error", "Este comando solo puede ser usado en el canal ◞﹕🧾﹕stock・gen.")
        return
    
    embed = discord.Embed(title="STOCK", description="Servicios disponibles", color=COLOR_MORADO_OSCURO)
    embed.add_field(name="Crunchyroll", value="155", inline=False)
    embed.add_field(name="Duolingo", value="17", inline=False)
    embed.add_field(name="Microsoft", value="1", inline=False)
    embed.add_field(name="Steam rnd", value="829", inline=False)
    embed.add_field(name="Steamop", value="29", inline=False)
    embed.add_field(name="Tidal", value="12", inline=False)
    embed.add_field(name="Napster", value="3", inline=False)
    embed.add_field(name="Ubisoft", value="2", inline=False)
    embed.add_field(name="Fox", value="11", inline=False)
    embed.add_field(name="Max", value="1", inline=False)
    embed.add_field(name="Disney", value="23", inline=False)
    embed.add_field(name="Pornhub", value="300", inline=False)
    embed.add_field(name="Hotmail", value="395", inline=False)
    embed.set_footer(text="Moon Generator | Created by stevieww_")
    await ctx.send(embed=embed)

# Iniciar el bot
bot.run(TOKEN)
