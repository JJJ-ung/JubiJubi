import sys
from tkinter import *
import tkinter.font
from . import UIMaker
from . import ImageLoader
sys.path.append('/Bitcoin.py')
import Bitcoin
sys.path.append('/Stock.py')
import Stock

Col_Title = '#4e4e4e'
Col_Main = '#333333'
Col_Sub = '#393939'
Col_red = '#eb6148'
Col_blue = '#008dd2'

class Page:
    def __init__(self, parent, IL):
        self.Frames = dict()
        self.Widgets = dict()
        W = self.Widgets

        self.FontMain = tkinter.font.Font(family='나눔스퀘어', size=10, weight='bold')
        self.Allin = tkinter.font.Font(family='나눔스퀘어', size=6, weight='bold')
        self.FontSub = tkinter.font.Font(family='나눔스퀘어', size=10, weight='normal')

        self.Frames['Coin'] = UIMaker.PackFix(Frame(parent, width = 481, bg = Col_Main, bd = 0), LEFT, Y, False)
        self.Frames['Stock'] = UIMaker.PackFix(Frame(parent, width = 481, bg = Col_Main, bd = 0), RIGHT, Y, False)

        P = self.Frames['Coin']
        W['CoinLogo'] = Label(P, height = 60, bg = Col_Title, bd = 0, image = IL.Get('bitcoin'))
        W['CoinLogo'].pack(side = TOP, fill = X)

        for i in range(0, 3):
            Col = Col_Main
            if i % 2 == 1 : Col = Col_Sub
            self.Frames['CoinLst'+str(i)] = UIMaker.PackFix(Frame(P, height = 40, bg = Col), TOP, X, False)
        Pa = self.Frames['CoinText'] = UIMaker.PackFix(Frame(P, height = 300, bg = 'yellow'), TOP, X, False)

        self.CoinLog = Text(Pa, bg = Col_Sub, bd = 0, fg = 'white', padx = 20, pady = 15, font = self.FontSub)#
        self.CoinLog.bind("<Key>", lambda e: "break")
        self.CoinLog.pack(side = TOP)
        self.CoinLog.insert(CURRENT, '▶ 비트코인 자동매매 로그\n\n')
        
        Pa = self.Frames['CoinFunc'] = UIMaker.PackFix(Frame(P, bg = Col_Title, bd = 0), TOP, BOTH, True)
        W['CoinJangoLabel'] = Label(Pa, text = '잔고  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['CoinJangoLabel'].place(relx = 0.06, rely = 0.15, anchor = 'w')
        W['CoinHandoLabel'] = Label(Pa, text = '구매한도  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['CoinHandoLabel'].place(relx = 0.06, rely = 0.3, anchor = 'w')
        W['CoinPercentLabel'] = Label(Pa, text = '수익률  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['CoinPercentLabel'].place(relx = 0.06, rely = 0.5, anchor = 'w')
        W['CoinPriceLabel'] = Label(Pa, text = '구매가격  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['CoinPriceLabel'].place(relx = 0.06, rely = 0.65, anchor = 'w')
        W['CPriceLabel'] = Label(Pa, text = '설정하지 않을 시, 남은 잔고를 올인합니다', font = self.Allin, bg = Col_Title, fg = 'white', bd = 0)
        W['CPriceLabel'].place(relx = 0.06, rely = 0.38, anchor = 'w')

        self.CoinJango = StringVar()
        self.CoinHando = StringVar()
        self.CoinPercent = StringVar()
        self.CoinPrice = StringVar()
        W['CoinJangoEntry'] = Label(Pa, bg= Col_Title, textvariable = self.CoinJango, bd = 0, fg = 'white', width = 40, anchor="w")
        W['CoinJangoEntry'].place(relx = 0.36, rely = 0.15, anchor = 'w')
        W['CoinHandoEntry'] = Entry(Pa, bd = 0, textvariable = self.CoinHando, width = 40)
        W['CoinHandoEntry'].place(relx = 0.36, rely = 0.3, anchor = 'w')
        W['CoinPercentEntry'] = Entry(Pa, bd = 0, textvariable = self.CoinPercent, width = 40)
        W['CoinPercentEntry'].place(relx = 0.36, rely = 0.5, anchor = 'w')
        W['CoinPriceEntry'] = Entry(Pa, bd = 0, textvariable = self.CoinPrice, width = 40)
        W['CoinPriceEntry'].place(relx = 0.36 , rely = 0.65, anchor = 'w')

        W['CoinSetButton'] = Button(Pa, bd = 0, text = '설정완료', bg = Col_Main, fg = 'white', font = self.FontMain, command = self.SetCoin)
        W['CoinSetButton'].place(relx = 0.5, rely = 0.85, anchor = CENTER)

        P = self.Frames['Stock']
        W['StockLogo'] = Label(P, height = 60, bg = Col_Title, bd = 0, image = IL.Get('stock'))
        W['StockLogo'].pack(side = TOP, fill = X)
        
        for i in range(0, 3):
            Col = Col_Main
            if i % 2 == 1 : Col = Col_Sub
            self.Frames['StockLst'+str(i)] = UIMaker.PackFix(Frame(P, height = 40, bg = Col), TOP, X, False)
        Pa = self.Frames['StockText'] = UIMaker.PackFix(Frame(P, height = 300, bg = 'yellow'), TOP, X, False)

        self.StockLog = Text(Pa, bg = Col_Sub, bd = 0, fg = 'white', padx = 20, pady = 15, font = self.FontSub)#
        self.StockLog.bind("<Key>", lambda e: "break")
        self.StockLog.pack(side = TOP)
        self.StockLog.insert(CURRENT, '▶ 주식 자동매매 로그\n\n')

        Pa = self.Frames['StockFunc'] = UIMaker.PackFix(Frame(P, bg = Col_Title, bd = 0), TOP, BOTH, True)
        W['StockJangoLabel'] = Label(Pa, text = '잔고  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['StockJangoLabel'].place(relx = 0.06, rely = 0.1, anchor = 'w')
        W['StockCodeLabel'] = Label(Pa, text = '주식  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['StockCodeLabel'].place(relx = 0.06, rely = 0.25, anchor = 'w')
        W['StockHandoLabel'] = Label(Pa, text = '구매한도  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['StockHandoLabel'].place(relx = 0.06, rely = 0.4, anchor = 'w')
        W['StockPercentLabel'] = Label(Pa, text = '수익률  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['StockPercentLabel'].place(relx = 0.06, rely = 0.55, anchor = 'w')
        W['StockPriceLabel'] = Label(Pa, text = '구매가격  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['StockPriceLabel'].place(relx = 0.06, rely = 0.7, anchor = 'w')
        W['SPriceLabel'] = Label(Pa, text = '설정하지 않을 시, 남은 잔고를 올인합니다', font = self.Allin, bg = Col_Title, fg = 'white', bd = 0)
        W['SPriceLabel'].place(relx = 0.06, rely = 0.46, anchor = 'w')

        self.StockJango = StringVar()
        self.StockHando = StringVar()
        self.StockPercent = StringVar()
        self.StockPrice = StringVar()
        W['StockJangoEntry'] = Label(Pa, bg= Col_Title, textvariable = self.StockJango, bd = 0, fg = 'white', width = 40, anchor="w")
        W['StockJangoEntry'].place(relx = 0.36, rely = 0.1, anchor = 'w')
        W['StockHandoEntry'] = Entry(Pa, bd = 0, textvariable = self.StockHando, width = 40)
        W['StockHandoEntry'].place(relx = 0.36, rely = 0.25, anchor = 'w')
        W['StockHandoEntry'] = Entry(Pa, bd = 0, textvariable = self.StockHando, width = 40)
        W['StockHandoEntry'].place(relx = 0.36, rely = 0.4, anchor = 'w')
        W['StockPercentEntry'] = Entry(Pa, bd = 0, textvariable = self.StockPercent, width = 40)
        W['StockPercentEntry'].place(relx = 0.36, rely = 0.55, anchor = 'w')
        W['StockPriceEntry'] = Entry(Pa, bd = 0, textvariable = self.StockPrice, width = 40)
        W['StockPriceEntry'].place(relx = 0.36 , rely = 0.7, anchor = 'w')

        W['StockSetButton'] = Button(Pa, bd = 0, text = '설정완료', bg = Col_Main, fg = 'white', font = self.FontMain, command = self.SetStock)
        W['StockSetButton'].place(relx = 0.5, rely = 0.9, anchor = CENTER)
        
    def SetCoinBalance(self, balance):
        self.Widgets['CoinJangoEntry']['text'] = balance

    def SetCoin(self):
        Jango = self.Widgets['CoinJangoEntry']['text']
        Hando = int(self.CoinHando.get())
        Percent = int(self.CoinPercent.get())
        Price = int(self.CoinPrice.get())
        # 이게 entry 값들이니 알아서 사용

        self.AddCoinLog('옵션 설정 완료\n')
        self.AddCoinLog('- 잔고 : ' + str(Jango))
        self.AddCoinLog('- 한도 : ' + str(Hando))
        self.AddCoinLog('- 수익률 : ' + str(Percent))
        self.AddCoinLog('- 구매가격 : ' + str(Price) + '\n')

    def AddCoinLog(self, message):
        #로그에 한줄 추가하는거
        self.CoinLog.insert(CURRENT, message + '\n')

    def SetStockBalance(self, balance):
        if Stock.StockInfo.login:
            self.Widgets['StockJangoEntry']['text'] = balance
        
    def SetStock(self):
        if Stock.StockInfo.login:
            Jango = self.Widgets['CoinJangoEntry']['text']
            Hando = int(self.StockHando.get())
            Percent = float(self.StockPercent.get())
            Price = int(self.StockPrice.get())
            # 이게 entry 값들이니 알아서 사용

            self.AddStockLog('옵션 설정 완료\n')
            self.AddStockLog('- 잔고 : ' + str(Jango))
            self.AddStockLog('- 한도 : ' + str(Hando))
            self.AddStockLog('- 수익률 : ' + str(Percent) + "%")
            self.AddStockLog('- 구매가격 : ' + str(Price) + '\n')

            Stock.StockInfo.Auto.append(Stock.AutoStockTrade(Stock.Stock(Stock.StockInfo.SearchStock('삼성전자')), Price, Percent, Hando, self))

    def AddStockLog(self, message):
        #로그에 한줄 추가하는거
        self.StockLog.insert(CURRENT, message + '\n')
