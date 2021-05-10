import os
try:
  from LEGENDX import id, ID, devs, LEGEND
except:
  os.system("pip install LEGENDX")
  from LEGENDX import id, ID, devs, LEGEND
else:
  print ("something got fucked")
finally:
  print ("REBELBOT IS STARTING WITH TELETHON")
  from REBELBOT import xbot
from REBEL import bot
from sys import argv
import sys
import os
os.system("pip install google_trans_new")
import glob
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient, Button
from var import Var
from REBEL.utils import load_module, load_pro
from REBEL import LOAD_PLUG, BOTLOG_CHATID
from pathlib import Path
import asyncio
TOKEN = os.environ.get("TG_BOT_TOKEN", None)
import telethon.utils
EXTRA_PLUGS = os.environ.get("EXTRA_PLUGS", False)
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

import glob



path = 'REBEL/plugins/assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_pro(shortname.replace(".py", ""))


if  EXTRA_PLUGS == True:
    os.system("git clone .git ./REBEL/plugins/")
    path = "REBEL/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            try:
                load_module(plugin_name.replace(".py", ""))
                if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                    print ('INSTALLING ALL MODULES', plugin_name)
            except:
                pass

else:
  path = 'REBEL/plugins/*.py'
  files = glob.glob(path)
  for name in files:
      with open(name) as f:
          path1 = Path(f.name)
          shortname = path1.stem
          load_module(shortname.replace(".py", ""))


import REBEL._core

print("REBEL is Up and Awake! ©️ TEAMREBELBOT 2021")
async def legend():
  try:
    pro = await xbot.get_me()
    legend = await bot.get_me()
    PROBOYX = [[Button.inline("Hᴇʀᴏᴋᴜ Vᴀʀs", data='ass_back')]]
    LEGENDX = f"""
**Sᴏᴍᴇᴛʜɪɴɢ Hᴀᴘᴘᴇɴᴇᴅ ! Lᴇᴛs Cʜᴇᴄᴋ** 🤔 

`☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎`

**Dɪɴɢ Dᴏɴɢ...** `.\./.\` **Tɪɴɢ Tᴏɴɢ...** `./.\./` **REBELBOT Hᴀs Bᴇᴇɴ Dᴇᴘʟᴏʏᴇᴅ !!**

**Pɪɴɢ Pᴏɴɢ...**

**➥ Mᴀsᴛᴇʀ** `➪` **@{legend.username}**
**➥ Assɪsᴛᴀɴᴛ** `➪` **@{pro.username}**
**➥ Sᴜᴘᴘᴏʀᴛ** `➪` **@UltraXchaT**
**➥ Cʜᴀɴɴᴇʟ** `➪` **@UltraX_SupporT**

**Cʜᴇᴄᴋ ᴍᴏɪ Pɪɴɢ ᴛɪᴍᴇ ʙʏ** `.ping` **[Fᴏʀ UsᴇʀBᴏᴛ] or** `/ping` **[Fᴏʀ Assɪsᴛᴀɴᴛ]**
"""
    await xbot.send_message(bot.me.id, LEGENDX, buttons=PROBOYX)
  except:
     pass


bot.loop.run_until_complete(legend())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
    
else:
    bot.run_until_disconnected()
    

