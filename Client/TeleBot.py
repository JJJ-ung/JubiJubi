from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import Bitcoin
import Stock

class TeleBot():
    token = "1839861409:AAECO1nSWMj6OBvKSuNMXS8mhlT7vkB6Vyo"

    fav = None
    
    # updater 
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    
    # polling
    updater.start_polling()

    def SetFav(fav):
        TeleBot.fav = fav

    # command hander
    def echo(update, context):
        user_id = update.effective_chat.id
        user_text = update.message.text
        if user_text == '즐찾' or user_text == '즐겨찾기':
            text = "코인 즐겨찾기\n"
            context.bot.send_message(chat_id=user_id, text=text)
            if len(TeleBot.fav.BitcoinFav):
                for c in TeleBot.fav.BitcoinFav:
                    print(c.Name)
                    coin = Bitcoin.Bitcoin(Bitcoin.CoinInfo.SearchCoin(c.Name))
                    text = coin.koreanName + " " + coin.ticker + " 정보\n"
                    text += " 현재가 : " + str(coin.getPrice())
                    text += "\n 거래량 : " + str(coin.lstDailyVolume[5]) + "\n"
                    context.bot.send_message(chat_id=user_id, text=text)
            else:
                text = " 비어있음"
                context.bot.send_message(chat_id=user_id, text=text)
            text = "주식 즐겨찾기\n"
            context.bot.send_message(chat_id=user_id, text=text)
            if Stock.StockInfo.login:
                if len(TeleBot.fav.StockFav):
                    for s in TeleBot.fav.StockFav:
                        if Stock.StockInfo.SearchStock(s.Name) != None:
                            result = Stock.StockInfo.SearchStock(s.Name)
                            text = result[0] + " " + result[1] + " 정보\n"
                            text += " 현재가 : " + str(Stock.StockInfo.getPrice(result[0]))
                            text += "\n 거래량 : " + str(Stock.StockInfo.getVolume(result[0]))
                            context.bot.send_message(chat_id=user_id, text=text)
                else:
                    text = " 비어있음"
                    context.bot.send_message(chat_id=user_id, text=text)
        elif Bitcoin.CoinInfo.SearchCoin(user_text) != None:
            c = Bitcoin.Bitcoin(Bitcoin.CoinInfo.SearchCoin(user_text))
            text = c.koreanName + " " + c.ticker + " 정보\n"
            text += " 현재가 : " + str(c.getPrice())
            text += "\n 거래량 : " + str(c.lstDailyVolume[5])
            context.bot.send_message(chat_id=user_id, text=text)
        elif Stock.StockInfo.login:
            if Stock.StockInfo.SearchStock(user_text) != None:
                result = Stock.StockInfo.SearchStock(user_text)
                text = result[0] + " " + result[1] + " 정보\n"
                text += " 현재가 : " + str(Stock.StockInfo.getPrice(result[0]))
                text += "\n 거래량 : " + str(Stock.StockInfo.getVolume(result[0]))
                context.bot.send_message(chat_id=user_id, text=text)
        else:
            text = "정상적인 값 입력 부탁"
            context.bot.send_message(chat_id=user_id, text=text)

    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="주비주비 봇 \n"
                                                                        "주식/코인 이름 입력 \n"
                                                                        "즐찾, 즐겨찾기")

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    