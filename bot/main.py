import os

from bale import Bot, Message
from bale.handlers import CommandHandler


TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)


@bot.handle(CommandHandler("start"))
async def start_command(message: Message):
    await message.reply(
        "🎌 سلام! به Anime Quiz خوش اومدی!\n\n"
        "برای شروع کوییز آماده‌ای؟ 😎"
    )


@bot.listen("on_ready")
async def on_ready():
    print("🤖 Anime Quiz Bot is ready!")


bot.run()
