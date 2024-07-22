import discord
from discord.ext import commands
from kodland_utils import *
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

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
async def generate_password(ctx):
    await ctx.send(pass_gen(10))

@bot.command()
async def emoji(ctx):
    await ctx.send(random_emoji())

@bot.command()
async def number(ctx):
    await ctx.send(random_number())

@bot.command()
async def flipacoin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def helper(ctx):
    await ctx.send(helper1())

@bot.command()
async def meme(ctx):
    selected = random.choice(os.listdir('images'))
    with open(f'images/{selected}', 'rb') as f:
        pictures = discord.File(f)
    await ctx.send(file=pictures)

"""------------------------------------------------------------------"""

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

"""------------------------------------------------------------------"""

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

#Daftar sampah
organik = ['sayur', 'sayur busuk', 'makanan basi', 'kotoran hewan', 'dedaunan']
kertas = ['kardus', 'kertas gorengan', 'kertas', 'paperbag']
plastik = ['kresek', 'botol plastik', ' cup plastik', 'mangkok plastik']
logam = ['kaleng', 'batrai', 'hp', 'elektronik', 'kabel']

@bot.command()
async def tanya_sampah(ctx):
    await ctx.send('Apa sampah yang anda ingin periksa?')
    message = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message = str(message.content)

    if message.lower() in organik:
        await ctx.send('Itu adalah sampah **organik**')
        await ctx.send('Sebaiknya, kalian gunakan itu menjadi **pupuk**')

    elif message.lower() in kertas:
        await ctx.send('jelas" itu sampah **kertas** bambang')
        await ctx.send('Mending kamu kumpulkan dan daur ulang jadi kertas')
        await ctx.send('Atau kamu jadiin karya sesuai dengan kreativitasmu')

    elif message.lower() in plastik:
        await ctx.send('Pake logika dikit dong, masa perlu nanya pdhl jelas" sampah **plastik**')
        await ctx.send('Kamu bisa daur ulang sampah plastik itu atau bikin hal" menarik')
        await ctx.send('Seperti pot bunga dari botol plastik, atau bisa dibuat tempat pensil/bolpen, bebazz')

    elif message.lower() in logam:
        await ctx.send('Otak dipake, **logam** ya **logam**')
        await ctx.send('Lebih baik diamankan pada tempat khusus seperti tempat pengolahan limbah B3 terdekat')
        await ctx.send('Jangan dibuang sembarangan, takutnya ada pencemaran lingkungan yang terjadi karena sampah-sampah logam itu')   

    else:
        await ctx.send('Di sistem gweh blom ada sampah gituan, mungkin ga kepikiran karena ga relevan, persis sama cintamu sama dirinya, ga diperhatikan.') 

bot.run('')
