
import logging
from helpers import main_screen, handle_send_document

from constants import bot, token


logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO)

def initialize_bot():
  global token
  global bot

  @bot.message_handler(commands=['start'])
  def welcome(message):
    main_screen(message)

  @bot.message_handler(func=lambda message: True)
  def echo_message (message):
      handle_send_document(message)


  bot.infinity_polling()