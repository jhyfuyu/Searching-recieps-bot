from loader import bot
from telebot import types
from database import db_handler
from database.db_handler import get_requests_history_by_id

@bot.message_handler(commands=['help'])
def help(message: types.Message) -> None:
    """ Вывод справки """
    REFERENCE_1 = 'Команды для работы с ботом: \n/history - вывод последних 10 запросов\n/registration - внести данные\n/request - найти рецепт блюда в базе'  
    REFERENCE_2 = '\n\nНажмите на необходимую Вам команду.'
    # TODO строки удобнее разбивать так:
    MESSAGE = "Команды для работы с ботом: \n/history - вывод последних 10 запросов\n/registration - внести данные\n" \
              "/request - найти рецепт блюда в базе\n/high - 10 самых высококалорийных блюд \n" \
              "/low - 10 самых низкокалорийных блюд\n\nНажмите на необходимую Вам команду."

    bot.send_message(message.from_user.id, f'{REFERENCE_1}{REFERENCE_2}')
