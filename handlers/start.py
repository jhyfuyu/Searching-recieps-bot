from loader import bot
from telebot import types

@bot.message_handler(commands=['start'])
def start(message: types.Message) -> None:
    """ Приветственное сообщение """
    bot.send_photo(message.chat.id, open('handlers/images/bot_main_image.jpg', 'rb'))
    bot.send_message(message.chat.id, "Привет, я бот\n Я здесь чтобы помочь тебе найти в базе любой рецепт.")