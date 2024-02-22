from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from myconfig import config

storage = StateMemoryStorage()
bot = TeleBot(token=config.TELEBOT_TOKEN, state_storage=storage)
