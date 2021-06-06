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
    def Add_Bitcoin(self, coin) :
        if self.Find_Bitcoin(coin) is True:
            return
        coin.Save = True
        self.BitcoinFav.append(coin)
        print(self.BitcoinFav)
        pass

    def Delete_Bitcoin(self, coin):
        print('코인삭제')
        idx = self.BitcoinFav.index(coin)
        print(idx)

    def Find_Bitcoin(self, coin):
        if coin in self.BitcoinFav :
            return True
        return False

    def Add_Stock(self, coin) :
        print('주식추가')
        pass

    def __init__(self, parent, IL):
        self.IL = IL
        self.BitcoinFav = list()
        self.StockFav = list()
        self.StockSel = 0
        self.BitcoinSel = 0

        self.FontMain = tkinter.font.Font(family='나눔스퀘어', size=12, weight='bold')
        self.FontSub = tkinter.font.Font(family='나눔스퀘어', size=12, weight='normal')

        self.Frames = dict()
        self.BitcoinFrame = UIMaker.PackFix(Frame(parent, width = 481, bg = Col_Main), LEFT, Y, False)
        self.StockFrame = UIMaker.PackFix(Frame(parent, width = 481, bg = Col_Main), RIGHT, Y, False)

        self.Widgets = {'Bitcoin' : dict(), 'Stock' : dict(), 'Title' : dict()}
        self.Widgets['Title']['Bitcoin'] = Label(self.BitcoinFrame, height = 60, image = self.IL.Get('bitcoin'), bg = Col_Title, bd = 0)
        self.Widgets['Title']['Bitcoin'].pack(side = TOP, fill = X)
        self.Widgets['Title']['Stock'] = Label(self.StockFrame, height = 60, image = self.IL.Get('stock'), bg = Col_Title, bd = 0)
        self.Widgets['Title']['Stock'].pack(side = TOP, fill = X)

        self.Setup('Bitcoin', self.BitcoinFrame, self.Widgets['Bitcoin'])
        self.Setup('Stock', self.StockFrame, self.Widgets['Stock'])

    def Setup(self, type, P, D):
        MenuFrame = UIMaker.PackFix(Frame(P, width = 481, height = 77, bg = Col_Title), BOTTOM, NONE, False)
        Button(MenuFrame, text = '  저장', font = self.FontMain, width = 100, height = 30, bd = 0, highlightthickness=0, activebackground=Col_Title, 
               bg = Col_Title, fg = 'white', activeforeground = Col_red, image = self.IL.Get('favorites_on'), compound = LEFT).pack(side = LEFT)
        for i in range(0, 15) :
            Col = Col_Main
            if i % 2 == 1 : Col = Col_Sub
            self.Frames[type+str(i)] = UIMaker.PackFix(Frame(P, height = 38, bg = Col), TOP, X, False)