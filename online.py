from colorama import Back, Fore, Style
import os
import json
from discord.interactions import Interaction
from requests import post, Session, get
from re import search
from random import choice
from string import ascii_uppercase, digits
import random
import threading
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
import requests as ru
import discord
from discord import ui
import time
import platform
from datetime import datetime
import pytz
import asyncio
from discord import app_commands
from discord_webhooks import DiscordWebhooks
from discord.ext.commands import Bot
import aiohttp
import uuid
from typing import Any, Coroutine, Literal
import json
from bs4 import BeautifulSoup as bs
from pystyle import Colors, Colorate
import itertools
from discord import SyncWebhook
import requests
from re import match
import sys
import subprocess
from promptpay import qrcode
import itertools
from discord import Activity, ActivityType, Status
import datetime



token = "MTIwMTgyODIyNDM3NjUxMjUxMg.GBmkJ4.kBGl-guufBBe0JVQX8FWHDeIkmBIro7uVEckrw" #TOKEN BOT
ONOFF_ID = 1201827866959159316 # ID CHANNEL


class aclient(commands.Bot):
    def __init__(self): 
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=discord.Intents().all())
        self.role = None

    async def on_ready(self):
        prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        activity = discord.Streaming(name="PROJECT ZERO", url="https://www.twitch.tv/yanglarkdeveloper")
        await client.change_presence(status=discord.Status.idle, activity=activity)
        print(prfx + " Logged in as " + Fore.YELLOW + self.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(self.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))
        synced = await self.tree.sync()
        print(prfx + " Slash CMDs Synced " + Fore.YELLOW + str(len(synced)) + " Commands")
        Welcome = discord.Embed(title="🔔 BOT NOTIFICATION"
                                , description=f"**🟢 บอทกลับมาออนไลน์แล้ว !!** \n Connecting Bot. 🌐 Ping: ({round(client.latency * 1000)} ms)\n บอทออนไลน์มา ||🔃:LOADING|| แล้วนะครับ"
                                ,color=0x2dff1b,)
        channel = client.get_channel(ONOFF_ID)
        message = await channel.send(embed=Welcome)
        i = 0 # วินาที
        s = 0 # นาที
        h = 0 # ชั่วโมง
        d = 0
        while True:
                await asyncio.sleep(1) #86400 1 วัน
                i += 1
                if i == 60: #วินาที
                 i = 0
                 s += 1
            
                if s == 60:
                 s = 0
                 h += 1

                if h == 24:
                 h = 0
                 d += 1
                
                Welcome2 = discord.Embed(title="🔔 BOT NOTIFICATION"
                                , description=f"**🟢 บอทกลับมาออนไลน์แล้ว !!** \n Connecting Bot. 🌐 Ping: ({round(client.latency * 1000)} ms)\n บอทออนไลน์มา ||{h} ชั่วโมง {s} นาที {i}|| แล้วนะครับ"
                                ,color=0x2dff1b,)
                Welcome2.set_footer(text="TEST BY STEPHENCURRY")
                await message.edit(embed=Welcome2)
     

client = aclient()


client.run(token)