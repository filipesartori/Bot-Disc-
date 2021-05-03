import discord
import uuid
import json
import urllib.request
import string
import random
import youtube_dl
from discord.ext import commands, tasks
from random import choice
from keep_alive import keep_alive



client = commands.Bot(command_prefix='+')

status = ['Use + / Tocando um Pagode', 'Use + / Comendo', 'Use + / Afinando o cavaco', 'Use + / Treinando a voz']

def senha_aleatoria(string_length=10): #cria o codigo da URL do print
    """Retorna um string aleatoria em string_length."""
    random = str(uuid.uuid4())  #alguma letra aleatoria
    random = random.replace("-","")  #algum numero aleatorio
    return random[0:string_length] #retorna o codigo

@client.event
async def on_ready():
  change_status.start()

@client.command()
async def gay(ctx, args):
    await ctx.send(args + ' é gay.')

@client.command()
async def amongus(ctx):
    fa = open('img/among.txt', 'r')
    Tfa = fa.read()
    await ctx.send(Tfa)

@client.command()
async def print(ctx, *site):
  site = 'https://prnt.sc/' + senha_aleatoria(6)
  await ctx.send(site)

@client.command()
async def video(ctx, *yt):
      count = 1
      API_KEY = 'AIzaSyDd-criexGFJFIYjnqLaIESrAUCRB7LOvo'
      randomY = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

      urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,randomY)
      webURL = urllib.request.urlopen(urlData)
      data = webURL.read()
      encoding = webURL.info().get_content_charset('utf-8')
      results = json.loads(data.decode(encoding))

      for data in results['items']:
        videoId = (data['id']['videoId'])
      yt = 'https://www.youtube.com/watch?v=' + videoId
      await ctx.send(yt)

@client.command()
async def clear(ctx):
  await ctx.channel.purge(limit=None, check=lambda msg: not msg.pinned)

@client.command()
async def secreto(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)

@client.command()
async def apelido(ctx, member : discord.Member, *,display_name):
  await member.display_name()

@client.command()
async def maissecreto(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)

@tasks.loop(seconds = 20)
async def change_status():
  await client.change_presence(activity=discord.Game(choice(status))) 

@client.command(name='ping', help='Retorna o ping')
async def ping(ctx):
  await ctx.send(f'Seu ping é esse meu consagrado: {round(client.latency * 1000)}ms')

@client.command()
async def criador(ctx):
  await ctx.send('O meu criador foi o lindo do **FilipePagodeiro🪕**, siga ele no insta  👉🏻 https://www.instagram.com/filipe9898/')

@client.command()
async def bjs(ctx):
  with open('img/tes.jpg', 'rb') as fh:
    f = discord.File(fh, filename='img/tes.jpg')
    await ctx.send(file=f)


keep_alive()
client.run('sua chave aqui')
