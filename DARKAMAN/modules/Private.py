import logging

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from DARKAMAN.config import (
    BOT_USERNAME,
    DARKAMAN,
    OWNER,
    PROJECT_NAME,
    SOURCE_CODE,
    SUPPORT_GROUP,
    UPDATES_CHANNEL,
)
from DARKAMAN.helpers.decorators import authorized_users_only
from DARKAMAN.modules.msg import Messages as tr

logging.basicConfig(level=logging.INFO)


@Client.on_message(filters.command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
HOME_TEXT = "<b>ʜᴇʏ, [{}](tg://user?id={})\n\n• ɪ'ᴍ ɖǟʀӄ ʍʊֆɨƈ ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ᴏᴘ ɢʀᴏᴜᴘ ᴅᴇᴠᴇʟᴏᴩᴇᴅ ʙʏ @DARKAMAN\n• ɪ ᴄᴀɴ ᴍᴀɴᴀɢᴇ ᴠᴄ's\n\n• ʜɪᴛ /help ᴛᴏ ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs.</b>"
HELP = """
🎧 <b>I Can Play Musics On VoiceChats 🤪</b>

🎶 **Common Commands**:
• `/song` __Download Song from youtube__
• `/play`  __Play song you requested__
• `/help` __Show help for commands__
• `/dplay` __Play song you requested via deezer__
• `splay` __Play song you requested via jio saavn__
• `/ytplay` __Play song directly from youtube server__
• `/search` __Search video songs links__
• `/current` __Show now playing__
• `/playlist` __Show now playing list__
• `/video` __Downloads video song quickly__
🎶 **Admin Commands**:
• `/player`  __Open music player settings panel__
• `/pause` __Pause song play__
• `/skip` __Skip next song__
• `/resume`  __Resume song play__
• `/userbotjoin`  __Invites assistant to your chat__
• `/end` __Stops music play__
• `/admincache` __Refresh list of admins with vc power__
© Powered By 
[ __ @DARKAMANSUPPORT__ || @DARKAMANCHANNEL__ ]
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
       [
                InlineKeyboardButton('𓆩ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ𓆪',url=f'https://t.me/{BOT_USERNAME}?startgroup=true'),
                InlineKeyboardButton('𓆩ɢʀᴏᴜᴘ𓆪', url='https://t.me/DARKAMANSUPPORT')
                ],[
                InlineKeyboardButton('𓆩ᴄʜᴀɴɴᴇʟ𓆪',url='https://t.me/DARKAMANCHANNEL'),
                InlineKeyboardButton('𓆩ᴀᴍᴀɴ ɢᴜᴊᴊᴀʀ𓆪', url='https://t.me/DARKAMAN')
                ],[
                InlineKeyboardButton('𓆩ᴍᴀɴᴀɢᴇʀ𓆪', url='DARKXV2BOT'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/cc396d1100c438d716430.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('𓆩ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ𓆪', url='https://t.me/DARKXV2BOT?startgroup=true'),
                InlineKeyboardButton('𓆩ɢʀᴏᴜᴘ𓆪', url='https://t.me/DARKAMANSUPPORT')
                ],[
                InlineKeyboardButton('𓆩ᴄʜᴀɴɴᴇʟ𓆪', url='https://t.me/DARKAMANCHANNEL'),
                InlineKeyboardButton('𓆩ᴀᴍᴀɴ ɢᴜᴊᴊᴀʀ𓆪', url='https://t.me/DARKAMAN')
                ],[
                InlineKeyboardButton('𓆩ᴍᴀɴᴀɢᴇʀ𓆪', url='DARKXV2BOT'),
       ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/cc396d1100c438d716430.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
