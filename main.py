import logging

import openpyxl
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from defaullt.inline import language, who

# Your Telegram API token
TOKEN = '6673206703:AAGelZ4-f98Lamr_WdwLMQTY6l6dDcWVUhM'

# Initialize the bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

# Middleware for logging
dp.middleware.setup(LoggingMiddleware())


class Mars(StatesGroup):
    uzb_lang = State()
    modme = State()


# Echo handler
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Mars botiga xush kelibsiz! Iltimos, Til tanlang,\n\nДобро пожаловать в Mars Bot! Пожалуйста, "
        "выберите язык\n\nWelcome to Mars Bot! Please select a language",
        reply_markup=language)
    await Mars.uzb_lang.set()


@dp.callback_query_handler(text='Uzbek', state=Mars.uzb_lang)
async def uzb_l(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Iltimos, kimligingizni ko`rsating))', reply_markup=who)


@dp.callback_query_handler(text='stud', state=Mars.uzb_lang)
async def student_login(call: types.CallbackQuery):
    await call.message.answer('Modme id ni kiriting: ')
    await Mars.modme.set()


@dp.message_handler(content_types=types.ContentType.TEXT, state=Mars.modme)
async def texter(message: types.Message, state: FSMContext):
    id_student = message.text
    print(id_student)
    # all values B2 in excel file
    wb = openpyxl.load_workbook('students.xlsx', 'rb')
    # activate workbook

    sheet = wb['Sheet1']
    users = []
    print(True)
    for i in range(2, sheet.max_row + 1):
        users.append(sheet.cell(row=i, column=2).value)
        print(users)
        if int(id_student) in users:
            print('True')
            await message.answer('Siz muvaffaqiyatli kirdingiz')
            print(users)
            bolakaylar = []

            for k in range(2, sheet.max_row + 1):
                _ = []
                for p in range(1,5):

                    _.append(sheet.cell(row=k, column=p).value)
                    if _ not in bolakaylar:
                        bolakaylar.append(_)
            for t in bolakaylar:
                if str(t[1]) == str(id_student):
                    t.remove(0)
                    t.append(1)
            for j in bolakaylar:
                print(j)







            # await state.finish()
            # break


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
