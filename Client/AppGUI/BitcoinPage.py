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

sys.path.append('/Bitcoin.py')
import Bitcoin
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

class Page:
    def SetCurr(self, coin):
        self.ResetFunction()
        D = self.W('Name')
        self.CurrCoin = coin
        self.Yesterday = coin.lstDailyData[4]
        ImagePath = 'https://static.upbit.com/logos/' + re.sub("KRW-", "", coin.ticker) + '.png'
        self.Widgets['Name']['Icon'].configure(image = self.IL.ImgFromURL(ImagePath, 25, 25))
        D['Name']['text'] = coin.koreanName
        D['Tiker']['text'] =  coin.ticker + '/' + coin.englishName
        self.SetDaily(coin)
        self.SetGraph()

    def SetDaily(self, coin):
        D = self.W('Daily')
        Today = datetime.today()
        for i in range(0, 5):
            P = self.F('Daily_'+str(i + 1))
            L = coin.lstDailyData
            CurrDate = (Today - timedelta(i)).strftime('%m-%d')
            PriceToday = L[5 - i]
            PriceYesterday = L[4 - i]
            PriceChange = round(PriceToday - PriceYesterday, 2)
            Percent = round((PriceChange / PriceYesterday) * 100, 2)
            Bought = int(coin.lstDailyVolume[5 - i])
            if PriceChange >= 0 :
                Col_F = Col_red
                PriceChange = '+' + str(PriceChange)
                Percent = '+' + str(Percent)
            else :
                Col_F = Col_blue
                PriceChange = str(PriceChange)
                Percent = str(Percent)
            D[str(i)+'Day'].configure(text = CurrDate)
            D[str(i)+'KRW'].configure(text = PriceToday, fg = Col_F)
            D[str(i)+'Real'].configure(text = PriceChange, fg = Col_F)
            D[str(i)+'Percent'].configure(text = Percent, fg = Col_F)
            D[str(i)+'Buy'].configure(text = Bought)

    def UpdateCurr(self, coin):
        now = coin.getPrice()
        change = now - self.Yesterday
        self.Curr.set(str(now))       
        self.Percent.set(str(round((change / self.Yesterday) * 100, 2)) + '%')
        if change > 0 : self.Widgets['Name']['UpDown'].configure(text = '▲', fg = Col_red)
        else : self.Widgets['Name']['UpDown'].configure(text = '▼', fg = Col_blue)

    def __init__(self, parent, IL):
        self.IL = IL
        self.Frames = dict()
        self.Widgets = {'Name' : dict(), 'Graph' : dict(), 'Daily' : dict(), 'Compare' : dict(), 'Functions' : dict()}
        # for Info
        self.CurrCoin = None
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

        self.LoadFont()
        self.LoadFrames(parent)
        self.LoadDailyFrame()
        self.LoadCompareFrame()
        self.LoadFuncFrame()

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
        self.Frames['Left'] = UIMaker.PackFix(Frame(parent, width = 610, bg=Col_back), LEFT, BOTH, NO)
        self.Frames['Right'] = UIMaker.PackFix(Frame(parent, width = 353, bg=Col_back), RIGHT, Y, NO)
        
        P = self.F('Left')
        self.Frames['Name'] = UIMaker.PackFix(Frame(P, height = 88, bg = Col_back), TOP, BOTH, NO)
        self.Frames['Graph'] = UIMaker.PackFix(Frame(P, height = 380, bg = Col_back), TOP, BOTH, NO)
        self.Frames['Daily'] = UIMaker.PackFix(Frame(P, bg = Col_back), TOP, BOTH, YES)
        
        P = self.F('Right')
        self.Frames['Compare'] = UIMaker.PackFix(Frame(P, height = 468, bg = '#6b6b6b'), TOP, BOTH, NO)
        self.Frames['Functions'] = UIMaker.PackFix(Frame(P, bg = '#6b6b6b'), TOP, BOTH, YES)
        
        P = self.F('Name')
        D = self.W('Name')
        self.Frames['Name_Icon'] = UIMaker.PackFix(Frame(P, width = 60, bg = Col_title), LEFT, BOTH, NO)
        D['Icon'] = Label(self.F('Name_Icon'), bg = Col_title, bd = 0)
        D['Icon'].place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.Frames['Name_Top'] = UIMaker.PackFix(Frame(P, height = 50, bg = Col_title), TOP, BOTH, NO)
        self.Frames['Name_Bot'] = UIMaker.PackFix(Frame(P, bg = Col_title), TOP, BOTH, YES)
        D['Name'] = Label(self.F('Name_Top'), font = self.Fo('Title'), fg = 'white', bg = Col_title, bd = 0)
        D['Name'].place(rely = 1, anchor = SW)
        D['Tiker'] = Label(self.F('Name_Bot'), font = self.Fo('SubTitle'), fg = 'white', bg = Col_title, bd = 0)
        D['Tiker'].place(relx = 0.005, anchor = NW)
        D['KRW'] = Label(self.F('Name_Top'), text = 'KRW', font = self.Fo('TitleS'), fg = 'white', bg = Col_title, bd = 0)
        D['KRW'].place(relx = 0.97, rely = 0.92, anchor = SE)
        D['Curr'] = Label(self.F('Name_Top'), textvariable = self.Curr, font = self.Fo('Title'), fg = 'white', bg = Col_title, bd = 0)
        D['Curr'].place(relx = 0.91, rely = 1, anchor = SE)
        D['Percent'] = Label(self.F('Name_Bot'), textvariable = self.Percent, font = self.Fo('SubTitle'), fg = 'white', bg = Col_title, bd = 0)
        D['Percent'].place(relx = 0.95, anchor = NE)
        D['UpDown'] = Label(self.F('Name_Bot'), font = self.Fo('SubTitle'), fg = Col_red, bg = Col_title, bd = 0)
        D['UpDown'].place(relx = 0.95, anchor = NW)

        P = self.F('Graph')
        self.fig = plt.figure(facecolor = Col_back)
        self.Canvas = FigureCanvasTkAgg(self.fig, P)
        self.Canvas.get_tk_widget().pack(fill = BOTH)
        self.anim = None

    def LoadDailyFrame(self):
        P = self.F('Daily')
        D = self.W('Daily')
        self.Frames['Daily_Menu'] = UIMaker.PackFix(Frame(P, height = 40, bg=Col_titleR), TOP, BOTH, NO)
        for i in range(1, 6):
            if(i % 2 == 0) :
                self.Frames['Daily_' + str(i)] = UIMaker.PackFix(Frame(P, height = 40, bg=Col_title), TOP, BOTH, NO)
            else :
                self.Frames['Daily_' + str(i)] = UIMaker.PackFix(Frame(P, height = 40, bg=Col_back), TOP, BOTH, NO)
        UIMaker.TextLabel(self.F('Daily_Menu'), '일자', self.Fo('Menu'), 'white', Col_titleR).place(relx = 0.05, rely = 0.5, anchor = W)
        UIMaker.TextLabel(self.F('Daily_Menu'), '종가(KRW)', self.Fo('Menu'), 'white', Col_titleR).place(relx = 0.20, rely = 0.5, anchor = W)
        UIMaker.TextLabel(self.F('Daily_Menu'), '전일대비', self.Fo('Menu'), 'white', Col_titleR).place(relx = 0.55, rely = 0.5, anchor = W)
        UIMaker.TextLabel(self.F('Daily_Menu'), '거래', self.Fo('Menu'), 'white', Col_titleR).place(relx = 0.78, rely = 0.5, anchor = W)      
        for i in range(0, 5):
            P = self.F('Daily_'+str(i + 1))
            Col = Col_title
            if(i % 2 == 0): Col = Col_back
            D[str(i)+'Day'] = Label(P, font = self.Fo('Items'), fg = 'white', bg = Col, bd = 0)
            D[str(i)+'Day'].place(relx = 0.05, rely = 0.5, anchor = W)
            D[str(i)+'KRW'] = Label(P, font = self.Fo('Menu'), fg = 'white', bg = Col, bd = 0)
            D[str(i)+'KRW'].place(relx = 0.2, rely = 0.5, anchor = W)
            D[str(i)+'Real'] = Label(P, font = self.Fo('Items'), fg = 'white', bg = Col, bd = 0)
            D[str(i)+'Real'].place(relx = 0.54, rely = 0.5, anchor = E)
            D[str(i)+'Percent'] = Label(P, font = self.Fo('Menu'), fg = 'white', bg = Col, bd = 0)
            D[str(i)+'Percent'].place(relx = 0.55, rely = 0.5, anchor = W)
            D[str(i)+'Buy'] = Label(P, font = self.Fo('Items'), fg = 'white', bg = Col, bd = 0)
            D[str(i)+'Buy'].place(relx = 0.78, rely = 0.5, anchor = W)

    def LoadCompareFrame(self):
        P = self.F('Compare')
        D = self.W('Compare')
        self.Frames['Compare_Menu'] = UIMaker.PackFix(Frame(P, height = 50, bg=Col_titleR), TOP, BOTH, NO)
        self.Frames['Compare_Info'] = UIMaker.PackFix(Frame(P, height = 38, bg = Col_back), TOP, BOTH, NO)
        for i in range(0, 10):
            Col = Col_back
            if(i % 2 == 1):
                Col = Col_title
            self.Frames['Compare_' + str(10 - i)] = UIMaker.PackFix(Frame(P, height = 38, bg = Col), BOTTOM, BOTH, NO)
        P = self.F('Compare_Menu')
        UIMaker.TextLabel(P, '비교목록', self.Fo('TitleM'), 'white', Col_titleR).place(relx = 0.05, rely = 0.5, anchor = W)
        D['Remove'] = Button(P, text = '─', font = self.Fo('Title'), width = 50, height = 50, bd = 0, highlightthickness=0, activebackground=Col_blue, 
                                          bg = Col_titleR, fg = Col_blue, image = self.IL.pixelVirtual, compound = CENTER)
        D['Remove'].pack(side = RIGHT)
        D['Add'] = Button(P, text = '+', font = self.Fo('Title'), width = 50, height = 50, bd = 0, highlightthickness=0, activebackground=Col_red, 
                                          bg = Col_titleR, fg = Col_red, image = self.IL.pixelVirtual, compound = CENTER)
        D['Add'].pack(side = RIGHT)
        P = self.F('Compare_Info')
        UIMaker.TextLabel(P, 'V', self.Fo('Menu'), 'white', Col_back).place(relx = 0.05, rely = 0.5, anchor = W)
        UIMaker.TextLabel(P, '이름', self.Fo('Menu'), 'white', Col_back).place(relx = 0.15, rely = 0.5, anchor = W)
        UIMaker.TextLabel(P, '현재가', self.Fo('Menu'), 'white', Col_back).place(relx = 0.5, rely = 0.5, anchor = W)
        UIMaker.TextLabel(P, '전일대비', self.Fo('Menu'), 'white', Col_back).place(relx = 0.8, rely = 0.5, anchor = W)

    def LoadFuncFrame(self):
        P = self.F('Functions')
        D = self.W('Functions')
        
        self.Frames['Function_Menu'] = UIMaker.PackFix(Frame(P, height = 40, bg = Col_titleR), TOP, BOTH, NO)
        self.Frames['Function_Buttons'] = UIMaker.PackFix(Frame(P, height = 81, bg = Col_titleR), TOP, BOTH, NO)
        self.Frames['Function_Dice'] = UIMaker.PackFix(Frame(P, height = 121, bg = Col_back), BOTTOM, BOTH, NO)        

        UIMaker.TextLabel(self.Frames['Function_Menu'], '기능', self.Fo('TitleM'), 'white', Col_titleR).place(relx = 0.05, rely = 0.5, anchor = W)
        
        P = self.F('Function_Buttons')
        D['Fav'] = Button(P, width = 118, height = 81, image = self.I('Fav_Off'), bg = Col_back, bd=0, relief = FLAT,
                                           highlightthickness=0, activebackground=Col_back, anchor='center',
                                           command =lambda: self.ChangeFunction('Fav'))
        D['Fav'].grid(row = 0, column = 0)
        D['Auto'] = Button(P, width = 118, height = 81, image = self.I('Auto_Off'), bg = Col_back, bd=0, relief = FLAT,
                                           highlightthickness=0, activebackground=Col_back, anchor='center',
                                           command =lambda: self.ChangeFunction('Auto'))
        D['Auto'].grid(row = 0, column = 1)
        D['Graph'] = Button(P, width = 118, height = 81, image = self.I('Graph_Off'), bg = Col_back, bd=0, relief = FLAT,
                                           highlightthickness=0, activebackground=Col_back, anchor='center',
                                           command =lambda: self.ChangeFunction('Graph'))
        D['Graph'].grid(row = 0, column = 2)
        
        P = self.F('Function_Dice')
        D['DiceImg'] = Button(P, width = 74, height = 74, image = self.I('dice_1'), bd = 0, relief = FLAT, highlightthickness=0, activebackground=Col_back, anchor = 'center',
                                                 command =lambda: self.DiceFunction())
        D['DiceImg'].place(relx = 0.1, rely = 0.5, anchor = W)
        D['DiceResult'] = Label(P, text = '운세 주사위 !', font = self.Fo('TitleMS'), fg = 'white', bg = Col_back)
        D['DiceResult'].place(relx = 0.9, rely = 0.5, anchor = SE)
        D['DiceComment'] = Label(P, text = '주사위를 굴려보세요', font = self.Fo('Items'), fg = 'white', bg = Col_back)
        D['DiceComment'].place(relx = 0.9, rely = 0.5, anchor = NE)

    def ChangeFunction(self, tag):
        if self.CurrCoin is None :
            return

        D = self.W('Functions')
        str = ''
        if tag is 'Fav':
            self.Fav = not self.Fav
            if self.Fav:
                str = tag + '_On'
            else:
                str = tag + '_Off'

        if tag is 'Auto':
            self.Auto = not self.Auto
            if self.Auto:
                str = tag + '_On'
            else:
                str = tag + '_Off'

        if tag is 'Graph':
            self.AniGraph = not self.AniGraph
            if self.AniGraph:
                str = tag + '_On'
                self.SetAniGraph()
            else:
                str = tag + '_Off'
                self.SetGraph()

        D[tag]['image'] = self.I(str)

    def DiceFunction(self):
        result = random.randint(1, 6)
        D = self.W('Functions')
        D['DiceImg']['image'] = self.I('dice_' + str(result))
        if result == 1 :
            D['DiceResult']['text'] = '1이 나왔네요!'
            D['DiceResult']['fg'] = Col_blue
            D['DiceComment']['text'] = '물리기 전에 손절하세요'
        if result == 2 :
            D['DiceResult']['text'] = '2가 나왔네요!'
            D['DiceResult']['fg'] = Col_blue
            D['DiceComment']['text'] = '좀 많이 안좋은거'
        if result == 3 :
            D['DiceResult']['text'] = '3이 나왔네요!'
            D['DiceResult']['fg'] = Col_blue
            D['DiceComment']['text'] = '적당히 안좋은거'
        if result == 4 :
            D['DiceResult']['text'] = '4가 나왔네요!'
            D['DiceResult']['fg'] = Col_red
            D['DiceComment']['text'] = '적당히 좋은거'
        if result == 5 :
            D['DiceResult']['text'] = '5가 나왔네요!'
            D['DiceResult']['fg'] = Col_red
            D['DiceComment']['text'] = '좀 좋은거'
        if result == 6 :
            D['DiceResult']['text'] = '6이 나왔네요!'
            D['DiceResult']['fg'] = Col_red
            D['DiceComment']['text'] = '개 좋은거'

    def ResetFunction(self):
        self.Auto = False
        self.Fav = False
        self.AniGraph = False

    def SetGraph(self):
        # 1분당        
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        self.GraphData.clear()
        self.GraphData = self.CurrCoin.getGraphData()
        self.x.clear()
        self.x = [datetime.now() - timedelta(minutes=i) for i in range(len(self.GraphData))]
        self.x.reverse()
        self.SetAxis('%H:%M')
        self.line, = self.ax.plot(self.x, self.GraphData, lw = 2)
        self.ax.ticklabel_format(axis='y', style='plain')
        if self.anim is not None:
            self.anim._stop()
        self.anim = FuncAnimation(self.fig, self.UpdateGraph, init_func = self.InitGraph, interval = 1000, frames = 60, blit = False)
        self.Canvas.draw()

    def UpdateGraph(self, i):
        self.GraphData.pop()
        self.GraphData.append(self.CurrCoin.getPrice())
        self.ax.relim()
        self.ax.autoscale_view()
        self.line.set_data(self.x, self.GraphData)
        return self.line

    def SetAniGraph(self):
        # 1초당
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        self.GraphData.clear()
        self.GraphData.append(self.CurrCoin.getPrice())
        self.x.clear()
        self.x = [datetime.now()]
        self.SetAxis('%H:%M:%S')
        self.line, = self.ax.plot(self.x, self.GraphData, lw = 2)
        self.ax.ticklabel_format(axis='y', style='plain')
        if self.anim is not None:
            self.anim._stop()
        self.anim = FuncAnimation(self.fig, self.UpdateAniGraph, init_func = self.InitAniGraph, interval = 1000, frames = 10, blit = False)
        self.Canvas.draw()

    def UpdateAniGraph(self, i):
        self.GraphData.append(self.CurrCoin.getPrice())
        self.x.append(datetime.now())
        if len(self.x) >= 60 :
            self.GraphData.pop(0)
            self.x.pop(0)
        self.ax.relim()
        self.ax.autoscale_view()
        self.line.set_data(self.x, self.GraphData)
        return self.line

    def InitGraph(self):
        self.GraphData.pop(0)
        self.GraphData.append(self.CurrCoin.getPrice())
        self.x.pop(0)
        self.x.append(datetime.now())
        return self.line

    def InitAniGraph(self):
        self.ax.ticklabel_format(axis='y', style='plain')
        return self.line

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

    def Fo(self, name):
        return self.Fonts[name]
    def I(self, name):
        return self.IL.Get(name)
    def F(self, name):
        return self.Frames[name]
    def W(self, name):
        return self.Widgets[name]
