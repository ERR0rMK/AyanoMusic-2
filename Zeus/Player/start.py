import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME
from config import GROUP_SUPPORT, UPDATES_CHANNEL, START_PIC
from Zeus.filters import command
from Zeus.command import commandpro
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Zeus.main import bot as Client

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**โจ๐แดส ๐สแดสแด ๐ส ๐แดแดแด ๐s ๐๐สแดษดแด ๐แดสแดแด๐ ๐'แด ๐  ๐แดแดกแดสาแดสส ๐๐ ๐ษดแด  ๐สแดแดแด ๐แดษดแดษขแดส ๐แดแด ๐ษชแดส ๐แดแดส ๐แดแดแดสแดs. ๐แดสส ๐สแดแด ๐แด ๐แดแด ๐แด ๐แด ๐แดแดส ๐สแดแดแดs ๐ษชแด ๐แดสแด ๐แดแดแดแดษด ๐แด ๐ษดแดแดก ๐ส ๐แดแดแดแดษดแดsโจ

โโโโโโโโโโโโโโโโโโโโโโโฅ
โฃ ๐แดแดแดแดแด๊ฑ -> @MARcos_ZEUS_XD
โฃ ๐แดแดแดแดสแด -> @TheMKHackerX131
โโโโโโโโโโโโโโโโโโโโโโโฅ
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ โฐ แดแดแด แดแด แดแด สแดแดส ษขสแดแดแด โฑ โ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๊ฑแดแดสแดแด แดแดแดแด", url="https://github.com/zeusop5/AyanoMusic-2"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/stats"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/eb9a9acde7a4a3e051556.jpg",
        caption=f"""Thanks For Adding Me To Ur Chat, For Any Query U Can Join Our Support Groups ๐ฅโฅ๏ธ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ แดแดษชษด สแดสแด ๐", url=f"https://t.me/{GROUP_SUPPORT}")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/eb9a9acde7a4a3e051556.jpg",
        caption=f"""Here Is The Source Code Fork And Give Stars โจ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " สแดแดแด โ๏ธ", url=f"https://github.com/zeusop5/AyanoMusic-2")
                ]
            ]
        ),
    )
