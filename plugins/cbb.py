# @Stelleron_Hunter

import os
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from config import *
from database.database import add_user, del_user, full_userbase, present_user

START_MSG2 = os.environ.get(
    "START_MESSAGE",
    "𝐻𝑒𝑦 {first}!!\n𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑇𝑜 𝐶𝑜𝑚𝑚𝑢𝑛𝑖𝑡𝑦. 𝐼𝑓 𝑦𝑜𝑢 𝑤𝑎𝑛𝑡 𝑡𝑜 𝑠𝑢𝑝𝑝𝑜𝑟𝑡 𝑜𝑢𝑟 𝑐𝑜𝑚𝑚𝑢𝑛𝑖𝑡𝑦, 𝑦𝑜𝑢 𝑐𝑎𝑛 𝑑𝑜 𝑠𝑜 𝑏𝑦 𝑠𝑢𝑏𝑠𝑐𝑟𝑖𝑏𝑖𝑛𝑔 𝑡𝑜 𝑜𝑢𝑟 𝑐ℎ𝑎𝑛𝑛𝑒𝑙 @Anime_expres\n\n𝑇ℎ𝑎𝑛𝑘𝑠 𝐹𝑜𝑟 𝑦𝑜𝑢𝑟 𝑆𝑢𝑝𝑝𝑜𝑟𝑡"
)

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data

    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")
                    ]
                ]
            )
        )

    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")
                    ]
                ]
            )
        )

    elif data == "start":
        await query.message.edit_text(
            text=START_MSG2.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help"),
                        InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
