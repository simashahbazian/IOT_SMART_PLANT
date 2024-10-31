# services/telegram_bot.py

import telegram
from config.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def send_alert(message):
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
