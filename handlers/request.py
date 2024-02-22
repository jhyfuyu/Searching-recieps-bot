import requests
from os import remove
from api import get_ingredients
from api import get_random_meal
from database import db_handler
from random import choice
from loader import bot
from telebot import types


@bot.message_handler(commands=['request'])
def request(message: types.Message) -> None:
    """ Запрос действия """
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    select_button = types.KeyboardButton('Ввести название блюда')
    random_button = types.KeyboardButton('Не знаю что приготовить')
    keyboard.add(select_button, random_button)

    bot.reply_to(message, 'Выберите действие:', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def saving_name(message: types.Message) -> None:
    if message.text == 'Ввести название блюда':
        bot.send_message(message.from_user.id, "Введите название блюда и/или иные кодовые слова")
        bot.register_next_step_handler(message, api_handler)
    if message.text == 'Не знаю что приготовить':
        cuisines = db_handler.get_cuisines_by_tg_id(message.from_user.id)
        try:
            random_cuisine = choice(cuisines[0][0].split(', '))
            meal = get_random_meal(str(random_cuisine))
            try:
                ingredients = get_ingredients(meal)

                img = requests.get(ingredients[1])
                with open('handlers/images/image.jpg', 'wb') as img_file:
                    img_file.write(img.content)

                bot.send_photo(message.from_user.id, open('handlers/images/image.jpg', 'rb'))
                remove('handlers/images/image.jpg')
                bot.send_message(message.from_user.id, choice(ingredients[0]))
            except IndexError:
                bot.send_message(message.from_user.id, 'Ошибка! Блюдо не найдено в базе!')

        except TypeError:
            bot.send_message(message.from_user.id, f'Ошибка! Кухня {random_cuisine} отсутствует в базе')
        finally:
            keyboard = types.InlineKeyboardMarkup()
            button_turn_back = types.InlineKeyboardButton(text='Назад', callback_data='back_button')
            keyboard.add(button_turn_back)
            bot.send_message(message.from_user.id, 'Хотите вернуться в меню выбора команды?', reply_markup=keyboard)


def api_handler(message: types.Message) -> None:
    """ Вывод на экран данных о блюде """
    try:
        db_handler.save_request(
            message.from_user.id,
            message.text
        )

        ingredients = get_ingredients(message.text)

        img = requests.get(ingredients[1])
        with open('handlers/images/image.jpg', 'wb') as img_file:
            img_file.write(img.content)

        bot.send_photo(message.from_user.id, open('handlers/images/image.jpg', 'rb'))
        remove('handlers/images/image.jpg')
        bot.send_message(message.from_user.id, str(choice(ingredients[0])))

        keyboard = types.InlineKeyboardMarkup()
        button_turn_back = types.InlineKeyboardButton(text='Назад', callback_data='back_button')
        keyboard.add(button_turn_back)
        bot.send_message(message.from_user.id, 'Хотите вернуться в меню выбора команды?', reply_markup=keyboard)

    except IndexError:
        bot.send_message(message.from_user.id, 'Ошибка! Блюдо не найдено в базе!')


@bot.callback_query_handler(func=lambda call: call.data == 'back_button')
def turn_back(call: types.CallbackQuery) -> None:
    chat_id = call.message.chat.id
    bot.send_message(chat_id, 'Нажмите /help чтобы вернуться в меню выбора команды', parse_mode="HTML",
                     reply_markup=types.ReplyKeyboardRemove())
                     
