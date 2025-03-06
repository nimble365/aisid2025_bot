import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = "8069908154:AAHZUeNvEwxVaVLFa4zwn6TocRa7i0cySfo"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Разработчики"))
keyboard.add(KeyboardButton("Техническая документация"))
keyboard.add(KeyboardButton("Презентация проекта"))

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Разработчики")
async def send_developers(message: types.Message):
    developers = "Проект разрабатывали:\n1. Айтбаев Жеңіс Жұмабайұлы\n2. Сундет Сумая Байжанқызы"
    await message.answer(developers)

@dp.message_handler(lambda message: message.text == "Техническая документация")
async def send_docs(message: types.Message):
    doc_link = "https://github.com/nimble365/aisid2025_bot/blob/main/tech_doc.md"
    await message.answer(f"Техническая документация доступна по ссылке: {doc_link}")

    with open("tech_doc.md", "rb") as file:
        await message.answer_document(file)

@dp.message_handler(lambda message: message.text == "Презентация проекта")
async def send_presentation(message: types.Message):
    presentation_link = "https://github.com/nimble365/aisid2025_bot/blob/main/aisid2025_presentation.pdf"
    await message.answer(f"Презентация проекта доступна по ссылке: {presentation_link}")

    with open("aisid2025_presentation.pdf", "rb") as file:
        await message.answer_document(file)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
