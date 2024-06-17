#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

# variables
API_ID = "cb1ba6bba27a3c68d219e5e34419cb5e" #config("API_ID", default=None, cast=int)
API_HASH = "24709391" #config("API_HASH", default=None)
BOT_TOKEN = "6662990823:AAGpNXjYprMbJb4l5TD_sEKARVvyXRuGjg4" #config("BOT_TOKEN", default=None)
SESSION = "BQGoP-IAYvKF0WFYziO01tybiU2AqjHVVN5BeN0ut5eXA_dif-SAd0A4wjbOLsvCe4e_2h8QAqIu-03-WdqBaTRiQgYRt30b8MuyESMc6186QGtjiwX9PJrEoKHLmIuRtjAvjhR7s0jM9DI--NU29FCBqxHXDkicIKiuk7noGBsLD68cNc8WQTCnrpLz7xdoBkvaR8ONWlcNAeVcnarCwoAwHnpu5zqX7JiFe6NUHdz0_zqIqfLPRDb12MpI1aIQSb5JTsd5jWArbkSDxQkUodtJ92S0ltdCnHpS5eTaanjgDDplGDSJkMKHYg90mHN7EWIFKqfBYK5BHg7eIRqCjflXC1EkgQAAAAAsaRVjAA" #config("SESSION", default=None)
FORCESUB = "bot_user12838" #config("FORCESUB", default=None)
AUTH = "1923238241" #config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    # print(e)
    # logger.info(e)
    sys.exit(1)
