import telebot
import TelegramBotAPI
from config import TOKEN, keys
from extensions import ConvertionsException, CryptoConverter

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(massage: telebot.types.Message):
    text="/help список комманд\n /value  доступные валюты\nвведите запрос через пробел: валюта которую перевести, валюта в которую перевести, количество переводимой валюты "
    bot.reply_to(massage,text)

@bot.message_handler(commands=['value'])
def values(massage: telebot.types.Message):
    text= "Доступные валюты"
    for key in keys.keys():
        text="\n".join((text,key,))
    bot.reply_to(massage,text)

@bot.message_handler(content_types=["text",])
def convert(massage:telebot.types.Message):
    try:
        value=massage.text.split(" ")
        if len(value)!=3:
            bot.reply_to(massage, 'Неверное количество параметров')
            raise ConvertionsException("Неверное количество параметров")
        quote, base, amount = value
        total_base = CryptoConverter.convert(quote, base, amount, massage, bot)
    except Exception:
       bot.reply_to(massage, "Не удалось обработать комманду")

    else:
        text= f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(massage.chat.id, text)

bot.polling()


