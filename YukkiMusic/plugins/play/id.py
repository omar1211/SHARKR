import asyncio
from YukkiMusic import app
from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(
    command(["ايدي"])
    & filters.group
    & ~filters.edited
)
async def vambir(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text(       f"""◂ 𝙸𝙳 ↫ `{message.from_user.id}`\n\n◂ 𝙸𝙳 𝙶𝚁𝙾𝚄𝙿 ↫ `{message.chat.id}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊", url=f"https://t.me/L_H_V"),
                ],
                [  
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
