import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'Bot token'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Salom\nBotga Xush kelibsiz yordam kerak bo'lsa quydagi buyurqni yozing\n/help")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):

    await message.reply("Bu bot dagi camandalr\n/dasturchi\n/python")


@dp.message_handler(commands=['dasturchi'])
async def send_welcome(message: types.Message):

    await message.answer("men bckend dasturlash kursda o'qiyapman")

@dp.message_handler(commands=['python'])
async def send_welcome(message: types.Message):

    await message.answer("Python - soddaligi va o'qilishi bilan mashhur bo'lgan mashhur dasturlash tili. U veb-ishlab chiqish, ma'lumotlarni tahlil qilish, sun'iy intellekt va boshqalar kabi turli sohalarda keng qo'llaniladi. Python ko'p qirrali va kuchli bo'lgan kutubxonalar va ramkalarning katta ekotizimiga ega. Python haqida aniq savollaringiz bo'lsa, bemalol so'rang!")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
