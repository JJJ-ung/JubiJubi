from pykiwoom.kiwoom import *
import datetime

KIWOOM = None

class StockInfo():
    kospi = None
    kosdaq = None
    etf = None

    Code2Name = {}
    Name2Code = {}

    def Login():
        Stock.KIWOOM = Kiwoom()
        Stock.KIWOOM.CommConnect(block=True)
        print("Login success")

        StockInfo.kospi = Stock.KIWOOM.GetCodeListByMarket('0')
        StockInfo.kosdaq = Stock.KIWOOM.GetCodeListByMarket('10')
        StockInfo.etf = Stock.KIWOOM.GetCodeListByMarket('8')
        
        for code in StockInfo.kospi:
            StockInfo.Code2Name[code] = Stock.KIWOOM.GetMasterCodeName(code)
            StockInfo.Name2Code[StockInfo.Code2Name[code]] = code
        for code in StockInfo.kosdaq:
            StockInfo.Code2Name[code] = Stock.KIWOOM.GetMasterCodeName(code)
            StockInfo.Name2Code[StockInfo.Code2Name[code]] = code
        for code in StockInfo.etf:
            StockInfo.Code2Name[code] = Stock.KIWOOM.GetMasterCodeName(code)
            StockInfo.Name2Code[StockInfo.Code2Name[code]] = code

    def SearchStock(str):
        if str in StockInfo.Name2Code:
            return [StockInfo.Name2Code[str], str]
       
        if str in StockInfo.Code2Name:
            return [str, StockInfo.Code2Name[str]]

class Stock():
    def __init__(self, info):
        self.code = info[0]
        self.name = info[1]

        self.type = "opt10081"
        self.interval = 1

        self.lstDailyData = list() # 종가
        self.lstDailyVolume = list() # 거래량
        self.lstDailyMarketPrice = list() # 시가

        self.graphData = list()
        self.Low = list()
        self.High = list()
           
        self.Refresh()

    def Refresh(self):
        self.df = kiwoom.block_request(self.type, 종목코드=self.code, 기준일자=time.strftime('%Y%m%d', time.localtime(time.time())), 수정주가구분=interval, next=0)

    def setInterval(self, type, cnt):
        if type == 1:
            interval = 1
            self.type = "opt10081"
        elif type == 2:
            interval = cnt
            self.type = "opt10080"
        self.Refresh()

    def getPrice(self):
        return int(KIWOOM.block_request("opt10001", 종목코드=self.code, output="주식기본정보", next=0)['기준가'])

    def getLow(self):
        return list(df['저가'])[0:200]

    def gethigh(self):
        return list(df['고가'])[0:200]

    def gethigh(self):
        return list(df['현재가'])[0:200]
