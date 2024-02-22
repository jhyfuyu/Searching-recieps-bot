# Основной файл проекта, через который происходит запуск

from handlers import help, registration, request, start, history
# TODO удаляйте неиспользуемые импорты

from loader import bot
from utils.set_commands import set_default_commands


def main() -> None:
    set_default_commands(bot)
    bot.infinity_polling()


if __name__ == "__main__":
    main()
