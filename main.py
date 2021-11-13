from pyrogram import Client as Bot

from callsmusic import run
from config import API_HASH, API_ID, BOT_TOKEN

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="KipliMusicV2"),
)

print("KIPLI MUSIC V2 STARTED!")

bot.start()
run()
