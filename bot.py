# Импортируем нужные компоненты

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from constants import token

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def glasha_help(bot, update):
    text = 'Вызван /help'
    print(text)
    my_msg = """
    Ваша расписание на этой неделе:

    Пн - 19.09
        10:00 - 10:45 урок с Жаком
        10:00 - 10:45 урок с Жаком
        10:00 - 10:45 урок с Жаком
        10:00 - 10:45 урок с Жаком

    Вт - 20.09
        10:00 - 10:45 урок с Жаком
        10:00 - 10:45 урок с Жаком
        10:00 - 10:45 урок с Жаком
        10:00 - 10:45 урок с Жаком

    Пт - 24.09
        10:00 - 10:45 урок с Жаком
        10:00 - 10:45 урок с Жаком
        10:00 - 10:45 урок с Жаком
        10:00 - 10:45 урок с Жаком
    """
    update.message.reply_text(my_msg)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater(token, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("help", glasha_help))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


# Вызываем функцию - эта строчка собственно запускает бота
main()
