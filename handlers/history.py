from loader import bot
from telebot import types
from database.db_handler import get_requests_history_by_id

@bot.message_handler(commands=['history']) # TODO Определение функции должно отделяться от остального кода двумя пустыми строками
def history(message: types.Message):
    history = get_requests_history_by_id(
        message.from_user.id,
        'req_history'
    )
    if len(history) <= 10:
        bot.send_message(message.from_user.id, f"Ваши 10 последних запросов\n{history}")
    else:
        bot.send_message(message.from_user.id, f"Ваши 10 последних запросов\n{history[-10:]}")
