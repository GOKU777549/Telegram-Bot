# Bot/modules/start.py

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import MediaEmpty
import asyncio

from Bot import bot
from Bot.db.users import add_user, get_user
from Bot.core.decorators.tracking import track_user
from Bot.core.decorators.error_handler import handle_errors
from Bot.core.utils.formatting import format_user_mention
from Bot.db.groups import save_group_for_drop  # Make sure this exists

# ✅ Valid video file ID
VIDEO_FILE_ID = "BAACAgQAAxkBAAMGaJGjPcSIJn1Qi6HZQYnliYyHZZoAAucHAAKJDm1RRZTIdDl7u8AeBA"

# 📜 Caption text
CAPTION = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━⧫
✾ Wᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ Naruto Bᴏᴛ
┗━━━━━━━━━━━━━━━━━━━━━━━━━⧫
┏━━━━━━━━━━━━━━━━━━━━━━━━━⧫
┠ ➻ I ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ ғɪɴᴅ ʏᴏᴜʀ Wᴀɪғᴜ ᴏʀ Hᴜsʙᴀɴᴅᴏ
┃        ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ.
┠ ➻ Yᴏᴜ ᴄᴀɴ sᴇᴀʟ ᴛʜᴇᴍ ʙʏ /guess ᴄᴏᴍᴍᴀɴᴅ
┃        ᴀɴᴅ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ʜᴀʀᴇᴍ.
┗━━━━━━━━━━━━━━━━━━━━━━━━━⧫
Tᴀᴘ ᴏɴ "Hᴇʟᴘ" ғᴏʀ ᴍᴏʀᴇ ᴄᴏᴍᴍᴀɴᴅs.
"""

# 🔘 Button layout
async def get_buttons():
    me = await bot.get_me()
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ αdd мe тσ yσυʀ ɡʀσυρ", url=f"https://t.me/{me.username}?startgroup=true")],
        [
            InlineKeyboardButton("ѕυρρσʀт cнαт", url="https://t.me/+ZyRZJntl2FU0NTk1"),
            InlineKeyboardButton("ѕυρρσʀт cнαɴɴel", url="https://t.me/Bey_war_updates")
        ],
        [
            InlineKeyboardButton("σωɴer", url="https://t.me/Uzumaki_X_Naruto_6"),
            InlineKeyboardButton("нelρ", callback_data="help_data")
        ]
    ])

# 🎬 Send intro video
async def send_start_video(chat_id: int):
    buttons = await get_buttons()
    try:
        await bot.send_video(
            chat_id=chat_id,
            video=VIDEO_FILE_ID,
            caption=CAPTION,
            reply_markup=buttons
        )
    except MediaEmpty:
        await bot.send_message(chat_id, "⚠️ The video file is invalid or empty. Contact the bot owner.")
    except Exception as e:
        await bot.send_message(chat_id, f"❌ An unexpected error occurred:\n{e}")

# 💌 Private /start
@bot.on_message(filters.command("start") & filters.private)
@handle_errors
@track_user
async def private_start(_, message: Message):
    chat_id = message.chat.id

    # Loading animation
    loading = await message.reply("⚡")
    await asyncio.sleep(1.5)
    await loading.delete()

    msg = await message.reply("𝐋𝐎𝐀𝐃𝐈𝐍𝐆.")
    for dots in ["..", "..."]:
        await asyncio.sleep(0.5)
        await msg.edit(f"𝐋𝐎𝐀𝐃𝐈𝐍𝐆{dots}")
    await asyncio.sleep(0.5)
    await msg.delete()

    await send_start_video(chat_id)

# 🧩 Group /start
@bot.on_message(filters.command("start") & filters.group)
@handle_errors
async def group_start(_, message: Message):
    await save_group_for_drop(message.chat.id)

    me = await bot.get_me()
    start_button = InlineKeyboardMarkup([[
        InlineKeyboardButton("🚀 START IN DM", url=f"https://t.me/{me.username}?start")
    ]])

    await message.reply_text(
        "✧ .:｡✧ 𝗡𝗔𝗥𝗨𝗧𝗢 𝗫 𝗪𝗔𝗜𝗙𝗨 ✧｡:. ✧\n\nTo start playing, please initiate me in DMs!",
        reply_markup=start_button,
        disable_web_page_preview=True
    )