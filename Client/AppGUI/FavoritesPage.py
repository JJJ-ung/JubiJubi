from tkinter import *
import tkinter.font
from . import UIMaker
from . import ImageLoader

Col_Title = '#4e4e4e'
Col_Main = '#333333'
Col_Sub = '#393939'
Col_red = '#eb6148'
Col_blue = '#008dd2'

class tmp:
    def __init__(self, name, KRW, percent, Up) :
        self.name = name
        self.percent = percent
        self.KRW = KRW
        self.IsUp = Up

class Page:
    ##################################################################################################################
    #   이니셜라이즈
    ##################################################################################################################
    def Add_Bitcoin(self) :
        D = self.Widgets['Bitcoin']
        i = len(self.BitcoinFav)
        if i == 15 : pass
        Col = Col_Main
        if i % 2 == 1 :
            Col = Col_Sub
            self.BitcoinFav.append(tmp('도지코인', 570, 12, True))
        else :
            self.BitcoinFav.append(tmp('이더리움 클래식', 1254013759713, 423670, False))
        F = self.Frames['Bit'+str(i)]
        D['Check'+str(i)].place(relx = 0.03, rely = 0.5, anchor = W)
        D['Name'+str(i)] = Label(F, height = 38, bg = Col, bd = 0, text = self.BitcoinFav[i].name, font = self.Fonts['Main'], fg = 'white')
        D['Name'+str(i)].place(relx = 0.1, rely = 0.5, anchor = W)
        D['Percent'+str(i)] = Label(F, height = 38, bg = Col, bd = 0, text = str(self.BitcoinFav[i].percent) + '%', font = self.Fonts['Sub'], fg = 'white')
        D['Percent'+str(i)].place(relx = 0.9, rely = 0.5, anchor = E)
        if self.BitcoinFav[i].IsUp :
            D['UpDown'+str(i)] = Label(F, height = 38, bg = Col, bd = 0, font = self.Fonts['Sub'], fg = Col_red, text = '▲')
        else:
            D['UpDown'+str(i)] = Label(F, height = 38, bg = Col, bd = 0, font = self.Fonts['Sub'], fg = Col_blue, text = '▼')
        D['UpDown'+str(i)].place(relx = 0.91, rely = 0.5, anchor = W)

    def __init__(self, parent, IL):
        self.IL = IL
        self.BitcoinFav = list()
        self.StockFav = list()
        self.StockSel = 0
        self.BitcoinSel = 0

        self.Fonts = dict()
        self.Fonts['Main'] = tkinter.font.Font(family='나눔스퀘어', size=12, weight='bold')
        self.Fonts['Sub'] = tkinter.font.Font(family='나눔스퀘어', size=12, weight='normal')

        self.Frames = dict()
        self.BitcoinFrame = UIMaker.CreateFixedFrame(parent, 481, 0, Col_Main, 'p')
        self.BitcoinFrame.pack(side = LEFT, fill = Y)

        self.StockFrame = UIMaker.CreateFixedFrame(parent, 481, 0, Col_Main, 'p')
        self.StockFrame.pack(side = RIGHT, fill = Y)

        self.Widgets = {'Bitcoin' : dict(), 'Stock' : dict(), 'Title' : dict()}
        
        self.Widgets['Title']['Bitcoin'] = Label(self.BitcoinFrame, height = 60, image = self.IL.Get('bitcoin'), bg = Col_Title, bd = 0)
        self.Widgets['Title']['Bitcoin'].pack(side = TOP, fill = X)
        self.Widgets['Title']['Stock'] = Label(self.StockFrame, height = 60, image = self.IL.Get('stock'), bg = Col_Title, bd = 0)
        self.Widgets['Title']['Stock'].pack(side = TOP, fill = X)

        #비트코인 쪽
        P = self.BitcoinFrame
        D = self.Widgets['Bitcoin']
        self.BitcoinMenuFrame = UIMaker.CreateFixedFrame(P, 481, 77, Col_Title, 'p')
        self.BitcoinMenuFrame.pack(side = BOTTOM)
        D['Button_Del'] = Button(self.BitcoinMenuFrame, width = 88, height = 78, image = self.IL.Get('delete'), bg = Col_Title, bd = 0, highlightthickness=0, activebackground=Col_Title)
                                          #command =lambda: self.ChangeFunction('Fav'))
        D['Button_Del'].place(relx = 0.97, rely = 0.5, anchor = E)
        D['SelectedCnt'] = Label(self.BitcoinMenuFrame, text = '0개 종목', bd = 0, bg = Col_Title, font = self.Fonts['Main'], fg = 'white')
        D['SelectedCnt'].place(relx = 0.05, rely = 0.5, anchor = W)

        for i in range(0, 15) :
            Col = Col_Main
            if i % 2 == 1 :
                Col = Col_Sub
            self.Frames['Bit'+str(i)] = UIMaker.CreateFixedFrame(P, 0, 38, Col, 'p')
            self.Frames['Bit'+str(i)].pack(side = TOP, fill = X)
            D['Check'+str(i)] = Checkbutton(self.Frames['Bit'+str(i)], image = self.IL.Get('check_no'), selectimage = self.IL.Get('check_yes'), indicatoron=False,
            onvalue=1, offvalue=0, variable=IntVar(value = i), bg = Col, selectcolor = Col, activebackground = Col, bd = 0, command = self.CheckBitcoin)
            self.Add_Bitcoin()

        #주식 쪽
        P = self.StockFrame
        D = self.Widgets['Stock']
        self.StockMenuFrame = UIMaker.CreateFixedFrame(P, 481, 77, Col_Title, 'p')
        self.StockMenuFrame.pack(side = BOTTOM)
        D['Button_Del'] = Button(self.BitcoinMenuFrame, width = 88, height = 78, image = self.IL.Get('delete'), bg = Col_Title, bd = 0, highlightthickness=0, activebackground=Col_Title)
                                          #command =lambda: self.ChangeFunction('Fav'))
        D['Button_Del'].place(relx = 0.97, rely = 0.5, anchor = E)
        D['SelectedCnt'] = Label(self.BitcoinMenuFrame, text = '0개 종목', bd = 0, bg = Col_Title, font = self.Fonts['Main'], fg = 'white')
        D['SelectedCnt'].place(relx = 0.05, rely = 0.5, anchor = W)

        for i in range(0, 15) :
            self.Frames['Stock'+str(i)] = UIMaker.CreateFixedFrame(P, 0, 38, Col, 'p')
            self.Frames['Stock'+str(i)].pack(side = TOP, fill = X)
            D['Check'+str(i)] = Checkbutton(self.Frames['Stock'+str(i)], image = self.IL.Get('check_no'), selectimage = self.IL.Get('check_yes'), indicatoron=False,
            onvalue=1, offvalue=0, variable=IntVar(value = i), bg = Col, selectcolor = Col, activebackground = Col, bd = 0, command = self.CheckStock)

    def CheckBitcoin(self):
        ++self.BitcoinSel
        self.Widgets['Bitcoin']['SelectedCnt']['text'] = str(self.BitcoinSel) + '개 종목'

    def CheckStock(self):
        ++self.StockSel
        self.Widgets['Stock']['SelectedCnt']['text'] = str(self.StockSel) + '개 종목'