from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
session1 = os.environ.get("TERMUX")
SESSION1 = os.environ.get("TERMUX")
token = os.environ.get("TOKEN")
sython1 = TelegramClient(StringSession(session1), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
heroku_api_key = os.environ.get('YOUR_HEROKU_API_KEY')
app_name = os.environ.get('YOUR_APP_NAME')




ispay = ['yes']
ispay2 = ['yes']
bot.start()

