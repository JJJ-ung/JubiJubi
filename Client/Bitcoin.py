import pyupbit
import requests
import json

class CoinInfo():
    data = requests.get("https://api.upbit.com/v1/market/all").json()

    accessKey = ""
    secretKey = ""
    acount = None

    def setKey(access, secret):
        if access != "" or secret != "":
            print(access, secret)
            CoinInfo.accessKey = access
            CoinInfo.secretKey = secret
            acount = pyupbit.Upbit(CoinInfo.accessKey, CoinInfo.secretKey)
            if acount.get_balance() == None:
                acount = None
                print("Login Error")
            else:
                print("Login success")

    def SearchCoin(str):
        for coin in CoinInfo.data:
            if coin['market'].startswith("KRW"):
                if coin['market'].lower().endswith(str.lower()) or coin['korean_name'] == str or coin['english_name'].lower() == str.lower():
                    return coin

    def getBalance():
        return int(acount.get_balance()['balance'])

class Bitcoin():
    intervalTable = ["minute1", "minute3", "minute5", "minute10", "minute15", "minute30", "minute60", "minute240", "day", "week", "month"]

    def __init__(self, info):
        self.ticker = info['market']
        self.koreanName = info['korean_name']
        self.englishName = info['english_name']
        self.interval = "day"
        self.lstDailyData = list(pyupbit.get_ohlcv(self.ticker, count=6, interval=self.interval)['close']) # 날짜 오름차순
        self.lstDailyVolume = list(pyupbit.get_ohlcv(self.ticker, count=6, interval=self.interval)['volume'])
        self.chartData = list(pyupbit.get_ohlcv(self.ticker, interval=self.interval)['close'])
        self.graphData = pyupbit.get_ohlcv(self.ticker, count=100, interval="minute1")
        self.Low = list(self.graphData['low'])
        self.High = list(self.graphData['high'])
        self.Low.sort()
        self.High.sort(reverse = True)
        self.Save = False

    # 0.minute1, 1.minute3, 2.minute5, 3.minute10, 4.minute15, 5.minute30, 6.minute60, 7.minute240, 8.day, 9.week, 10.month
    def setInterval(self, cnt=8):
        self.interval = Bitcoin.intervalTable[cnt]
        self.chartData = list(pyupbit.get_ohlcv(self.ticker, interval=self.interval)['close'])

    def getPrice(self):
        return pyupbit.get_current_price(self.ticker)

    def getLow(self):
        return self.Low[0]

    def getHigh(self):
        return self.High[0]

    def getGraphData(self):
        return list(self.graphData['close'])


class AutoStockTrade():
    def __init__(self, coin, price, per, balance, log):
        self.coin = coin
        self.price = price
        self.per = per
        self.balance = balance
        self.log = log
        self.buyOrder = None
        self.sellOrder = None

        self.buy = False
        print(self.price * self.per * 0.01)

    def Update(self):
        if self.buyOrder == None and not self.buy:
            self.BuyOrder()

        if self.SellOrder != None and self.buy:
            if self.coin.getPrice() > self.price + (self.price * self.per * 0.01):
                print(self.price * self.per * 0.01)
                self.SellOrder()
        
    def Update(self):
        if self.GetChejanData(913) == '체결' and not self.buy:
            self.buy = True
            self.log.AddStockLog(self.stock.name + " 체결량 " + self.GetChejanData(911) + " 체결가 " + self.GetChejanData(910) + " 구매 완료")
        elif self.GetChejanData(913) == '체결' and self.buy:
            self.buy = False
            self.log.AddStockLog(self.stock.name + " 체결량 " + self.GetChejanData(911) + " 체결가 " + self.GetChejanData(910) + " 판매 완료")

    def BuyOrder(self):
        if StockInfo.KIWOOM.SendOrder("주문주문", "0101", StockInfo.accno, 1, self.stock.code, self.balance//self.price, self.price, "00", ""):
            self.log.AddStockLog(self.stock.name + " 주문 실패")
        pass

    def SellOrder(self):
        if StockInfo.KIWOOM.SendOrder("주문주문", "0101", StockInfo.accno, 2, self.stock.code, self.balance//self.price, self.price + (self.price * (self.per/100)), "00", ""):
            self.log.AddStockLog(self.stock.name + " 주문 실패")
        pass