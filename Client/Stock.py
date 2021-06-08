from pykiwoom.kiwoom import *
import datetime


class StockInfo(): 
    KIWOOM = None
    kospi = None
    kosdaq = None
    etf = None
    accno = None

    Code2Name = {}
    Name2Code = {}

    login = False

    def Login():
        if not StockInfo.login:
            StockInfo.KIWOOM = Kiwoom()
            StockInfo.KIWOOM.CommConnect()
            print("Login success")
            StockInfo.login = True

            StockInfo.accno = int(StockInfo.KIWOOM.GetLoginInfo("ACCNO")[0])

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

    def getBalance():
        return int(StockInfo.KIWOOM.block_request("opw00001", 계좌번호=StockInfo.accno, next=1, output="예수금상세현황")['출금가능금액'])

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

        self.Save = False

    def Refresh(self):
        df = StockInfo.KIWOOM.block_request("opt10082", 종목코드=self.code, 기준일자=time.strftime('%Y%m%d', time.localtime(time.time())), 수정주가구분=30, next=0, output="주식차트조회")
        
        dailyData = StockInfo.KIWOOM.block_request("opt10081", 종목코드=self.code, 기준일자=time.strftime('%Y%m%d', time.localtime(time.time())), 수정주가구분=1, next=0, output="주식차트조회")
        
        self.lstDailyData = [int(list(dailyData['현재가'])[i]) for i in range(6, 0, -1)] # 종가
        self.lstDailyVolume = [int(list(dailyData['거래량'])[i]) for i in range(6, 0, -1)] # 거래량
        self.lstDailyMarketPrice = [int(list(dailyData['시가'])[i]) for i in range(6, 0, -1)] # 시가

        self.graphDataDay = [int(list(dailyData['현재가'])[i]) for i in range(0, 100)]
        self.graphDataWeek = [abs(int(list(df['현재가'])[i])) for i in range(0, 100)]
        self.Low = list(df['저가'])[0:6]
        self.High = list(df['고가'])[0:6]

    def setInterval(self, type, cnt):
        if type == 1:
            interval = 1
            self.type = "opt10081"
        elif type == 2:
            interval = cnt
            self.type = "opt10080"
        self.Refresh()

    def getPrice(self):
        cur = int(StockInfo.KIWOOM.block_request("opt10003", 종목코드=self.code, output="주식기본정보", next=0)['현재가'][0][1:])
        return cur
        
    def getLow(self):
        return int(self.Low[0])

    def gethigh(self):
        return int(self.High[0])

class AutoStockTrade():
    def __init__(self, stock):
        self.stock = stock
        self.price = None
        self.per = None
        self.balance = None
        self.log = None

        self.buy = False
        self.order = False

        StockInfo.KIWOOM.ocx.OnReceiveChejanData.connect(self._handler_chejan)

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
                if self.stock.getPrice() > self.price + (self.price * self.per * 0.01):
                    self.order = True
                    self.SellOrder()
            
    def _handler_chejan(self, gubun, item_cnt, fid_list):
        if self.GetChejanData(913) == '체결' and not self.buy:
            self.buy = True
            self.order = False
            self.log.AddStockLog(self.stock.name + " 체결량 " + self.GetChejanData(911) + " 체결가 " + self.GetChejanData(910) + " 구매 완료")
        elif self.GetChejanData(913) == '체결' and self.buy:
            self.buy = False
            self.order = False
            self.log.AddStockLog(self.stock.name + " 체결량 " + self.GetChejanData(911) + " 체결가 " + self.GetChejanData(910) + " 판매 완료")
        
    def GetChejanData(self, fid):
        data = StockInfo.KIWOOM.ocx.dynamicCall("GetChejanData(int)", fid)
        return data

    def BuyOrder(self):
        if StockInfo.KIWOOM.SendOrder("주문주문", "0101", StockInfo.accno, 1, self.stock.code, self.balance//self.price, self.price, "00", ""):
            self.log.AddStockLog(self.stock.name + " 주문 실패")
        else:
            self.order = False

    def SellOrder(self):
        if StockInfo.KIWOOM.SendOrder("주문주문", "0101", StockInfo.accno, 2, self.stock.code, self.balance//self.price, self.price + (self.price * (self.per/100)), "00", ""):
            self.log.AddStockLog(self.stock.name + " 주문 실패")
        else:
            self.order = False