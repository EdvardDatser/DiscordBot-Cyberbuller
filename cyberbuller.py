import random
import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import time


client = commands.Bot(command_prefix= "!" )



# <-----===== PASS CHECK =====-----> #

@client.event
async def on_ready():
    while True:
        UserName = input ("Enter Username: ")
        PassWord = input ("Enter Password: ")

        if UserName == 'EdaK' and PassWord == 'Krut':
            time.sleep(1)
            print ("Успешно!")
            logged()
            break
        else:
            print ("Ошибка!")
def logged():
    time.sleep(1)
    print ("Cyberbuller приступает к работе.")




# <-----===== START =====-----> #

#@client.event
# async def on_ready():
   # print("Cyberbuller na baze")


# <-----===== MISC =====-----> #

determine_flip = [1,0]

@client.command(help= "Дефолтный 'coinflip' 50/50.", aliases= ["flip", "coin","Решка","решка","орёл","Орёл","Орел",'орел' ])
async def coinflip(ctx):
    if random.choice(determine_flip)==1:
        embed =discord.Embed(title="Coinflip | (Cyberbuller)", description=f"{ctx.author.mention} Крутанул монету, выпал Орёл!")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Coinflip | (Cyberbuller)",
                              description=f"{ctx.author.mention} Крутанул монету, выпала Решка!")
        await ctx.send(embed=embed)

@client.command(pass_context=True , help="Здарова.")
async def Hello(ctx):
    author = ctx.message.author
    await ctx.send( f" { author.mention } Hi, m8! ")


@client.command(help= "Обычный ролл")
async def roll(ctx):
    await ctx.reply(random.randint(0, 100))

# <-----===== Facts =====-----> #


@client.command(help='Фактик о Илье.', aliases= ["Илья","Ilja",])
async def ilja(ctx):
    user_id = "324167449316425730"
    await ctx.message.channel.send(f"<@{user_id}> Подпивас. A.K.A-GingerSledge .")

@client.command(help = "Фактик о Андрее.", alieses = ["Andrew", "Andrej", "Андрей"] )
async def Andrew(ctx):
    user_id = "457998560567361538"
    await ctx.message.channel.send(f"<@{user_id}> Топ-1 Морф.")

@client.command(help = "Фактик о Мареке.", alieses = ["marek", "марек", "Марек"] )
async def Marek(ctx):
    user_id = "437487615189450752"
    await ctx.message.channel.send(f"<@{user_id}> Rocket League Daddy.")

@client.command(help = "Фактик о Эдварде.", alieses = ["EdaK", "edak", "Edward"] )
async def EdaK(ctx):
    user_id = "338063004736159746"
    await ctx.message.channel.send(f"<@{user_id}> .........")

@client.command(help = "Фактик о Максоне.", alieses = ["max", "Max0ne", "Maksim"] )
async def Max(ctx):
    user_id = "317263096756305922"
    await ctx.message.channel.send(f"<@{user_id}> Максим. ")

# <-----===== Voice =====-----> #


@client.command(help= "Зайдет к тебе в войс, я понимаю ты одинок...")
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f"Бот присоеденился к каналу: {channel} ")


        @client.command(help = "Бот ливает из 'Voice' канала. ", aliases=[ "leave", "l", "Leave" ])
        async def Leave(ctx):
            channel = ctx.message.author.voice.channel
            voice = get(client.voice_clients, guild=ctx.guild)

            if voice and voice.is_connected():
                await voice.disconnect()
            else:
                voice = await channel.connect()
                await ctx.send (f'Бот отключился от канала: {channel}')

# BOOOOOUNTY HUNTEEEER


# <-----===== Voice(2.0) =====-----> # /NOT WORKING. DO NOT SUPPORT PYTHON 3.10/

#YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True',
               #'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
#FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

#@client.command()
#async def play(ctx, *, arg):
   # vc = await ctx.message.author.voice.channel.connect()

    #with YoutubeDL(YDL_OPTIONS) as ydl:
        #if 'https://' in arg:
           # info = ydl.extract_info(arg, download=False)
        #else:
            #info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]

   # url = info['formats'][0]['url']

   # vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=url, **FFMPEG_OPTIONS))


# <-----===== Akinator =====-----> #

@client.command(help="Акинатор - Он всё знает бро, не спорь.", aliases=['8b', 'eightball', '8ball', "akinator"])
async def Akinator(ctx):
    answers = ["Естественно, кто сомневался", "Я пожалуй промолчу", "Да", "Возможно", "Нет", "Скорее да чем нет", "Факт", "Понянтое дело", "Пфф, даже не спрашивай", "Тут даже я безсилен", "Илья" ]
    bot_answer = random.choice(answers)
    await ctx.send(bot_answer)



@client.command(help="Rock,Paper,Scissors.", aliases=['rps',])
async def RockPaperScissors(ctx):
    answers = ["Rock", "Paper", "Scissors"]
    bot_answer = random.choice(answers)
    await ctx.send(bot_answer)

#  Connect

token = open( "token.txt", "r").readline()
client.run( token )


