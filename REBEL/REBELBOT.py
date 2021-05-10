#Copyright 2021-2022 REBELBOT
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from REBEL import ALIVE_NAME, StartTime
from REBEL.utils import admin_cmd
from REBEL import bot
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from ULTRA.helpers.functions import get_readable_time
import time
import os
import datetime
#importing finished
from ULTRA import botnickname 
BOT = str(botnickname) if botnickname else "REBEL BOY"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "REBEL BOY"
tim = get_readable_time((time.time() - StartTime))
#pic 👇
PIC = os.environ.get("ALIVE_PIC")
#op 
uptime = tim
#time = date + time okay
TIME = time.asctime(time.localtime())
#my name 👇
REBELBOT = "[REBELBOT](https://t.me/REBELBOT_SUPPOT)"
#my bots repo 👇
REPO = "[REBELBOT](https://github.com/REBEL725/REBELBOT)"
#grpup👇NAME = "[{MAATER}](tg://user?id={X})"
#yrr isko apne bot me aply krne se pehle mere se pooch lena ok
#aur aage add kruga abhi busy okay 🤔
global ghanti
X = bot.uid
MASTER = f"[{NAME}](tg://user?id={X})"
GROUP = "[SUPPORT GROUP](https://t.me/REBELBOT_SUPPORT)"
#itna test h aur aage krte h
#test successful raha ab aage 
ALIVE = "REBELBOT IS ON 🔥 FIRE 🔥 " 
OP = " нєℓℓσ мαѕтєя му ηαмє ιѕ REBELBOT ι αм тнє вєѕт υѕєявσт 💝"
EMOJI = "🔥"
