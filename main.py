import telebot
from config import keys, TOKEN
from extensions import APIException, ValuteConverter


bot = telebot.TeleBot(TOKEN)  # Создание бота


@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    """
    Ответ бота на команды /start и /help
    :param message:
    :return:
    """
    text = ('Чтобы начать работу с ботом введите:\n'
            '<название валюты> <в какую валюту перевести> <количество валюты>\n'
            'Чтобы увидеть список доступных валют введите: /values')
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    """
    Ответ бота на команду /values
    :param message:
    :return:
    """
    text = 'Список доступных валют: '
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    """
    Ответ бота на ввод текста
    :param message:
    :return:
    """
    try:
        values = message.text.lower().split(' ')  # Разбиваем введённый пользователем текст по пробелам

        if len(values) != 3:
            raise APIException('Слишком много параметров')

        quote, base, amount = values
        total_base = ValuteConverter.get_price(quote, base, amount)  # Результат конвертации валют
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:  # Если введённый пользователем текст не попал под вышеописанные исключения, то бот отправляет результат конвертации
        text = f'Цена {amount} {quote} в {base}: {total_base}'
        bot.reply_to(message, text)


bot.polling(non_stop=True)  # Запуск бота
