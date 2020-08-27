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

@client.event
async def on_message(message):
    if message.content == '!인증':
        syscha = message.channel
        embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
        embed.add_field(name="잠시만 기다려주세요", value="역할 지급중...", inline=True)
        embed.set_footer(text=f"{message.author}, 인증중", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        time.sleep(8)
        await message.delete()
        embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
        await syscha.send(f"{message.author.mention} 님 역할이 지급 되었습니다 !")
        role = discord.utils.get(message.author.guild.roles, name='유저')
        await message.author.add_roles(role)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
