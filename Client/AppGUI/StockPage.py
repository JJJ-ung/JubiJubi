import re
import sys
import random
import numpy as np
from datetime import *

from tkinter import *
import tkinter.font

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.figure import *
from matplotlib.animation import *
from matplotlib.backends.backend_tkagg import *

sys.path.append('/Stock.py')
import Stock
from . import UIMaker
from . import ImageLoader

Col_title = '#3f3f3f'
Col_titleR = '#4e4e4e'
Col_titleM = '#4a4a4a'
Col_back = '#333333'
Col_line0 = '#3b3b3b'
Col_line1 = '#353535'
Col_red = '#eb6148'
Col_blue = '#008dd2'
Col_SubFont = '#bbbbbb'


class Compare:
    def __init__(self, stock, label, radio):
        self.Stock = stock
        self.Ticker = stock.code
        self.Name = stock.name + "  " + stock.code
        self.Label = label
        self.Radio = radio
        self.Label.configure(text=self.Name)

    def Delete(self):
        self.Stock.Save = False
        self.Label.destroy()
        self.Radio.destroy()

    def Set(self, index, label, radio):
        self.Label.destroy()
        self.Radio.destroy()
        self.Label = label
        self.Radio = radio
        self.Label.configure(text=self.Name)


class Page:
    def SetCurr(self, stock):
        if self.CurrStock is not None:
            if not self.CurrStock.Save:
                del self.CurrStock
        D = self.W('Name')
        self.CurrStock = stock
        self.Yesterday = stock.lstDailyData[4]
        D['Name']['text'] = stock.name
        D['Tiker']['text'] = stock.code
        self.ResetFunction()
        self.SetDaily(stock)
        self.SetGraph()

    def SetDaily(self, stock):
        D = self.W('Daily')
        Today = datetime.today()
        for i in range(0, 5):
            P = self.F('Daily_' + str(i + 1))
            L = stock.lstDailyData
            CurrDate = (Today - timedelta(i)).strftime('%m-%d')
            PriceToday = L[5 - i]
            PriceYesterday = L[4 - i]
            PriceChange = round(PriceToday - PriceYesterday, 2)
            Percent = round((PriceChange / PriceYesterday) * 100, 2)
            Market = stock.lstDailyMarketPrice[5 - i]
            Bought = int(stock.lstDailyVolume[5 - i])
            if PriceChange >= 0:
                Col_F = Col_red
                PriceChange = '+' + str(PriceChange)
                Percent = '+' + str(Percent)
            else:
                Col_F = Col_blue
                PriceChange = str(PriceChange)
                Percent = str(Percent)
            D[str(i) + 'Day'].configure(text=CurrDate)
            D[str(i) + 'KRW'].configure(text=PriceToday, fg=Col_F)
            D[str(i) + 'Real'].configure(text=PriceChange, fg=Col_F)
            D[str(i) + 'Percent'].configure(text=Percent, fg=Col_F)
            D[str(i) + 'MarketPrice'].configure(text=Market, fg=Col_F)
            D[str(i) + 'Buy'].configure(text=Bought)

    def UpdateCurr(self):
        if self.CurrStock is None:
            return
        now = self.CurrStock.getPrice()
        change = now - self.Yesterday
        self.Curr.set(str(now))
        self.Percent.set(str(round((change / self.Yesterday) * 100, 2)) + '%')
        if change > 0:
            self.Widgets['Name']['UpDown'].configure(text='▲', fg=Col_red)
        else:
            self.Widgets['Name']['UpDown'].configure(text='▼', fg=Col_blue)

    def __init__(self, parent, IL, FavPage, AutoPage):
        self.IL = IL
        self.Frames = dict()
        self.Widgets = {'Name': dict(), 'Graph': dict(), 'Daily': dict(), 'Compare': dict(), 'Functions': dict()}
        # for Info
        self.CurrStock = None
        self.Yesterday = None
        self.Curr = StringVar()
        # for Daily
        self.DailyData = list()
        self.Percent = StringVar()
        self.UpDown = StringVar()
        # for Graph
        self.x = list()
        self.GraphData = list()
        # for Func
        self.Auto = False
        self.Fav = False
        self.AniGraph = False
        # for Compare
        self.CompareList = list()
        self.CompareIndex = IntVar()
        self.CompareItems = 0

        self.LoadFont()
        self.LoadFrames(parent)
        self.LoadDailyFrame()
        self.LoadCompareFrame()
        self.LoadFuncFrame()

        self.FavPage = FavPage
        self.AutoPage = AutoPage

    def LoadFont(self):
        self.Fonts = dict()
        self.Fonts['Title'] = tkinter.font.Font(family='NanumSquareEB', size=20, weight='bold')
        self.Fonts['TitleS'] = tkinter.font.Font(family='NanumSquareEB', size=10, weight='bold')
        self.Fonts['TitleM'] = tkinter.font.Font(family='NanumSquareEB', size=13, weight='bold')
        self.Fonts['TitleMS'] = tkinter.font.Font(family='NanumSquareEB', size=18, weight='bold')
        self.Fonts['SubTitle'] = tkinter.font.Font(family='나눔스퀘어', size=10, weight='normal')
        self.Fonts['Items'] = tkinter.font.Font(family='나눔스퀘어', size=10, weight='normal')
        self.Fonts['Menu'] = tkinter.font.Font(family='나눔스퀘어', size=10, weight='bold')

    def LoadFrames(self, parent):
        self.Frames['Left'] = UIMaker.PackFix(Frame(parent, width=610, bg=Col_back), LEFT, BOTH, NO)
        self.Frames['Right'] = UIMaker.PackFix(Frame(parent, width=353, bg=Col_back), RIGHT, Y, NO)

        P = self.F('Left')
        self.Frames['Name'] = UIMaker.PackFix(Frame(P, height=88, bg=Col_back), TOP, BOTH, NO)
        self.Frames['Graph'] = UIMaker.PackFix(Frame(P, height=380, bg=Col_back), TOP, BOTH, NO)
        self.Frames['Daily'] = UIMaker.PackFix(Frame(P, bg=Col_back), TOP, BOTH, YES)

        P = self.F('Right')
        self.Frames['Compare'] = UIMaker.PackFix(Frame(P, height=468, bg='#6b6b6b'), TOP, BOTH, NO)
        self.Frames['Functions'] = UIMaker.PackFix(Frame(P, bg='#6b6b6b'), TOP, BOTH, YES)

        P = self.F('Name')
        D = self.W('Name')
        self.Frames['Name_Top'] = UIMaker.PackFix(Frame(P, height=50, bg=Col_title), TOP, BOTH, NO)
        self.Frames['Name_Bot'] = UIMaker.PackFix(Frame(P, bg=Col_title), TOP, BOTH, YES)
        D['Name'] = Label(self.F('Name_Top'), font=self.Fo('Title'), fg='white', bg=Col_title, bd=0)
        D['Name'].place(relx=0.05, rely=1, anchor=SW)
        D['Tiker'] = Label(self.F('Name_Bot'), font=self.Fo('SubTitle'), fg='white', bg=Col_title, bd=0)
        D['Tiker'].place(relx=0.05, anchor=NW)
        D['KRW'] = Label(self.F('Name_Top'), text='KRW', font=self.Fo('TitleS'), fg='white', bg=Col_title, bd=0)
        D['KRW'].place(relx=0.97, rely=0.92, anchor=SE)
        D['Curr'] = Label(self.F('Name_Top'), textvariable=self.Curr, font=self.Fo('Title'), fg='white', bg=Col_title,
                          bd=0)
        D['Curr'].place(relx=0.91, rely=1, anchor=SE)
        D['Percent'] = Label(self.F('Name_Bot'), textvariable=self.Percent, font=self.Fo('SubTitle'), fg='white',
                             bg=Col_title, bd=0)
        D['Percent'].place(relx=0.95, anchor=NE)
        D['UpDown'] = Label(self.F('Name_Bot'), font=self.Fo('SubTitle'), fg=Col_red, bg=Col_title, bd=0)
        D['UpDown'].place(relx=0.95, anchor=NW)

        P = self.F('Graph')
        self.fig = plt.figure(facecolor=Col_back)
        self.Canvas = FigureCanvasTkAgg(self.fig, P)
        self.Canvas.get_tk_widget().pack(fill=BOTH)

    def LoadDailyFrame(self):
        P = self.F('Daily')
        D = self.W('Daily')
        self.Frames['Daily_Menu'] = UIMaker.PackFix(Frame(P, height=40, bg=Col_titleR), TOP, BOTH, NO)
        for i in range(1, 6):
            if (i % 2 == 0):
                self.Frames['Daily_' + str(i)] = UIMaker.PackFix(Frame(P, height=40, bg=Col_title), TOP, BOTH, NO)
            else:
                self.Frames['Daily_' + str(i)] = UIMaker.PackFix(Frame(P, height=40, bg=Col_back), TOP, BOTH, NO)
        UIMaker.TextLabel(self.F('Daily_Menu'), '일자', self.Fo('Menu'), 'white', Col_titleR).place(relx=0.05, rely=0.5,
                                                                                                  anchor=W)
        UIMaker.TextLabel(self.F('Daily_Menu'), '종가(KRW)', self.Fo('Menu'), 'white', Col_titleR).place(relx=0.20,
                                                                                                       rely=0.5,
                                                                                                       anchor=W)
        UIMaker.TextLabel(self.F('Daily_Menu'), '전일대비', self.Fo('Menu'), 'white', Col_titleR).place(relx=0.43, rely=0.5,
                                                                                                    anchor=W)
        UIMaker.TextLabel(self.F('Daily_Menu'), '시가', self.Fo('Menu'), 'white', Col_titleR).place(relx=0.62, rely=0.5,
                                                                                                  anchor=W)
        UIMaker.TextLabel(self.F('Daily_Menu'), '거래', self.Fo('Menu'), 'white', Col_titleR).place(relx=0.79, rely=0.5,
                                                                                                  anchor=W)
        for i in range(0, 5):
            P = self.F('Daily_' + str(i + 1))
            Col = Col_title
            if (i % 2 == 0): Col = Col_back
            D[str(i) + 'Day'] = Label(P, font=self.Fo('Items'), fg='white', bg=Col, bd=0)
            D[str(i) + 'Day'].place(relx=0.03, rely=0.5, anchor=W)
            D[str(i) + 'KRW'] = Label(P, font=self.Fo('Menu'), fg='white', bg=Col, bd=0)
            D[str(i) + 'KRW'].place(relx=0.2, rely=0.5, anchor=W)
            D[str(i) + 'Real'] = Label(P, font=self.Fo('Items'), fg='white', bg=Col, bd=0)
            D[str(i) + 'Real'].place(relx=0.2, rely=0.5, anchor=E)
            D[str(i) + 'Percent'] = Label(P, font=self.Fo('Menu'), fg='white', bg=Col, bd=0)
            D[str(i) + 'Percent'].place(relx=0.43, rely=0.5, anchor=W)
            D[str(i) + 'MarketPrice'] = Label(P, font=self.Fo('Menu'), fg='white', bg=Col, bd=0)
            D[str(i) + 'MarketPrice'].place(relx=0.62, rely=0.5, anchor=W)
            D[str(i) + 'Buy'] = Label(P, font=self.Fo('Items'), fg='white', bg=Col, bd=0)
            D[str(i) + 'Buy'].place(relx=0.79, rely=0.5, anchor=W)

    def LoadCompareFrame(self):
        P = self.F('Compare')
        D = self.W('Compare')

        self.Frames['Compare_Menu'] = UIMaker.PackFix(Frame(P, height=50, bg=Col_titleR), TOP, BOTH, NO)
        self.Frames['Compare_Info'] = UIMaker.PackFix(Frame(P, height=38, bg=Col_back), TOP, BOTH, NO)
        for i in range(0, 10):
            Col = Col_back
            if (i % 2 == 0): Col = Col_title
            self.Frames['Compare_' + str(i)] = UIMaker.PackFix(Frame(P, height=38, bg=Col), TOP, BOTH, NO)
        P = self.F('Compare_Menu')
        UIMaker.TextLabel(P, '비교목록', self.Fo('TitleM'), 'white', Col_titleR).place(relx=0.05, rely=0.5, anchor=W)
        D['Remove'] = Button(P, text='─', font=self.Fo('Title'), width=50, height=50, bd=0, highlightthickness=0,
                             activebackground=Col_blue,
                             bg=Col_titleR, fg=Col_blue, image=self.IL.pixelVirtual, compound=CENTER,
                             command=self.DeleteCompare)
        D['Remove'].pack(side=RIGHT)
        D['Add'] = Button(P, text='+', font=self.Fo('Title'), width=50, height=50, bd=0, highlightthickness=0,
                          activebackground=Col_red,
                          bg=Col_titleR, fg=Col_red, image=self.IL.pixelVirtual, compound=CENTER,
                          command=self.AddCompare)
        D['Add'].pack(side=RIGHT)
        P = self.F('Compare_Info')
        Label(P, image=self.I('boxminus_small'), bg=Col_back, bd=0).place(relx=0.05, rely=0.5, anchor=W)
        Label(P, text='종목', font=self.Fo('Menu'), fg='white', bg=Col_back, bd=0).place(relx=0.2, rely=0.5, anchor=W)

    def LoadFuncFrame(self):
        P = self.F('Functions')
        D = self.W('Functions')

        self.Frames['Function_Menu'] = UIMaker.PackFix(Frame(P, height=40, bg=Col_titleR), TOP, BOTH, NO)
        self.Frames['Function_Buttons'] = UIMaker.PackFix(Frame(P, height=81, bg=Col_titleR), TOP, BOTH, NO)
        self.Frames['Function_Dice'] = UIMaker.PackFix(Frame(P, height=121, bg=Col_back), BOTTOM, BOTH, NO)

        UIMaker.TextLabel(self.Frames['Function_Menu'], '기능', self.Fo('TitleM'), 'white', Col_titleR).place(relx=0.05,
                                                                                                            rely=0.5,
                                                                                                            anchor=W)

        P = self.F('Function_Buttons')
        D['Fav'] = Button(P, width=118, height=81, image=self.I('Fav_Off'), bg=Col_back, bd=0, relief=FLAT,
                          highlightthickness=0, activebackground=Col_back, anchor='center',
                          command=lambda: self.ChangeFunction('Fav'))
        D['Fav'].grid(row=0, column=0)
        D['Auto'] = Button(P, width=118, height=81, image=self.I('Auto_Off'), bg=Col_back, bd=0, relief=FLAT,
                           highlightthickness=0, activebackground=Col_back, anchor='center',
                           command=lambda: self.ChangeFunction('Auto'))
        D['Auto'].grid(row=0, column=1)
        D['Graph'] = Button(P, width=118, height=81, image=self.I('Graph1_Off'), bg=Col_back, bd=0, relief=FLAT,
                            highlightthickness=0, activebackground=Col_back, anchor='center',
                            command=lambda: self.ChangeFunction('Graph'))
        D['Graph'].grid(row=0, column=2)

        P = self.F('Function_Dice')
        D['DiceImg'] = Button(P, width=74, height=74, image=self.I('dice_1'), bd=0, relief=FLAT, highlightthickness=0,
                              activebackground=Col_back, anchor='center',
                              command=lambda: self.DiceFunction())
        D['DiceImg'].place(relx=0.1, rely=0.5, anchor=W)
        D['DiceResult'] = Label(P, text='운세 주사위 !', font=self.Fo('TitleMS'), fg='white', bg=Col_back)
        D['DiceResult'].place(relx=0.9, rely=0.5, anchor=SE)
        D['DiceComment'] = Label(P, text='주사위를 굴려보세요', font=self.Fo('Items'), fg='white', bg=Col_back)
        D['DiceComment'].place(relx=0.9, rely=0.5, anchor=NE)

    def ChangeFunction(self, tag):
        if self.CurrStock is None:
            return

        D = self.W('Functions')
        str = ''
        if tag is 'Fav':
            self.Fav = not self.Fav
            if self.Fav:
                str = tag + '_On'
                self.AddFav()
            else:
                str = tag + '_Off'
                self.DelFav()

        if tag is 'Auto':
            self.Auto = not self.Auto
            if self.Auto:
                str = tag + '_On'
                self.AutoPage.Add('stock', self.CurrStock.name)
            else:
                str = tag + '_Off'
                self.AutoPage.Delete('stock', self.CurrStock.name)

        if tag is 'Graph':
            self.AniGraph = not self.AniGraph
            if self.AniGraph:
                str = tag + '_On'
                self.SetAniGraph()
            else:
                str = tag + '_Off'
                self.SetGraph()

        D[tag]['image'] = self.I(str)

    def ResetFunction(self):
        D = self.W('Functions')

        if self.AutoPage.Find('stock', self.CurrStock.name) is False:
            self.Auto = False
            D['Auto']['image'] = self.I('Auto_Off')
        else:
            self.Auto = True
            D['Auto']['image'] = self.I('Auto_On')

        if self.FavPage.Find('stock', self.CurrStock.code) is False:
            self.Fav = False
            D['Fav']['image'] = self.I('Fav_Off')
        else:
            self.Fav = True
            D['Fav']['image'] = self.I('Fav_On')

        self.AniGraph = False
        D['Graph']['image'] = self.I('Graph_Off')

    def DiceFunction(self):
        result = random.randint(1, 6)
        D = self.W('Functions')
        D['DiceImg']['image'] = self.I('dice_' + str(result))
        if result == 1:
            D['DiceResult']['text'] = '1이 나왔네요!'
            D['DiceResult']['fg'] = Col_blue
            D['DiceComment']['text'] = '나-락'
        if result == 2:
            D['DiceResult']['text'] = '2가 나왔네요!'
            D['DiceResult']['fg'] = Col_blue
            D['DiceComment']['text'] = '물리기 전에 손절하세요'
        if result == 3:
            D['DiceResult']['text'] = '3이 나왔네요!'
            D['DiceResult']['fg'] = Col_blue
            D['DiceComment']['text'] = '적당히 안좋은거'
        if result == 4:
            D['DiceResult']['text'] = '4가 나왔네요!'
            D['DiceResult']['fg'] = Col_red
            D['DiceComment']['text'] = '적당히 좋은거'
        if result == 5:
            D['DiceResult']['text'] = '5가 나왔네요!'
            D['DiceResult']['fg'] = Col_red
            D['DiceComment']['text'] = '좀 좋은거'
        if result == 6:
            D['DiceResult']['text'] = '6이 나왔네요!'
            D['DiceResult']['fg'] = Col_red
            D['DiceComment']['text'] = '극-락'

    def SetGraph(self):
        # 하루당
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        self.GraphData.clear()
        self.GraphData = list(self.CurrStock.graphDataDay)
        self.GraphData.reverse()
        self.x.clear()
        self.x = [datetime.now() - timedelta(days=i) for i in range(len(self.GraphData))]
        self.x.reverse()
        self.SetAxis('%m/%d')
        self.line, = self.ax.plot(self.x, self.GraphData, lw=2, color=Col_red)
        self.ax.ticklabel_format(axis='y', style='plain')
        self.Canvas.draw()

    def SetAniGraph(self):
        # 1주당
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        self.GraphData.clear()
        self.GraphData = list(self.CurrStock.graphDataWeek)
        self.GraphData.reverse()
        self.x.clear()
        self.x = [datetime.now() - timedelta(days=i * 7) for i in range(len(self.GraphData))]
        self.x.reverse()
        self.SetAxis('%m/%d')
        self.line, = self.ax.plot(self.x, self.GraphData, lw=2, color=Col_red)
        self.ax.ticklabel_format(axis='y', style='plain')
        self.Canvas.draw()

    def SetAxis(self, format):
        self.ax.set_facecolor(Col_back)
        self.ax.spines['bottom'].set_color('#dddddd')
        self.ax.spines['top'].set_color(Col_back)
        self.ax.spines['right'].set_color(Col_back)
        self.ax.spines['left'].set_color('#dddddd')
        self.ax.tick_params(axis='x', colors='#dddddd')
        self.ax.tick_params(axis='y', colors='#dddddd')
        self.ax.ticklabel_format(axis='y', style='plain')
        self.ax.grid(True, color='white', alpha=0.1)
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter(format))
        self.fig.autofmt_xdate()

    def AddCompare(self):
        if self.CurrStock is None:
            return
        for var in self.CompareList:
            if var.Ticker == self.CurrStock.code:
                return
        index = len(self.CompareList)
        P = self.Frames['Compare_' + str(index)]
        Col = Col_back
        if (index % 2 == 0): Col = Col_title
        label = Label(P, font=self.Fo('Items'), fg='white', bg=Col, bd=0)
        label.place(relx=0.2, rely=0.5, anchor=W)
        radio = Radiobutton(P, image=self.I('check_no'), selectimage=self.I('check_yes'), value=index,
                            variable=self.CompareIndex,
                            bg=Col, activebackground=Col, selectcolor=Col, bd=0, indicatoron=0,
                            command=self.SetCompareToCurr)
        radio.place(relx=0.045, rely=0.5, anchor=W)
        self.CompareList.append(Compare(self.CurrStock, label, radio))
        self.CompareIndex.set(index)
        self.CurrStock.Save = True

    def DeleteCompare(self):
        self.CompareList[self.CompareIndex.get()].Delete()
        del self.CompareList[self.CompareIndex.get()]
        for index in range(0, len(self.CompareList)):
            P = self.Frames['Compare_' + str(index)]
            Col = Col_back
            if (index % 2 == 0): Col = Col_title
            label = Label(P, font=self.Fo('Items'), fg='white', bg=Col, bd=0)
            label.place(relx=0.2, rely=0.5, anchor=W)
            radio = Radiobutton(P, image=self.I('check_no'), selectimage=self.I('check_yes'), value=index,
                                variable=self.CompareIndex,
                                bg=Col, activebackground=Col, selectcolor=Col, bd=0, indicatoron=0,
                                command=self.SetCompareToCurr)
            radio.place(relx=0.045, rely=0.5, anchor=W)
            self.CompareList[index].Set(index, label, radio)

    def SetCompareToCurr(self):
        stock = self.CompareList[self.CompareIndex.get()].Stock
        self.SetCurr(stock)

    def AddFav(self):
        self.FavPage.Add('stock', self.CurrStock)

    def DelFav(self):
        self.FavPage.Delete('stock', self.CurrStock.code)

    def Fo(self, name):
        return self.Fonts[name]

    def I(self, name):
        return self.IL.Get(name)

    def F(self, name):
        return self.Frames[name]

    def W(self, name):
        return self.Widgets[name]
