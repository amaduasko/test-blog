from telebot import types
from constants import chat_ids, bot
import asyncio
from services import fetch_xml_doc
from build_data.db import db

def main_screen(message = None):
    if message and bot :
        k_board = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        fio_button = types.KeyboardButton(text="Записать работника")
        k_board.add(fio_button)
        
        bot.send_message(message.chat.id, "Вы в главном меню",reply_markup=k_board)

def handle_send_document(message = None):
    if message and bot:
        if message.text == "Записать работника":
            chat_ids[message.chat.id] = True
            bot.reply_to(message, "Введите ФИО работника")
        elif chat_ids[message.chat.id]:
            bot.reply_to(message, "Документ загружается...")
            db.add_new_user(user_fio=message.text)
            file = asyncio.run(fetch_xml_doc())
            bot.send_document(message.chat.id, file)
            main_screen(message)
            chat_ids[message.chat.id] = False
        else:
            bot.send_message(message.chat.id, """доступные команды: /start""")