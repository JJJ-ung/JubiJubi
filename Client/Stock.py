from pykiwoom.kiwoom import *
import datetime


class StockInfo(): 
    KIWOOM = None
    kospi = None
    kosdaq = None
    etf = None

    Code2Name = {}
    Name2Code = {}

    login = False

    def Login():
        StockInfo.KIWOOM = Kiwoom()
        StockInfo.KIWOOM.CommConnect(block=True)
        StockInfo.login = True
        print("Login success")

        StockInfo.kospi = StockInfo.KIWOOM.GetCodeListByMarket('0')
        StockInfo.kosdaq = StockInfo.KIWOOM.GetCodeListByMarket('10')
        StockInfo.etf = StockInfo.KIWOOM.GetCodeListByMarket('8')
        
        for code in StockInfo.kospi:
            StockInfo.Code2Name[code] = StockInfo.KIWOOM.GetMasterCodeName(code)
            StockInfo.Name2Code[StockInfo.Code2Name[code]] = code
        for code in StockInfo.kosdaq:
            StockInfo.Code2Name[code] = StockInfo.KIWOOM.GetMasterCodeName(code)
            StockInfo.Name2Code[StockInfo.Code2Name[code]] = code
        for code in StockInfo.etf:
            StockInfo.Code2Name[code] = StockInfo.KIWOOM.GetMasterCodeName(code)
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
        df = StockInfo.KIWOOM.block_request(self.type, 종목코드=self.code, 기준일자=time.strftime('%Y%m%d', time.localtime(time.time())), 수정주가구분=self.interval, next=0, output="주식차트조회")
        
        dailyData = StockInfo.KIWOOM.block_request("opt10081", 종목코드=self.code, 기준일자=time.strftime('%Y%m%d', time.localtime(time.time())), 수정주가구분=1, next=0, output="주식차트조회")
        
        self.lstDailyData = df['전일종가'][0] # 종가
        self.lstDailyVolume = dailyData['거래량'][0] # 거래량
        self.lstDailyMarketPrice = dailyData['시가'][0] # 시가

        print(self.lstDailyData, self.lstDailyMarketPrice, self.lstDailyVolume)

        self.graphData = list(df['현재가'])[0:200]
        self.Low = list(df['저가'])[0:200]
        self.High = list(df['고가'])[0:200]

    def setInterval(self, type, cnt):
        if type == 1:
            interval = 1
            self.type = "opt10081"
        elif type == 2:
            interval = cnt
            self.type = "opt10080"
        self.Refresh()

    def getPrice(self):
        return int(StockInfo.KIWOOM.block_request("opt10001", 종목코드=self.code, output="주식기본정보", next=0)['기준가'])

    def getLow(self):
        return self.Low[0]

    def gethigh(self):
        return self.High[0]

    def gethigh(self):
        return self.graphData[0]
