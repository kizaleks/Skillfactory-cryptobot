import telebot
import  requests
import json
from config import TOKEN, keys

class ConvertionsException(Exception):
    pass
#Класс с обработчиком ошибок возвращающий сообщение подсказку где ошибка
class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str, massage, bot ):
        if quote==base:
            bot.reply_to(massage,f'Введены одинаковые валюты {base}.')
            raise ConvertionsException(f'Введены одинаковые валюты {base}.')

        try:
            quote_ticker=keys[quote]
        except KeyError:
            bot.reply_to(massage,f'Не удалось обработать валюту {quote}.')
            raise ConvertionsException(f'Не удалось обработать валюту {quote}.')
        try:
            base_ticker=keys[base]
        except KeyError:
            bot.reply_to(massage,f'Не удалось обработать валюту {base}.')
            raise ConvertionsException(f'Не удалось обработать валюту {base}.')
        try:
            amount = float(amount)
        except ValueError:
            bot.reply_to(massage,f'Не удалось обработать количество {amount}.')
            raise ConvertionsException(f'Не удалось обработать количество {amount}.')
        r=requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base= json.loads(r.content)[keys[base]]
        return total_base

