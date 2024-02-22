from loader import bot
from telebot import types
from database import db_handler

inc_data: dict = {}  # TODO лишняя переменная

@bot.message_handler(commands=['registration']) # TODO Определение функции должно отделяться от остального кода двумя пустыми строками
def request_to_user(message: types.Message) -> None:
    """ Сохраняем имя пользователя в БД"""
    bot.send_message(
        message.from_user.id, 
        f"{message.from_user.first_name}, кухни каких стран вам интересны?\nВведите кухни на английском через запятую"
    )
    bot.register_next_step_handler(message, save_data)

def save_data(message: types.Message) -> None: # TODO Определение функции должно отделяться от остального кода двумя пустыми строками
    """ Сохраняем данные в БД """
    initial_data = message.text
    db_handler.set_data(
        initial_data, 
        message.from_user.id, 
        message.from_user.first_name
    )
    bot.send_message(message.from_user.id, 'Ваши данные сохранены! Можете сделать запрос')

    