#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝐌𝐲 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : <a href='tg://user?id={OWNER_ID}'>🕊️⃝🇮🇳★𝐃𝐞𝐯𝐢𝐋😈𝐇𝐚𝐜𝐤𝐞𝐫★🇮🇳⃝🕊️</a>\n○ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : <code>Python3</code>\n○ 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 : <a href='https://github.com/rakeshyt/DevilFilesStore'>Click here</a>\n○ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : @JaiHindChatting\n○ 𝐌𝐚𝐢𝐧 𝐆𝐫𝐨𝐮𝐩 : @SonalModdingGod</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
