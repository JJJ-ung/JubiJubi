#from pykiwoom.kiwoom import *

#KIWOOM = Kiwoom()
#KIWOOM.CommConnect(block=True)

#class StockInfo():
#    kospi = KIWOOM.GetCodeListByMarket('0')
#    kosdaq = KIWOOM.GetCodeListByMarket('10')
#    etf = KIWOOM.GetCodeListByMarket('8')

#    Code2Name = {}
#    Name2Code = {}

#    for code in kospi:
#        Code2Name[code] = KIWOOM.GetMasterCodeName(code)
#        Name2Code[Code2Name[code]] = code
#    for code in kosdaq:
#        Code2Name[code] = KIWOOM.GetMasterCodeName(code)
#        Name2Code[Code2Name[code]] = code
#    for code in etf:
#        Code2Name[code] = KIWOOM.GetMasterCodeName(code)
#        Name2Code[Code2Name[code]] = code

#    def SearchStock(str):
#        if str in StockInfo.Name2Code:
#            return [StockInfo.Name2Code[str], str]
        
#        if str in StockInfo.Code2Name:
#            return [str, StockInfo.Code2Name[str]]

#class Stock():
#    def __init__(self, info):
#        self.code = info[0]
#        self.name = info[1]

#    def getPrice(self):
#        return int(KIWOOM.block_request("opt10001", 종목코드=self.code, output="주식기본정보", next=0)['기준가'])
