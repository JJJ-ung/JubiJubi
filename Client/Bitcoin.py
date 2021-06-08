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
            CoinInfo.acount = pyupbit.Upbit(CoinInfo.accessKey, CoinInfo.secretKey)
            if CoinInfo.acount.get_balance() == None:
                CoinInfo.acount = None
                print("Login Error")
            else:
                print("Login success")

    def SearchCoin(str):
        for coin in CoinInfo.data:
            if coin['market'].startswith("KRW"):
                if coin['market'].lower().endswith(str.lower()) or coin['korean_name'] == str or coin['english_name'].lower() == str.lower():
                    return coin

    def getBalance():
        return int(CoinInfo.acount.get_balance())

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

class AutoCoinTrade():
    def __init__(self, coin):
        self.coin = coin
        self.price = None
        self.per = None
        self.balance = None
        self.log = None

        self.UUID = None

        self.buy = False
        self.order = False

    def Setting(self, price, per, balance, log):
        self.price = price
        self.per = per
        self.balance = balance
        self.log = log
        
    def Update(self):
        if self.price != None:
            if not self.order and not self.buy:
                self.BuyOrder()
            elif not self.order and self.buy:
                self.SellOrder()

            if self.UUID != None:
                Response = CoinInfo.acount.get_individual_order(self.UUID)
                if Response['state'] == 'done' and not self.buy:
                    self.buy = True
                    self.order = False
                    self.UUID = None
                    self.log.AddCoinLog(self.coin.koreanName + " 체결량 " + Response['volume'] + " 체결가 " + Response['price'] + " 매수 완료")
                elif Response['state'] == 'done' and self.buy:
                    self.buy = False
                    self.order = False
                    self.UUID = None
                    self.log.AddCoinLog(self.coin.koreanName + " 체결량 " + Response['volume'] + " 체결가 " + Response['price'] + " 매도 완료")

    def BuyOrder(self):
        tr = CoinInfo.acount.buy_limit_order(self.coin.ticker, self.price, self.balance/self.price)
        if tr.get('error') != None:
            self.log.AddCoinLog(self.coin.koreanName + " 주문 실패")
            print(tr)
            self.UUID=None
        else:
            self.order = True
            self.UUID = tr['uuid']
            self.log.AddCoinLog(self.coin.koreanName + " 매수 주문 성공")


    def SellOrder(self):
        tr = CoinInfo.acount.sell_limit_order(self.coin.ticker, self.price + round(self.price * 0.01 * self.per), self.balance/self.price)
        print(self.price + self.price * 0.01 * self.per)
        if tr.get('error') != None:
            self.log.AddCoinLog(self.coin.koreanName + " 주문 실패")
            print(tr)
            self.UUID=None
        else:
            self.order = True
            self.UUID = tr['uuid']
            self.log.AddCoinLog(self.coin.koreanName + " 매도 주문 성공")
