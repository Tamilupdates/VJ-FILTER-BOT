# Don't Remove Credit @VJ_Botz
import os
from pyrogram import Client, filters
from urllib.parse import quote
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import 

@Client.on_message(filters.command(["share_text", "share", "sharetext",]))
async def share_text(client, message):
    reply = message.reply_to_message
    reply_id = message.reply_to_message.id if message.reply_to_message else message.id
    input_split = message.text.split(None, 1)
    if len(input_split) == 2:
        input_text = input_split[1]
    elif reply and (reply.text or reply.caption):
        input_text = reply.text or reply.caption
    else:
        await message.reply_text(
            text=f"**Notice:**\n\n1. Reply Any Messages.\n2. No Media Support\n\n**Any Question Join Support Chat**",                
            reply_to_message_id=reply_id,               
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Updates channel", url=)]])
            )                                                   
        return
    await message.reply_text(
        text=f"**Here is Your Sharing Text 👇**\n\nhttps://telegram.me/share/url?url=" + quote(input_text),
        reply_to_message_id=reply_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("♂️ Share", url=f"https://telegram.me/share/url?url={quote(input_text)}")]])       
    )
