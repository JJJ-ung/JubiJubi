import re
import sys
import random
from tkinter import *
from datetime import *
import tkinter.font
from . import UIMaker
from . import ImageLoader
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import *
from matplotlib.animation import *
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import *
sys.path.append('/Bitcoin.py')
import Bitcoin

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
    def Update_CurrInfo(self, coin):
        now = coin.getPrice()
        change = now - self.Yesterday
        self.Curr.set(str(now))       
        self.Percent.set(str(round((change / self.Yesterday) * 100, 2)) + '%')
        if change > 0 : self.Widgets['Name']['UpDown'].configure(text = '▲', fg = Col_red)
        else : self.Widgets['Name']['UpDown'].configure(text = '▼', fg = Col_blue)

    def Set_CurrInfo(self, coin):
        D = self.W('Name')
        self.CurrCoin = coin
        self.Yesterday = coin.lstDailyData[4]

        self.SetGraph()

        ImagePath = 'https://static.upbit.com/logos/' + re.sub("KRW-", "", coin.ticker) + '.png'
        self.Widgets['Name']['Icon'].configure(image = self.IL.ImgFromURL(ImagePath, 25, 25))

        D['Name']['text'] = coin.koreanName
        D['Tiker']['text'] =  coin.ticker + '/' + coin.englishName

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

    ##################################################################################################################
    #   이니셜라이즈
    ##################################################################################################################


    def __init__(self, parent, IL):
        self.IL = IL
        self.Frames = dict()
        self.Widgets = {'Name' : dict(), 'Graph' : dict(), 'Daily' : dict(), 'Compare' : dict(), 'Functions' : dict()}
        self.DailyData = list()

        self.Curr = StringVar()
        self.Percent = StringVar()
        self.UpDown = StringVar()
        self.Yesterday = 0

        self.GraphData = list()

    ##################################################################################################################
    #  폰트 로드
    ##################################################################################################################
        self.Fonts = dict()
        self.Fonts['Title'] = tkinter.font.Font(family='NanumSquareEB', size=20, weight='bold')
        self.Fonts['TitleS'] = tkinter.font.Font(family='NanumSquareEB', size=10, weight='bold')
        self.Fonts['TitleM'] = tkinter.font.Font(family='NanumSquareEB', size=13, weight='bold')
        self.Fonts['TitleMS'] = tkinter.font.Font(family='NanumSquareEB', size=18, weight='bold')
        self.Fonts['SubTitle'] = tkinter.font.Font(family='나눔스퀘어', size=10, weight='normal')    
        self.Fonts['Items'] = tkinter.font.Font(family='나눔스퀘어', size=10, weight='normal')    
        self.Fonts['Menu'] = tkinter.font.Font(family='나눔스퀘어', size=10, weight='bold')    

    ##################################################################################################################
    #   메인 정보
    ##################################################################################################################
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

    ##################################################################################################################
    #   그래프
    ##################################################################################################################


        P = self.F('Graph')

        self.fig = plt.figure(facecolor = Col_back)
        Canvas = FigureCanvasTkAgg(self.fig, P)
        Canvas.get_tk_widget().pack(fill = BOTH)
        self.anim = None


    ##################################################################################################################
    #   일일 정보
    ##################################################################################################################


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


    ##################################################################################################################
    #   비교 칸
    ##################################################################################################################


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


    ##################################################################################################################
    #   기능 칸
    ##################################################################################################################


        P = self.F('Functions')
        D = self.W('Functions')
        self.Frames['Function_Menu'] = UIMaker.PackFix(Frame(P, height = 40, bg = Col_titleR), TOP, BOTH, NO)
        UIMaker.TextLabel(self.Frames['Function_Menu'], '기능', self.Fo('TitleM'), 'white', Col_titleR).place(relx = 0.05, rely = 0.5, anchor = W)
        self.Frames['Function_Buttons'] = UIMaker.PackFix(Frame(P, height = 81, bg = Col_titleR), TOP, BOTH, NO)
        self.Frames['Function_Fav'] = Frame(P, height = 121, bg = Col_back)
        self.Frames['Function_Fav'].pack_propagate(0)
        self.Frames['Function_Auto'] = Frame(P, height = 121, bg = 'yellow')
        self.Frames['Function_Auto'].pack_propagate(0)
        self.Frames['Function_Dice'] = Frame(P, height = 121, bg = Col_back)
        self.Frames['Function_Dice'].pack_propagate(0)

        P = self.F('Function_Buttons')
        D['Fav'] = Button(P, width = 118, height = 81, image = self.I('Fav_Off'), bg = Col_back, bd=0, relief = FLAT,
                                           highlightthickness=0, activebackground=Col_back, anchor='center',
                                           command =lambda: self.ChangeFunction('Fav'))
        D['Fav'].grid(row = 0, column = 0)
        D['Auto'] = Button(P, width = 118, height = 81, image = self.I('Auto_Off'), bg = Col_back, bd=0, relief = FLAT,
                                           highlightthickness=0, activebackground=Col_back, anchor='center',
                                           command =lambda: self.ChangeFunction('Auto'))
        D['Auto'].grid(row = 0, column = 1)
        D['Dice'] = Button(P, width = 118, height = 81, image = self.I('Dice_On'), bg = Col_back, bd=0, relief = FLAT,
                                           highlightthickness=0, activebackground=Col_back, anchor='center',
                                           command =lambda: self.ChangeFunction('Dice'))
        D['Dice'].grid(row = 0, column = 2)
        self.Frames['Curr'] = self.Frames['Function_Dice']
        self.Frames['Curr'].pack(side = TOP, fill = BOTH)

        P = self.F('Function_Dice')
        D['DiceImg'] = Button(P, width = 74, height = 74, image = self.I('dice_1'), bd = 0, relief = FLAT, highlightthickness=0, activebackground=Col_back, anchor = 'center',
                                                 command =lambda: self.DiceFunction())
        D['DiceImg'].place(relx = 0.1, rely = 0.5, anchor = W)
        D['DiceResult'] = Label(P, text = '운세 주사위 !', font = self.Fo('TitleMS'), fg = 'white', bg = Col_back)
        D['DiceResult'].place(relx = 0.9, rely = 0.5, anchor = SE)
        D['DiceComment'] = Label(P, text = '주사위를 굴려보세요', font = self.Fo('Items'), fg = 'white', bg = Col_back)
        D['DiceComment'].place(relx = 0.9, rely = 0.5, anchor = NE)

        P = self.F('Function_Fav')
        D['FavAdd'] = Button(P, width = 340, height = 60, image = self.I('boxplus'), bd = 0, relief = FLAT, highlightthickness=0, bg = Col_back, activebackground=Col_title, anchor='w')
        D['FavAdd'].place(relx = 0.02, rely = 0.5, anchor = SW)

    def ChangeFunction(self, tag):
        D = self.W('Functions')
        D['Fav']['image'] = self.I('Fav' + '_Off')
        D['Dice']['image'] = self.I('Dice' + '_Off')
        D['Auto']['image'] = self.I('Auto' + '_Off')
        D[tag]['image'] = self.I(tag + '_On')
        self.Frames['Curr'].pack_forget()
        self.Frames['Curr'] = self.Frames['Function_' + tag]
        self.Frames['Curr'].pack(side = TOP, fill = BOTH)

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


    ##################################################################################################################
    #   귀차니즘 함수
    ##################################################################################################################


    def Fo(self, name):
        return self.Fonts[name]
    def I(self, name):
        return self.IL.Get(name)
    def F(self, name):
        return self.Frames[name]
    def W(self, name):
        return self.Widgets[name]


    ##################################################################################################################
    #   그래프 함수
    ##################################################################################################################

    def Animate(self, i):
        #self.ax.relim()
        #self.ax.autoscale()
        self.line.set_data(self.x, self.y)
        #self.ax.set_xlim(self.x[0], self.x[len(self.x)-1])
        return (self.line,)

    def SetGraph(self):
        plt.clf()
        self.ax = plt.subplot(111)
        self.ax.set_facecolor(Col_back)
        self.ax.spines['bottom'].set_color('#dddddd')
        self.ax.spines['top'].set_color(Col_back) 
        self.ax.spines['right'].set_color(Col_back)
        self.ax.spines['left'].set_color('#dddddd')
        self.ax.tick_params(axis='x', colors='#dddddd')
        self.ax.tick_params(axis='y', colors='#dddddd')
        self.GraphData = self.CurrCoin.graphData
        self.x = [datetime.now() - timedelta(minutes=i) for i in range(len(self.GraphData))]
        self.x.reverse()
        self.ax.set_xlim(self.x[0], self.x[len(self.x)-1])
        low = self.CurrCoin.getLow()
        high = self.CurrCoin.getHigh()
        curr = self.CurrCoin.getPrice()
        self.ax.set_ylim(self.CurrCoin.getLow(), self.CurrCoin.getHigh())
        self.line, = self.ax.plot([], [], lw=2)
        if self.anim is not None:
            self.anim._stop()
        self.anim = FuncAnimation(self.fig, self.Animate, init_func=self.init, interval=100, frames=600, blit=True)
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        self.ax.ticklabel_format(axis='y', style='plain')
        self.ax.grid(True, color = 'white', alpha = 0.1)
        plt.gcf().autofmt_xdate()

    def init(self):
        print('그래프업데이트')
        self.GraphData.pop(0)
        self.GraphData.append(self.CurrCoin.getPrice())
        #self.x = [datetime.now() - timedelta(minutes=i) for i in range(len(self.GraphData))]
        self.y = self.GraphData
        print(self.GraphData)
        self.x = [datetime.now() - timedelta(minutes=i) for i in range(len(self.GraphData))]

        return (self.line, )