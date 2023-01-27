from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "19425462")
APP_HASH = os.environ.get("APP_HASH", "a859a87bcc16d1021148a245b4bea2d6")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "jdijebdkkxbbot")
session = os.environ.get("TERMUX", "1ApWapzMBu0jSAGznZ7mt77djf30L5eoWP3Zo79fS6XLnELWQqgTMxFRC7qE-7RSXd0Zo28AI5Y8vdEds0XJ6biO3qsz3hsNczoLx0qHdzFC9FmlnjEykY-9aA4khIgHi6OUM6QJm-VQ7HWEVVhhTRUOPMPR7AjtKpfzJJg0WGS8sEG42_wmmgw6SL5f3h8iuAtqT_CIyxpEYOE8jMGNLFbe_rq2vH01tH8a57Vm7siRgUJOHAK8eGZfwjW5xG16CFSjwqgVa2nDY5_5Luqk0rXENJ1z0qG7DEMx-33GCrQBOYuhdqP90XyFTjhepzLnB6VuBuxoC0viIEScaVb_8zALpx6jxdL8=")
SESSION = os.environ.get("TERMUX", "1ApWapzMBu0jSAGznZ7mt77djf30L5eoWP3Zo79fS6XLnELWQqgTMxFRC7qE-7RSXd0Zo28AI5Y8vdEds0XJ6biO3qsz3hsNczoLx0qHdzFC9FmlnjEykY-9aA4khIgHi6OUM6QJm-VQ7HWEVVhhTRUOPMPR7AjtKpfzJJg0WGS8sEG42_wmmgw6SL5f3h8iuAtqT_CIyxpEYOE8jMGNLFbe_rq2vH01tH8a57Vm7siRgUJOHAK8eGZfwjW5xG16CFSjwqgVa2nDY5_5Luqk0rXENJ1z0qG7DEMx-33GCrQBOYuhdqP90XyFTjhepzLnB6VuBuxoC0viIEScaVb_8zALpx6jxdL8=")
token = os.environ.get("TOKEN", "5677480664:AAEKhmSn-dL6IxjGZSr5ixrSJEKNFKlCRGM")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
