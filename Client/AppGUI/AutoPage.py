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

        self.FontMain = tkinter.font.Font(family='나눔스퀘어', size=12, weight='bold')
        self.FontSub = tkinter.font.Font(family='나눔스퀘어', size=10, weight='normal')

        self.Frames['Coin'] = UIMaker.PackFix(Frame(parent, width = 481, bg = Col_Main, bd = 0), LEFT, Y, False)
        self.Frames['Stock'] = UIMaker.PackFix(Frame(parent, width = 481, bg = Col_Main, bd = 0), RIGHT, Y, False)

        P = self.Frames['Coin']
        W['CoinLogo'] = Label(P, height = 60, bg = Col_Title, bd = 0, image = IL.Get('bitcoin'))
        W['CoinLogo'].pack(side = TOP, fill = X)

        Pa = self.Frames['CoinMain'] = UIMaker.PackFix(Frame(P, height = 400, bg = '#3f3f3f', bd = 0), TOP, X, False)
        Pb = self.Frames['CoinLst'] = UIMaker.PackFix(Frame(Pa, width = 240, bg = 'yellow', bd = 0), LEFT, Y, False)
        for i in range(0, 10) :
            Col = Col_Main
            if i % 2 == 1 : Col = Col_Sub
            self.Frames['CoinLst'+str(i)] = UIMaker.PackFix(Frame(Pb, height = 40, bg = Col), TOP, X, False)
        self.CoinLog = Text(Pa, bg = Col_Main, bd = 0, fg = 'white', padx = 8, pady = 8, font = self.FontSub)#
        self.CoinLog.bind("<Key>", lambda e: "break")
        self.CoinLog.pack(side = RIGHT, fill = BOTH, expand = True)

        self.CoinLog.insert(CURRENT, '▶ 업비트 자동매매 로그\n\n')
        self.CoinLog.insert(CURRENT, '- 자동매매 설정을 완료 해주세요\n')

        Pa = self.Frames['CoinFunc'] = UIMaker.PackFix(Frame(P, bg = Col_Title, bd = 0), TOP, BOTH, True)
        W['CoinBuyLabel'] = Label(Pa, text = '구매 가격  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['CoinBuyLabel'].place(relx = 0.1, rely = 0.2, anchor = 'w')
        W['CoinPercentLabel'] = Label(Pa, text = '수익률  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['CoinPercentLabel'].place(relx = 0.1, rely = 0.4, anchor = 'w')

        P = self.Frames['Stock']
        W['StockLogo'] = Label(P, height = 60, bg = Col_Title, bd = 0, image = IL.Get('stock'))
        W['StockLogo'].pack(side = TOP, fill = X)
        
        Pa = self.Frames['StockMain'] = UIMaker.PackFix(Frame(P, height = 400, bg = '#3f3f3f', bd = 0), TOP, X, False)
        Pb = self.Frames['StockLst'] = UIMaker.PackFix(Frame(Pa, width = 240, bg = 'yellow', bd = 0), LEFT, Y, False)
        for i in range(0, 10) :
            Col = Col_Main
            if i % 2 == 1 : Col = Col_Sub
            self.Frames['StockLst'+str(i)] = UIMaker.PackFix(Frame(Pb, height = 40, bg = Col), TOP, X, False)
        self.StockLog = Text(Pa, bg = Col_Main, bd = 0, fg = 'white', padx = 8, pady = 8, font = self.FontSub)#
        self.StockLog.bind("<Key>", lambda e: "break")
        self.StockLog.pack(side = RIGHT, fill = BOTH, expand = True)

        self.StockLog.insert(CURRENT, '▶ 키움증권 자동매매 로그\n\n')
        self.StockLog.insert(CURRENT, '- 자동매매 설정을 완료 해주세요\n')
        
        Pa = self.Frames['StockFunc'] = UIMaker.PackFix(Frame(P, bg = Col_Title, bd = 0), TOP, BOTH, True)
        W['StockBuyLabel'] = Label(Pa, text = '구매 가격  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['StockBuyLabel'].place(relx = 0.1, rely = 0.2, anchor = 'w')
        W['StockPercentLabel'] = Label(Pa, text = '수익률  ', font = self.FontMain, bg = Col_Title, fg = 'white', bd = 0)
        W['StockPercentLabel'].place(relx = 0.1, rely = 0.4, anchor = 'w')

