import os
import asyncio
import sys
import git
import heroku3
from Zeus.main import BOT
from config import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY
from telethon.tl.functions.users import GetFullUserRequest
# alive Pic By Default It's Will Show Our
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
hl = '/'
deadlyversion = 'Spambot0.10'

ZAID_PIC = "https://telegra.ph/file/7262dbb16274f074764b4.jpg"
  

DEADLY = "โฏ ๐๐ฎ๐ฌ๐ข๐+๐๐๐ข๐ ๐๐ฉ๐๐ฆ ๐๐จ๐ญ โฏ\n\n"
DEADLY += f"โโโโโโโโโโโโโโโโโโโ\n"
DEADLY += f"โข **แดสแดสแดษด แด แดสsษชแดษด** : `3.10.1`\n"
DEADLY += f"โข **แดแดสแดแดสแดษด แด แดสsษชแดษด** : `{version.__version__}`\n"
DEADLY += f"โข **vแดสsษชแดษด**  : `{deadlyversion}`\n"
DEADLY += f"โโโโโโโโโโโโโโโโโโโ\n\n"   

                                  
@BOT.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
     await BOT.send_file(event.chat_id,
                                  ZAID_PIC,
                                  caption=DEADLY,
                                  buttons=[
        [
        Button.url("แดสแดษดษดแดส", "https://t.me/about_zeus_xd"),
        Button.url("sแดแดแดแดสแด", "https://t.me/TheMKHackerX131")
        ],
        [
        Button.url("โข สแดแดแด โข", "https://github.com/zeusop5/AyanoMusic-2")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"โฐโขโโฐ  โฦกลษ  โฐโโขโฏ\n\nโ  สโษษษ : `{ms}`\n โ  ลณโษฌฤฑษฑษ : 15h:6m:34s\nโ  ฦกแฟณลษเฝ : โคออโ๐ฉแชต๐๐๐๐ ๐ฉ๐๐๐ช ๐ฅ\nโฐ ๐ด๐๐ด๐๐ ๐๐๐๐ผ๐ถ ๐ผ๐ ๐ด๐ฟ๐ผ๐๐ธ โฐ")
        
    

@BOT.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**Rebooting โช๏ธ**.. Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await BOT.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

# this Feature Will Works only If u r Added Heroku api
@BOT.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding user as a sudo...")
        DEADLY = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** as a sudo user ๐ฑ Restarting.. Please wait a minute...")
        heroku_var[DEADLY] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
