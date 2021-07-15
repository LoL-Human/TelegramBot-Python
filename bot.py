from pyrogram import Client

TOKEN = "" # @botfather
API_ID = "" # https://core.telegram.org/api/obtaining_api_id -> https://my.telegram.org/auth 
API_HASH = "" # https://core.telegram.org/api/obtaining_api_id -> https://my.telegram.org/auth

# https://www.youtube.com/watch?v=HPlFRqjJtX4 [ GET API_ID & API_HASH ]

plugins = dict(
    root="plugins",
)

Client(
    "telegram_bot",
    bot_token=TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=100
).run()