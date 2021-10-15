from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**ʜᴇʏ, I'm {bn} 🎵

ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ'ꜱ ᴠᴏɪᴄᴇ ᴄᴀʟʟ. ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [xᴍᴀʀᴛʏ ꜱᴀʟɪᴍ](https://t.me/Xmartperson).

ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ꜰʀᴇᴇʟʏ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💋𝙊𝙬𝙣𝙚𝙧💥", url="https://t.me/imnikkkk")
                  ],[
                    InlineKeyboardButton(
                        "💬 𝙂𝙍𝙊𝙐𝙋", url="https://t.me/cchour"
                    ),
                    InlineKeyboardButton(
                        "✨𝘼𝙙𝙙 𝙈𝙚 𝙏𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥✨", url="https://t.me/Innocent_Bacha_Bot?startgroup=true"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "𝙈𝘼𝙆𝙀 𝙐𝙍 𝙊𝙒𝙉 𝙄𝙁 𝙐 𝙒𝘼𝙉𝙏 𝘼𝙉𝙔 𝙃𝙀𝙇𝙋 𝙋𝙇𝙀𝘼𝙎𝙀 𝘾𝙊𝙉𝙏𝘼𝘾𝙏 𝙈𝙔 𝘽𝙊𝙎𝙎 ", url="https://t.me/shivamdemon"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝙴𝚜𝚎 𝙷𝚒 𝙽𝚊 𝙼𝚊𝚛𝚞𝚗𝚐𝚊 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐎𝐃𝐄⚡", url="https://t.me/shivamdemon")
                ]
            ]
        )
   )


