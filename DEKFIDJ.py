import discord
from discord.ext import commands
import os
import asyncio
import random
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib import parse
import bs4
import time
import captcha

client = discord.Client()

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

@client.event
async def on_member_join(member):
    try:
        syscha = member.guild.system_channel
        await syscha.send(f"{member.mention} 님 어서오세요 !인증이라고 말해주세요 ! ")
    except:
        pass
    
    if message.content == "/인증":
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = "Captcha.png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))
        embed = discord.Embed(title="인증코드", description = message.author.mention + ", 위에 있는 인증코드를 10초내에 입력해주세요.", timestamp=message.created_at,
        colour=discord.Colour.blurple()
    )
        embed.set_footer(text="FOR#1234", icon_url="https://media.discordapp.net/attachments/725955414444736516/749785381716623436/DSAdSW.PNG"")
        await message.channel.send(embed=embed)

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            embed = discord.Embed(title="실패!", description = message.author.mention + ", __**Captcha**__ 인증시간 ( 10초 ) 를 초과했어요.", timestamp=message.created_at,
            colour=discord.Colour.orange()
    )
            embed.set_footer(text="FOR#1234", icon_url="https://media.discordapp.net/attachments/725955414444736516/749785381716623436/DSAdSW.PNG")
            await message.channel.send(embed=embed)

        if msg.content == a:
            embed = discord.Embed(title="성공!", description = message.author.mention + ", __**Captcha**__ 인증코드를 정확히 입력하여 USER 권한이 지급되었어요!", timestamp=message.created_at,
            colour=discord.Colour.green()
    )
            embed.set_footer(text="FOR#1234", icon_url="https://media.discordapp.net/attachments/725955414444736516/749785381716623436/DSAdSW.PNG")
            await message.channel.send(embed=embed)
            role = discord.utils.get(message.author.guild.roles, name='유저')
            await message.author.add_roles(role)
        
        else:
            embed = discord.Embed(title="실패!", description = message.author.mention + ", __**Captcha**__ 인증코드가 올바르지 않아요! 다시 시도해봐요.", timestamp=message.created_at,
            colour=discord.Colour.red()
    )
            embed.set_footer(text="FOR#1234", icon_url="https://media.discordapp.net/attachments/725955414444736516/749785381716623436/DSAdSW.PNG")
            await message.channel.send(embed=embed)
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
