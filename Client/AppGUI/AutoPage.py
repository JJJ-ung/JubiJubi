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
        # 리스트, 현재는 이름만 담는데 클래스 만들었으면 밑에 것들 수정해야댐 검색으로 찾으면 몇개 없을것임
        self.AutoCoin = list()
        self.AutoStock = list()

        # 현재선택된놈의인덱스, get쓰면 int로 받아와짐
        self.BitcoinIndex = IntVar()
        self.StockIndex = IntVar()

        self.Frames = dict()
        self.Widgets = dict()
        W = self.Widgets

        self.FontMain = tkinter.font.Font(family='나눔스퀘어', size=10, weight='bold')
        self.Allin = tkinter.font.Font(family='나눔스퀘어', size=6, weight='bold')
        self.FontSub = tkinter.font.Font(family='나눔스퀘어', size=10, weight='normal')

        self.Frames['Coin'] = UIMaker.PackFix(Frame(parent, width=481, bg=Col_Main, bd=0), LEFT, Y, False)
        self.Frames['Stock'] = UIMaker.PackFix(Frame(parent, width=481, bg=Col_Main, bd=0), RIGHT, Y, False)

        P = self.Frames['Coin']
        W['CoinLogo'] = Label(P, height=60, bg=Col_Title, bd=0, image=IL.Get('bitcoin'))
        W['CoinLogo'].pack(side=TOP, fill=X)

        for i in range(0, 3):
            Col = Col_Main
            if i % 2 == 1: Col = Col_Sub
            Pa = self.Frames['CoinLst' + str(i)] = UIMaker.PackFix(Frame(P, height=40, bg=Col), TOP, X, False)
            W['CoinRadio' + str(i)] = Radiobutton(Pa, image=IL.Get('bookmark'),
                                                  selectimage=IL.Get('bookmarksel'), value=i,
                                                  variable=self.BitcoinIndex,
                                                  bg=Col, activebackground=Col, selectcolor=Col, bd=0, indicatoron=0,
                                                  command = self.SelCoin)
            W['CoinLabel' + str(i)] = Label(Pa, font=self.FontSub, bg=Col, fg='white', bd=0)
        Pa = self.Frames['CoinText'] = UIMaker.PackFix(Frame(P, height=300, bg='yellow'), TOP, X, False)

        self.CoinLog = Text(Pa, bg=Col_Sub, bd=0, fg='white', padx=20, pady=15, font=self.FontSub)  #
        self.CoinLog.bind("<Key>", lambda e: "break")
        self.CoinLog.pack(side=TOP)
        self.CoinLog.insert(CURRENT, '▶ 비트코인 자동매매 로그\n\n')

        Pa = self.Frames['CoinFunc'] = UIMaker.PackFix(Frame(P, bg=Col_Title, bd=0), TOP, BOTH, True)
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
        W['CoinJangoEntry'] = Label(Pa, bg= Col_Title, bd = 0,font = self.FontMain, fg = 'white', width = 40, anchor="w")
        W['CoinJangoEntry'].place(relx = 0.36, rely = 0.15, anchor = 'w')
        W['CoinHandoEntry'] = Entry(Pa, bd = 0, textvariable = self.CoinHando, width = 40)
        W['CoinHandoEntry'].place(relx = 0.36, rely = 0.3, anchor = 'w')
        W['CoinPercentEntry'] = Entry(Pa, bd = 0, textvariable = self.CoinPercent, width = 40)
        W['CoinPercentEntry'].place(relx = 0.36, rely = 0.5, anchor = 'w')
        W['CoinPriceEntry'] = Entry(Pa, bd = 0, textvariable = self.CoinPrice, width = 40)
        W['CoinPriceEntry'].place(relx = 0.36 , rely = 0.65, anchor = 'w')

        W['CoinSetButton'] = Button(Pa, bd=0, text='설정완료', bg=Col_Main, fg='white', font=self.FontMain,
                                    command=self.SetCoin)
        W['CoinSetButton'].place(relx=0.5, rely=0.85, anchor=CENTER)

        P = self.Frames['Stock']
        W['StockLogo'] = Label(P, height=60, bg=Col_Title, bd=0, image=IL.Get('stock'))
        W['StockLogo'].pack(side=TOP, fill=X)

        for i in range(0, 3):
            Col = Col_Main
            if i % 2 == 1: Col = Col_Sub
            Pa = self.Frames['StockLst' + str(i)] = UIMaker.PackFix(Frame(P, height=40, bg=Col), TOP, X, False)
            W['StockRadio' + str(i)] = Radiobutton(Pa, image=IL.Get('bookmark'),
                                                   selectimage=IL.Get('bookmarksel'), value=i,
                                                   variable=self.StockIndex,
                                                   bg=Col, activebackground=Col, selectcolor=Col, bd=0, indicatoron=0,  
                                                   command = self.SelStock)
            W['StockLabel' + str(i)] = Label(Pa, font=self.FontSub, bg=Col, fg='white', bd=0)

        Pa = self.Frames['StockText'] = UIMaker.PackFix(Frame(P, height=300, bg='yellow'), TOP, X, False)

        self.StockLog = Text(Pa, bg=Col_Sub, bd=0, fg='white', padx=20, pady=15, font=self.FontSub)  #
        self.StockLog.bind("<Key>", lambda e: "break")
        self.StockLog.pack(side=TOP)
        self.StockLog.insert(CURRENT, '▶ 주식 자동매매 로그\n\n')

        Pa = self.Frames['StockFunc'] = UIMaker.PackFix(Frame(P, bg=Col_Title, bd=0), TOP, BOTH, True)
        W['StockJangoLabel'] = Label(Pa, text = '잔고  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['StockJangoLabel'].place(relx = 0.06, rely = 0.15, anchor = 'w')
        W['StockHandoLabel'] = Label(Pa, text = '구매한도  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['StockHandoLabel'].place(relx = 0.06, rely = 0.3, anchor = 'w')
        W['StockPercentLabel'] = Label(Pa, text = '수익률  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['StockPercentLabel'].place(relx = 0.06, rely = 0.5, anchor = 'w')
        W['StockPriceLabel'] = Label(Pa, text = '구매가격  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['StockPriceLabel'].place(relx = 0.06, rely = 0.65, anchor = 'w')
        W['SPriceLabel'] = Label(Pa, text = '설정하지 않을 시, 남은 잔고를 올인합니다', font = self.Allin, bg = Col_Title, fg = 'white', bd = 0)
        W['SPriceLabel'].place(relx = 0.06, rely = 0.38, anchor = 'w')

        self.StockJango = StringVar()
        self.StockHando = StringVar()
        self.StockPercent = StringVar()
        self.StockPrice = StringVar()
        W['StockJangoEntry'] = Label(Pa, bg=Col_Title, bd=0, font = self.FontMain, fg = 'white', width=40, anchor="w")
        W['StockJangoEntry'].place(relx=0.36, rely=0.15, anchor='w')
        W['StockHandoEntry'] = Entry(Pa, bd=0, textvariable=self.StockHando, width=40)
        W['StockHandoEntry'].place(relx=0.36, rely=0.3, anchor='w')
        W['StockPercentEntry'] = Entry(Pa, bd=0, textvariable=self.StockPercent, width=40)
        W['StockPercentEntry'].place(relx=0.36, rely=0.5, anchor='w')
        W['StockPriceEntry'] = Entry(Pa, bd=0, textvariable=self.StockPrice, width=40)
        W['StockPriceEntry'].place(relx=0.36, rely=0.65, anchor='w')

        W['StockSetButton'] = Button(Pa, bd=0, text='설정완료', bg=Col_Main, fg='white', font=self.FontMain,
                                    command=self.SetStock)
        W['StockSetButton'].place(relx=0.5, rely=0.85, anchor=CENTER)
        
    def SetCoinBalance(self):
        if Bitcoin.CoinInfo.acount != None:
            print(Bitcoin.CoinInfo.getBalance())
            self.Widgets['CoinJangoEntry']['text'] = Bitcoin.CoinInfo.getBalance()

    def SetCoin(self):
        if Bitcoin.CoinInfo.acount != None:
            Jango = self.Widgets['CoinJangoEntry']['text']
            if self.CoinHando.get() == "":
                Hando = Jango-1
            else:
                Hando = int(self.CoinHando.get())
            Percent = float(self.CoinPercent.get())
            Price = int(self.CoinPrice.get())
            # 이게 entry 값들이니 알아서 사용

            self.AddCoinLog('옵션 설정 완료\n')
            self.AddCoinLog('- 잔고 : ' + str(Jango))
            self.AddCoinLog('- 한도 : ' + str(Hando))
            self.AddCoinLog('- 수익률 : ' + str(Percent))
            self.AddCoinLog('- 구매가격 : ' + str(Price) + '\n')

            print(Hando)

            self.AutoCoin[self.BitcoinIndex.get()].Setting(Price, Percent, Hando, self)

    def SetStockBalance(self):
        if Stock.StockInfo.login:
            self.Widgets['StockJangoEntry']['text'] = Stock.StockInfo.getBalance()

    def SetStock(self):
        if Stock.StockInfo.login:
            Jango = self.Widgets['StockJangoEntry']['text']
            if self.StockHando.get() == "":
                Hando = Jango
            else:
                Hando = int(self.StockHando.get())
            Percent = float(self.StockPercent.get())
            Price = int(self.StockPrice.get())
            # 이게 entry 값들이니 알아서 사용

            self.AddStockLog('옵션 설정 완료\n')
            self.AddStockLog('- 잔고 : ' + str(Jango))
            self.AddStockLog('- 한도 : ' + str(Hando))
            self.AddStockLog('- 수익률 : ' + str(Percent) + "%")
            self.AddStockLog('- 구매가격 : ' + str(Price) + '\n')

            self.AutoStock[self.StockIndex.get()].Setting(Price, Percent, Hando, self)
    def AddCoinLog(self, message):
        # 로그에 한줄 추가하는거
        self.CoinLog.insert(CURRENT, message + '\n')

    def AddStockLog(self, message):
        # 로그에 한줄 추가하는거
        self.StockLog.insert(CURRENT, message + '\n')

    def Add(self, tag, name):
        if tag == 'bitcoin':
            if len(self.AutoCoin) > 2:
                return
            # 중복검사
            for var in self.AutoCoin:
                if var.koreanName == name:
                    return
            index = len(self.AutoCoin)
            self.AutoCoin.append(Bitcoin.AutoCoinTrade(Bitcoin.Bitcoin(Bitcoin.CoinInfo.SearchCoin(name))))
            self.Widgets['CoinLabel' + str(index)].configure(text=name)
            self.Widgets['CoinLabel' + str(index)].place(relx = 0.1, rely = 0.5, anchor = W)
            self.Widgets['CoinRadio' + str(index)].place(relx = 0.05, rely = 0.5, anchor = W)

        if tag == 'stock':
            if len(self.AutoStock) > 2:
                return
            for var in self.AutoStock:
                if var == name:
                    return
            index = len(self.AutoStock)
            self.AutoStock.append(Stock.AutoStockTrade(Stock.Stock(Stock.StockInfo.SearchStock(name))))
            self.Widgets['StockLabel' + str(index)].configure(text=name)
            self.Widgets['StockLabel' + str(index)].place(relx = 0.1, rely = 0.5, anchor = W)
            self.Widgets['StockRadio' + str(index)].place(relx = 0.05, rely = 0.5, anchor = W)

    def Delete(self, tag, name):
        #if self.Find(tag, name) is False :
        #    return
        if tag == 'bitcoin':
            index = 0
            for var in self.AutoCoin:
                if var.coin.koreanName == name :
                    break
                ++index
            #index = self.AutoCoin.index(name)
            del self.AutoCoin[index]
            self.Widgets['CoinRadio'+str(len(self.AutoCoin))].place_forget()
            self.Widgets['CoinLabel' + str(len(self.AutoCoin))].place_forget()
            for i in range(index, len(self.AutoCoin)):
                self.Widgets['CoinLabel' + str(i)].configure(text=self.AutoCoin[i])
        if tag == 'stock':
            index = self.AutoStock.index(name)
            del self.AutoStock[index]
            self.Widgets['StockRadio'+str(len(self.AutoStock))].place_forget()
            self.Widgets['StockLabel' + str(len(self.AutoStock))].place_forget()
            for i in range(index, len(self.AutoStock)):
                self.Widgets['StockLabel' + str(i)].configure(text=self.AutoStock[i])

    def Find(self, tag, name):
        if tag == 'bitcoin':
            L = self.AutoCoin
            for var in L :
                if var.coin.koreanName == name :
                    return True
        if tag == 'stock':
            L = self.AutoStock
            for var in L :
                if var == name :
                    return True
        return False

    def Update(self):
        for coin in self.AutoCoin:
            coin.Update()
        for stock in self.AutoStock:
            stock.Update()
        self.SetCoinBalance()
        self.SetStockBalance()

    def SelCoin(self):
        # 옆에 버튼 눌렀을때 밑에 옵션 뜨도록 하는 기능들
        self.AddCoinLog(self.AutoCoin[self.BitcoinIndex.get()].coin.koreanName)

    def SelStock(self):
        # 옆에 버튼 눌렀을때 밑에 옵션 뜨도록 하는 기능들
        self.AddStockLog(self.AutoStock[self.StockIndex.get()].stock.name)