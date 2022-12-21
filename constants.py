import telebot



chat_ids = {}

token = "5896700548:AAEd-fpjx3xZUqiTla0w4qXEqyi1GKScwBI"


bot = telebot.TeleBot(token)

sheet_header = {
  "A1": "ФИО",
  "B1": "Дата рождения",
  "C1": "Наименование роли",
}