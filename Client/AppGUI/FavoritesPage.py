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


class Info:
    def __init__(self, name, ticker):
        self.Name = name
        self.Ticker = ticker

class Page:
    def Add(self, tag, item):
        if tag == 'bitcoin':
            if len(self.BitcoinFav) > 14:
                return
            info = Info(item.koreanName, item.ticker)
            if self.Find(tag, info.Ticker):
                return
            index = len(self.BitcoinFav)
            self.BitcoinFav.append(info)
            self.Widgets['Bitcoin']['Label' + str(index)].configure(text=info.Name + '  ' + info.Ticker)
            self.Widgets['Bitcoin']['Radio' + str(index)].place(relx=0.05, rely=0.5, anchor=W)
            self.Widgets['Bitcoin']['Label' + str(index)].place(relx=0.15, rely=0.5, anchor=W)
        if tag == 'stock':
            if len(self.StockFav) > 14:
                return
            info = Info(item.name, item.code)
            if self.Find(tag, info.Ticker):
                return
            index = len(self.StockFav)
            self.StockFav.append(info)
            self.Widgets['Stock']['Label' + str(index)].configure(text=info.Name + '  ' + info.Ticker)
            self.Widgets['Stock']['Radio' + str(index)].place(relx=0.05, rely=0.5, anchor=W)
            self.Widgets['Stock']['Label' + str(index)].place(relx=0.15, rely=0.5, anchor=W)

        self.MainUI.Pages['profile'].SetTelegram(self)
    def Delete(self, tag, ticker):
        if tag == 'bitcoin':
            L = self.BitcoinFav
            D = self.Widgets['Bitcoin']
        if tag == 'stock':
            L = self.StockFav
            D = self.Widgets['Stock']
        if not self.Find(tag, ticker): return
        index = -1
        for i in range(0, len(L)):
            if L[i].Ticker == ticker:
                index = i
                break
        if index is -1: return
        del L[index]
        D['Radio' + str(len(L))].place_forget()
        D['Label' + str(len(L))].place_forget()
        for i in range(index, len(L)):
            D['Label' + str(i)].configure(text=L[i].Name + '  ' + L[i].Ticker)

        self.MainUI.Pages['profile'].SetTelegram(self)
    def Find(self, tag, ticker):
        if tag is 'bitcoin':
            for var in self.BitcoinFav:
                if var.Ticker == ticker:
                    return True
            return False
        if tag is 'stock':
            for var in self.StockFav:
                if var.Ticker == ticker:
                    return True
            return False

    def __init__(self, parent, IL, mainUI):
        self.IL = IL
        self.MainUI = mainUI
        self.BitcoinFav = list()
        self.StockFav = list()

        self.BitcoinIndex = IntVar()
        self.StockIndex = IntVar()

        self.FontMain = tkinter.font.Font(family='나눔스퀘어', size=12, weight='bold')
        self.FontSub = tkinter.font.Font(family='나눔스퀘어', size=12, weight='normal')

        self.Frames = dict()
        self.BitcoinFrame = UIMaker.PackFix(Frame(parent, width=481, bg=Col_Main), LEFT, Y, False)
        self.StockFrame = UIMaker.PackFix(Frame(parent, width=481, bg=Col_Main), RIGHT, Y, False)

        self.Widgets = {'Bitcoin': dict(), 'Stock': dict(), 'Title': dict()}
        self.Widgets['Title']['Bitcoin'] = Label(self.BitcoinFrame, height=60, image=self.IL.Get('bitcoin'),
                                                 bg=Col_Title, bd=0)
        self.Widgets['Title']['Bitcoin'].pack(side=TOP, fill=X)
        self.Widgets['Title']['Stock'] = Label(self.StockFrame, height=60, image=self.IL.Get('stock'), bg=Col_Title,
                                               bd=0)
        self.Widgets['Title']['Stock'].pack(side=TOP, fill=X)

        self.Setup('Bitcoin', self.BitcoinFrame, self.Widgets['Bitcoin'])
        self.Setup('Stock', self.StockFrame, self.Widgets['Stock'])

        self.LoadCoin()
        self.LoadStock()
    def Setup(self, type, P, D):
        MenuFrame = UIMaker.PackFix(Frame(P, width=481, height=77, bg=Col_Title), BOTTOM, NONE, False)
        if type == 'Bitcoin':
            Button(MenuFrame, text='  저장', font=self.FontMain, width=100, height=30, bd=0, highlightthickness=0,
                   activebackground=Col_Title,
                   bg=Col_Title, fg='white', activeforeground=Col_red, image=self.IL.Get('favorites_on'),
                   compound=LEFT, command = lambda : self.SaveCoin()).pack(side=LEFT)
        if type == 'Stock':
            Button(MenuFrame, text='  저장', font=self.FontMain, width=100, height=30, bd=0, highlightthickness=0,
                   activebackground=Col_Title,
                   bg=Col_Title, fg='white', activeforeground=Col_red, image=self.IL.Get('favorites_on'),
                   compound=LEFT, command = lambda : self.SaveStock()).pack(side=LEFT)
        for i in range(0, 15):
            Col = Col_Main
            if i % 2 == 1: Col = Col_Sub
            Pa = self.Frames[type + str(i)] = UIMaker.PackFix(Frame(P, height=38, bg=Col), TOP, X, False)
            if type == 'Bitcoin':
                D['Radio' + str(i)] = Radiobutton(Pa, image=self.IL.Get('bookmark'),
                                                  selectimage=self.IL.Get('bookmarksel'), value=i,
                                                  variable=self.BitcoinIndex,
                                                  bg=Col, activebackground=Col, selectcolor=Col, bd=0, indicatoron=0,
                                                  command=lambda: self.SetCoin())
            if type == 'Stock':
                D['Radio' + str(i)] = Radiobutton(Pa, image=self.IL.Get('bookmark'),
                                                  selectimage=self.IL.Get('bookmarksel'), value=i,
                                                  variable=self.StockIndex,
                                                  bg=Col, activebackground=Col, selectcolor=Col, bd=0, indicatoron=0,
                                                  command=lambda: self.SetStock())
            D['Label' + str(i)] = Label(Pa, font=self.FontSub, bg=Col, fg='white', bd=0)

    def SetCoin(self):
        Coin = self.BitcoinFav[self.BitcoinIndex.get()]
        CoinPage = self.MainUI.Pages['bitcoin']
        result = Bitcoin.CoinInfo.SearchCoin(Coin.Ticker)
        if result is not None:
            CurrCoin = Bitcoin.Bitcoin(result)
            CoinPage.SetCurr(CurrCoin)

    def SetStock(self):
        st = self.StockFav[self.StockIndex.get()]
        StockPage = self.MainUI.Pages['stock']
        result = Stock.StockInfo.SearchStock(st.Ticker)
        if result is not None:
            CurrStock = Stock.Stock(result)
            StockPage.SetCurr(CurrStock)

    def SaveCoin(self):
        f = open('비트코인즐찾.txt', 'w')
        for var in self.BitcoinFav :
            f.write(var.Name+'\n'+var.Ticker+'\n')
        f.close()

    def SaveStock(self):
        f = open('주식즐찾.txt', 'w')
        for var in self.StockFav :
            f.write(var.Name+'\n'+var.Ticker+'\n')
        f.close()

    def LoadCoin(self):
        f = open('비트코인즐찾.txt', 'r')
        while True:
            Name = f.readline()
            Ticker = f.readline()
            if not Name or not Ticker : break
            info = Info(Name.strip(), Ticker.strip())
            index = len(self.BitcoinFav)
            self.BitcoinFav.append(info)
            self.Widgets['Bitcoin']['Label' + str(index)].configure(text=info.Name + '  ' + info.Ticker)
            self.Widgets['Bitcoin']['Radio' + str(index)].place(relx=0.05, rely=0.5, anchor=W)
            self.Widgets['Bitcoin']['Label' + str(index)].place(relx=0.15, rely=0.5, anchor=W)
        f.close()

    def LoadStock(self):
        f = open('주식즐찾.txt', 'r')
        while True:
            Name = f.readline()
            Ticker = f.readline()
            if not Name or not Ticker : break
            info = Info(Name.strip(), Ticker.strip())
            index = len(self.StockFav)
            self.StockFav.append(info)
            self.Widgets['Stock']['Label' + str(index)].configure(text=info.Name + '  ' + info.Ticker)
            self.Widgets['Stock']['Radio' + str(index)].place(relx=0.05, rely=0.5, anchor=W)
            self.Widgets['Stock']['Label' + str(index)].place(relx=0.15, rely=0.5, anchor=W)
        f.close()
