import os

from bale import Bot, Message


TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)


@bot.listen("on_ready")
async def on_ready():
    print("🤖 Anime Quiz Bot is ready!")


@bot.listen("on_message")
async def on_message(message: Message):
    if message.content == "/start":
        await message.reply(
            "🎌 سلام! به Anime Quiz خوش اومدی!\n\n"
            "اسم انیمه‌ای که می‌خوای ازش سوال بپرسم رو بنویس 👇"
        )
    else:
        await message.reply(
            f"👌 انیمه انتخاب شد: {message.content}\n\n"
            "حالا آماده‌ای برای سوال‌ها؟ 😎"
        )


bot.run()
