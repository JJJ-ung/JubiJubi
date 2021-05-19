from tkinter import *
import tkinter.font

Col_border = '#4e4e4e'
Col_title = '#3f3f3f'
Col_titleR = '#4a4a4a'
Col_back = '#333333'
Col_line0 = '#3b3b3b'
Col_line1 = '#353535'
Col_red = '#eb6148'
Col_blue = '#008dd2'
Col_SubFont = '#bbbbbb'

class Page:
    def __init__(self, parent):
        self.Load_Resources()
        self.Setup_Frame(parent)
        self.Setup_CoinTitle(self.Frames['CoinTitle'])
        self.Setup_Graph(self.Frames['Graph'])
        self.Setup_Daily(self.Frames['DailyList'])
        self.Setup_Compare(self.Frames['CompareList'])

    def Load_Resources(self):
        #fonts
        self.Fonts = dict()
        self.Fonts['CoinName'] = tkinter.font.Font(family='NanumSquareEB', size=20, weight='bold')
        self.Fonts['TikerName'] = tkinter.font.Font(family='나눔스퀘어', size=10, weight='normal')    
        self.Fonts['Items'] = tkinter.font.Font(family='나눔스퀘어', size=12, weight='normal')    
        self.Fonts['Menu'] = tkinter.font.Font(family='나눔스퀘어', size=12, weight='bold')    

        #images
        self.Images = dict()
        self.Images['SampleCoin'] = PhotoImage(file = 'Image/sample.png')

    def Setup_Frame(self, parent):
        self.Frames = dict()
        self.Frames['Left'] = Frame(parent, relief = RIDGE, width=610, height = 708, bg=Col_back)
        self.Frames['Left'].pack(side=LEFT, fill=BOTH, expand = YES)
        self.Frames['Right'] = Frame(parent, relief = RIDGE, width=355, height = 708, bg=Col_back)
        self.Frames['Right'].pack(side=RIGHT, fill=BOTH, expand = YES)

        #leftside
        self.Frames['CoinTitle'] = Frame(self.Frames['Left'], relief = RIDGE, width = 610, height=88, bg=Col_title)
        self.Frames['CoinTitle'].pack(side=TOP, fill=BOTH) #620
        self.Frames['Graph'] = Frame(self.Frames['Left'], relief = RIDGE, width = 610, height=380, bg=Col_back)
        self.Frames['Graph'].pack(side=TOP, fill=BOTH) #240
        self.Frames['DailyList'] = Frame(self.Frames['Left'], relief = RIDGE, width = 610, height=240, bg=Col_title)
        self.Frames['DailyList'].pack(side=TOP, fill=BOTH) #240

        #rightside
        self.Frames['CompareList'] = Frame(self.Frames['Right'], relief = RIDGE, width = 355, height=468, bg=Col_back)
        self.Frames['CompareList'].pack(side=TOP, fill=BOTH) #620
        self.Frames['Functions'] = Frame(self.Frames['Right'], relief = RIDGE, width = 355, height=240, bg=Col_back)
        self.Frames['Functions'].pack(side=TOP, fill=BOTH) #620

    def Setup_CoinTitle(self, parent):
        #frame
        self.Frames['CoinTitleImg'] = Frame(parent, relief = RIDGE, bg=Col_title)
        self.Frames['CoinTitleImg'].pack(side = LEFT) #620

        self.Frames['CoinTitleTop'] = Frame(parent, relief = RIDGE, width = 550, height=50, bg=Col_title)
        self.Frames['CoinTitleTop'].pack(side = TOP) #620

        self.Frames['CoinTitleBot'] = Frame(parent, relief = RIDGE, width = 550, height=38, bg=Col_title)
        self.Frames['CoinTitleBot'].pack(side = BOTTOM) #620

        #widgets
        self.wCoinTitle = dict()
        self.wCoinTitle['CoinIcon'] = Label(self.Frames['CoinTitleImg'], image=self.Images['SampleCoin'], bg = Col_title, 
                                                                        width = 60, height=88, borderwidth=0)
        self.wCoinTitle['CoinIcon'].pack()

        self.wCoinTitle['CoinName'] = Label(self.Frames['CoinTitleTop'], 
                                                                            text='도지코인', fg='white', font=self.Fonts['CoinName'],
                                                                            bg = Col_title, borderwidth=0)
        self.wCoinTitle['CoinName'].place(x = 0, y = 55, anchor = SW)
        
        self.wCoinTitle['TikerName'] = Label(self.Frames['CoinTitleBot'],
                                                                            text='DOGE/KRW', fg=Col_SubFont, font=self.Fonts['TikerName'],
                                                                            bg = Col_title, borderwidth=0)
        self.wCoinTitle['TikerName'].place(x = 0, y = 0, anchor = NW)
                
        self.wCoinTitle['Current'] = Label(self.Frames['CoinTitleTop'], 
                                                                            text='607 KRW', fg=Col_red, font=self.Fonts['CoinName'],
                                                                            bg = Col_title, borderwidth=0)
        self.wCoinTitle['Current'].place(x = 350, y = 55, anchor = SW)

        self.wCoinTitle['Last'] = Label(self.Frames['CoinTitleBot'], 
                                                                            text='전일대비 +0.17% ▲ 1.00', fg=Col_red, font=self.Fonts['TikerName'],
                                                                            bg = Col_title, borderwidth=0)
        self.wCoinTitle['Last'].place(x = 350, y = 0, anchor = NW)
                
    def Setup_Graph(self, parent):
        self.Graph = Canvas(parent, width = 610, height=380, bg=Col_back, 
                                            bd=0, highlightthickness=0, relief='ridge')
        self.Graph.pack()
        self.Graph.create_line(0, 0, 610, 380, fill='red', width = 3)

    def Setup_Daily(self, parent):
        pad_date = 20
        pad_KRW = 50
        pad_Yest = 40
        pad_Deal = 86
        
        self.DailyMenu = list()
        self.DailyMenu.append(Label(parent, fg='white', font = self.Fonts['Menu'], bg=Col_title, borderwidth=0,
                                                        text = '일자'))
        self.DailyMenu[0].grid(row = 0, column = 0, ipadx = pad_date, ipady = 15,  sticky=NSEW)
        self.DailyMenu.append(Label(parent, fg='white', font = self.Fonts['Menu'], bg=Col_title, borderwidth=0,
                                                        text = '종가(KRW)'))
        self.DailyMenu[1].grid(row = 0, column = 1, ipadx = pad_KRW, ipady = 15,  sticky=NSEW)
        self.DailyMenu.append(Label(parent, fg='white', font = self.Fonts['Menu'], bg=Col_title, borderwidth=0,
                                                        text = '전일대비'))
        self.DailyMenu[2].grid(row = 0, column = 2, ipadx = pad_Yest, ipady = 15,  sticky=NSEW)
        self.DailyMenu.append(Label(parent, fg='white', font = self.Fonts['Menu'], bg=Col_title, borderwidth=0,
                                                        text = '거래'))
        self.DailyMenu[3].grid(row = 0, column = 3, ipadx = pad_Deal, ipady = 15,  sticky=NSEW)

        self.Daily_Date = list()
        self.InsertDailyList(parent, self.Daily_Date, 0, 0, 9, ' ')

        self.DailyKRW = list()
        self.InsertDailyList(parent, self.DailyKRW, 1, 0, 9, ' ')
 
        self.DailyLast = list()
        self.InsertDailyList(parent, self.DailyLast, 2, 0, 9, ' ')
       
        self.DailyDeals = list()
        self.InsertDailyList(parent, self.DailyDeals, 3, 0, 9, ' ')

    def InsertDailyList(self, parent, list, column, padX, padY, text):
        for i in range(0, 5):
            color = Col_back
            if i % 2 == 1:
                color = Col_title
            list.append(Label(parent, fg='white', font = self.Fonts['Items'], bg=color, borderwidth=0,
                                                        text = text))
            list[i].grid(row = i + 1, column = column, ipadx = padX, ipady = padY,  sticky=NSEW)

    def Setup_Compare(self, parent):
        self.wCompare = dict()
        self.wCompare['menu'] = Label(parent, width = 1, height = 1,
                                                                   text='비교목록', fg='white', font=self.Fonts['Menu'],
                                                                   bg = Col_titleR, borderwidth=0)
        self.wCompare['menu'].place(x = 0, y = 0, anchor = NW)