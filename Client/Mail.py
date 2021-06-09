import smtplib
from email.message import EmailMessage

import Bitcoin
import Stock
import time

class Mail():
    sender = '2021jubijubi@gmail.com'
    password = 'qwer1234!@#$'
    subject = '주비주비 거래 정보'
    fav = None


    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(sender, password)

    def SendEmail(target, fav):
        msg = EmailMessage()

        msg['From'] = Mail.sender
        msg['Subject'] = Mail.subject
        msg['To'] = target + "@gmail.com"
        content = []
        
        text = "코인 즐겨찾기\n"
        content.append(text)
        if len(fav.BitcoinFav):
            for c in fav.BitcoinFav:
                print(c.Name)
                coin = Bitcoin.Bitcoin(Bitcoin.CoinInfo.SearchCoin(c.Name))
                text = coin.koreanName + " " + coin.ticker + " 정보\n"
                text += " 현재가 : " + str(coin.getPrice())
                text += "\n 거래량 : " + str(coin.lstDailyVolume[5]) + "\n"
                content.append(text)
                time.sleep(0.3)
        else:
            text = " 비어있음"
            content.append(text)
        text = "주식 즐겨찾기\n"
        content.append(text)
        if Stock.StockInfo.login:
            if len(fav.StockFav):
                for s in fav.StockFav:
                    if Stock.StockInfo.SearchStock(s.Name) != None:
                        result = Stock.StockInfo.SearchStock(s.Name)
                        text = result[0] + " " + result[1] + " 정보\n"
                        text += " 현재가 : " + str(Stock.StockInfo.getPrice(result[0]))
                        text += "\n 거래량 : " + str(Stock.StockInfo.getVolume(result[0]))
                        content.append(text)
            else:
                text = " 비어있음"
                content.append(text)

        msg.set_content("".join(content))

        Mail.smtp.send_message(msg)
