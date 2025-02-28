import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
import Photo.photo as ph


# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = '7340313394:AAEh26gBE6x48NOW1xJ-XXft-Rb1SIqkmeA'

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()


    @dp.message(CommandStart())
    async def start_handler(message: types.Message, bot: bot):
        photo = ph.url_start
        await bot.send_photo(photo=photo, caption=f"Это фото", chat_id=message.from_user.id)
        logging.info(f"Получена команда /start от {message.from_user.id}")
        await message.answer("Привет! Отправь мне фотографию, и я пришлю её ID.")


    @dp.message(F.photo)
    async def echo_photo_id(message: types.Message):
        # Получаем file_id наибольшего размера фотографии
        photo_id = message.photo[-1].file_id
        await message.answer(f"ID вашей фотографии: {photo_id}")


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':

    asyncio.run(main())