#@Stelleron_Hunter



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23537462"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c9599a5aa61ee8ca4f5e778d20c61f24")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7654385403"))

#Port
PORT = os.environ.get("PORT", "8080")

#File Auto Delete
FILE_AUTO_DELETE = int(os.environ.get("FILE_AUTO_DELETE", "0")) # auto delete in seconds


#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "kurumiX_Robot") # Don't Change Database Name

#force sub channel id, if you want to enable force sub (Use different ForceSub Channel ID)
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "0"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "0"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "0"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "0"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/slqlf5")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://files.catbox.moe/slqlf5") 

HELP_TXT = "<b>𝑯𝒆𝒍𝒍𝒐!! 𝑊𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 @Anime_expres 𝒀𝒐𝒖 𝒏𝒆𝒆𝒅 𝒕𝒐 𝒋𝒐𝒊𝒏 𝒊𝒏 𝒎𝒚 𝑪𝒉𝒂𝒏𝒏𝒆𝒍/𝑮𝒓𝒐𝒖𝒑 𝒇𝒊𝒓𝒔𝒕, 𝑷𝒍𝒆𝒂𝒔𝒆 𝒔𝒖𝒃𝒔𝒄𝒓𝒊𝒃𝒆\n\n𝐇𝐞𝐥𝐩𝐥𝐢𝐧𝐞 @anime_chat_expres</b>"
ABOUT_TXT = "𝐀𝐧𝐢𝐦𝐞 𝐂ʜᴀᴛ : <a href='https://t.me/anime_chat_expres'>𝐀𝐧𝐢𝐦𝐞 </a>\n○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_expres'>𝐀𝐧𝐢𝐦𝐞 𝐄𝐭𝐞𝐫𝐧𝐚𝐥𝐬</a>\n○ 𝐎ɴɢᴏɪɴɢ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/ongoing_anime_expres'>𝐎𝐧𝐠𝐨𝐢𝐧𝐠 </a></b>"
START_MSG = os.environ.get("START_MESSAGE", "𝐻𝑒𝑦!! {mention} 𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑇𝑜 𝐶𝑜𝑚𝑚𝑢𝑛𝑖𝑡𝑦. 𝐼𝑓 𝑦𝑜𝑢 𝑤𝑎𝑛𝑡 𝑡𝑜 𝑠𝑢𝑝𝑝𝑜𝑟𝑡 𝑜𝑢𝑟 𝑐𝑜𝑚𝑚𝑢𝑛𝑖𝑡𝑦, 𝑦𝑜𝑢 𝑐𝑎𝑛 𝑑𝑜 𝑠𝑜 𝑏𝑦 𝑠𝑢𝑏𝑠𝑐𝑟𝑖𝑏𝑖𝑛𝑔 𝑡𝑜 𝑜𝑢𝑟 𝑐ℎ𝑎𝑛𝑛𝑒𝑙.» @Anime_expres\n\n 𝑇ℎ𝑎𝑛𝑘𝑠 𝐹𝑜𝑟 𝑦𝑜𝑢𝑟 𝑆𝑢𝑝𝑝𝑜𝑟𝑡")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "</b>𝑯𝒆𝒍𝒍𝒐!! {mention} 𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 @Anime_expres 𝒀𝒐𝒖 𝒏𝒆𝒆𝒅 𝒕𝒐 𝒋𝒐𝒊𝒏 𝒊𝒏 𝒎𝒚 𝑪𝒉𝒂𝒏𝒏𝒆𝒍/𝑮𝒓𝒐𝒖𝒑 𝒇𝒊𝒓𝒔𝒕, 𝑷𝒍𝒆𝒂𝒔𝒆 𝒔𝒖𝒃𝒔𝒄𝒓𝒊𝒃𝒆 𝒕𝒐 𝒐𝒖𝒓 𝒄𝒉𝒂𝒏𝒏𝒆𝒍𝒔 𝒕𝒉𝒓𝒐𝒖𝒈𝒉 𝒕𝒉𝒆 𝒃𝒖𝒕𝒕𝒐𝒏𝒔 𝒃𝒆𝒍𝒐𝒘 𝒂𝒏𝒅 𝒔𝒕𝒂𝒓𝒕 𝒃𝒐𝒕 𝒂𝒈𝒂𝒊𝒏.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @Anime_expres !!\n\n👋Hᴇʏ Fʀɪᴇɴᴅ,🚫Dᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇs ᴛᴏ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ I'ᴍ ᴏɴʟʏ Fɪʟᴇ Sʜᴀʀᴇ ʙᴏᴛ!"

ADMINS.append(OWNER_ID)
ADMINS.append(7654385403)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
