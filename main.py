import logging

from aiogram import Bot, Dispatcher, executor, types
import lookup
from googletrans import Translator

API_TOKEN = "6334715119:AAHXFSO3FIO6kuGojDAy9J-SAW-_h4dpx60"
translator = Translator()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

lookup.getDefination("apple")


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Salom")


@dp.message_handler()
async def send(message: types.Message):
    lan = translator.detect(message.text).lang
    if len(message.text.split()) >= 2:
        dest = 'uz' if lan == 'en' else "en"
        await message.reply(translator.translate(message.text, dest).text)
    else:
        try:
            if lan == 'en':
                word_id = message.text
            else:
                word_id = translator.translate(message.text, dest='en').text
            res = lookup.getDefination(word_id)
            voice = lookup.getAudio(word_id)
            await message.reply(f"{res}")
            await message.reply_voice(voice, caption="UK")
        except:
            await message.reply("Bunday so'z topilmadi")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    oxford_lookup.getDefination("apple")
