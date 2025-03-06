from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import logging

TOKEN = "8069908154:AAHZUeNvEwxVaVLFa4zwn6TocRa7i0cySfo"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def main_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("Разработчики", callback_data="developers"),
        InlineKeyboardButton("Техническая документация", callback_data="docs"),
        InlineKeyboardButton("Презентация проекта", callback_data="presentation")
    )
    return keyboard

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=main_menu())

@dp.callback_query_handler(lambda call: call.data == "developers")
async def send_developers(call: types.CallbackQuery):
    developers = "👨‍💻 Проект разрабатывали:\n1. Айтбаев Жеңіс Жұмабайұлы\n2. Сундет Сумая Байжанқызы"
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("🔙 Главное меню", callback_data="back"))
    await call.message.edit_text(developers, reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data == "docs")
async def send_docs_menu(call: types.CallbackQuery):
    doc_link = "https://github.com/nimble365/aisid2025_bot/blob/main/tech_doc.md"
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🌐 Открыть документацию", url=doc_link),
        InlineKeyboardButton("📄 Скачать документацию", callback_data="download_docs"),
        InlineKeyboardButton("🔙 Главное меню", callback_data="back")
    )
    await call.message.edit_text("📑 Выберите действие:", reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data == "download_docs")
async def send_docs_file(call: types.CallbackQuery):
    with open("tech_doc.md", "rb") as file:
        await call.message.answer_document(file, caption="📄 Техническая документация")
    await call.message.answer("Выберите действие:", reply_markup=main_menu())

@dp.callback_query_handler(lambda call: call.data == "presentation")
async def send_presentation_menu(call: types.CallbackQuery):
    presentation_link = "https://github.com/nimble365/aisid2025_bot/blob/main/aisid2025_presentation.pdf"
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🌐 Открыть презентацию", url=presentation_link),
        InlineKeyboardButton("📥 Скачать презентацию", callback_data="download_presentation"),
        InlineKeyboardButton("🔙 Главное меню", callback_data="back")
    )
    await call.message.edit_text("🎞 Выберите действие:", reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data == "download_presentation")
async def send_presentation_file(call: types.CallbackQuery):
    with open("aisid2025_presentation.pdf", "rb") as file:
        await call.message.answer_document(file, caption="📥 Презентация проекта")
    await call.message.answer("🔙 Вернуться в главное меню:", reply_markup=main_menu())

@dp.callback_query_handler(lambda call: call.data == "back")
async def go_back(call: types.CallbackQuery):
    await call.message.edit_text("Выберите действие:", reply_markup=main_menu())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
