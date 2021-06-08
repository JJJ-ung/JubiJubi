from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

class TeleBot():
    token = "1839861409:AAECO1nSWMj6OBvKSuNMXS8mhlT7vkB6Vyo"
    
    # updater 
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    
    # polling
    updater.start_polling()

    # command hander
    def echo(update, context):
        user_id = update.effective_chat.id
        user_text = update.message.text
        #주식/코인 확인 검사
        #코인 티커 이름 영문이름
        #주식 코드 이름
        #고가/저가/현재가/최근 5일 종가/거래량
        text = f"텍스트"
        context.bot.send_message(chat_id=user_id, text=text)
    
    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="주비주비 봇 \n"
                                                                        "주식/코인 이름 입력")
    