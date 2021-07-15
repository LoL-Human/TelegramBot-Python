from pyrogram import Client, filters
from pyrogram.types import Message
import html


@Client.on_message(filters.command('tagall'))
async def tagall(client: Client, message: Message):
    if "group" in message.chat.type:
        members = await client.get_chat_members(message.chat.id, )
        if len(message.text.split()) >= 2:
            text = message.text.split(None, 1)[1]
        else:
            text = "Tag All"
        for x in members:
            if not x.user.is_bot:
                text += '<a href="tg://user?id={}">{}</a>'.format(x.user.id, html.escape('\u200b'))
    await message.reply_text(text)