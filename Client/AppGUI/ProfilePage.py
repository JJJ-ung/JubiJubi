from tkinter import *
import tkinter.font
from . import UIMaker
from . import ImageLoader
import Stock
import Bitcoin

Col_back = '#333333'

class Page:
    def __init__(self, parent, IL):
        self.Font1 = tkinter.font.Font(family='NanumSquareEB', size=12, weight='bold')
        self.Font2 = tkinter.font.Font(family='나눔스퀘어', size=20, weight='bold')

        Label(parent, width = 865, height = 80, text = ' ', bg = '#3f3f3f', bd = 0,fg = 'white', image = IL.Get('kiwoom'), anchor = 'w', compound = LEFT, padx = 40).place(x = 10, y = 10)
        Label(parent, width = 865, height = 80, text = ' ', bg = '#3f3f3f', bd = 0,fg = 'white', image = IL.Get('upbit'), anchor = 'w', compound = LEFT, padx = 40).place(x = 10, y = 100)
        Button(parent, text = '  Login', font = self.Font1, width = 100, height = 30, bd = 0, highlightthickness=0, command=self.StockLogin,
               activebackground='#eb6148', bg = '#eb6148', fg = 'white', image = IL.Get('check_yes'), compound = LEFT).place(x = 280, y = 50, anchor = E)
        Button(parent, text = '  Login', font = self.Font1, width = 100, height = 30, bd = 0, highlightthickness=0, command=self.CoinLogin,
               activebackground='#eb6148', bg = '#eb6148', fg = 'white', image = IL.Get('check_yes'), compound = LEFT).place(x = 580, y = 140, anchor = E)
        Label(parent, text = ' Access Key ', bg = '#3f3f3f', bd = 0, font = self.Font1, fg = 'white', anchor = 'w').place(x = 180, y = 115)
        Label(parent, text = ' Secret Key ', bg = '#3f3f3f', bd = 0, font = self.Font1, fg = 'white', anchor = 'w').place(x = 180, y = 145)
        self.access = Entry(parent, bd = 0)
        self.access.place(x = 300, y = 115)
        self.secret = Entry(parent, bd = 0, show = '●')
        self.secret.place(x = 300, y = 145)
        #self.Widgets.append(Label(parent, image = IL.Get('kiwoom'), bg = Col_back, bd = 0))
        #self.Widgets[0].place(relx = 0.25, y = 96, anchor = E)
        #self.Widgets.append(Label(parent, image = IL.Get('upbit'), bg = Col_back, bd = 0))
        #self.Widgets[1].place(relx = 0.25, y = 200, anchor = E)
        #self.Widgets.append(Button(parent, text = 'Login', font = self.Font, width = 145, height = 38, bd = 0, highlightthickness=0, activebackground='#eb6148', 
        #                                  bg = '#3f3f3f', fg = 'white', image = IL.Get('check_yes'), compound = LEFT))
        #self.Widgets[2].place(x = 284, y = 96, anchor = W)height = 80, , image = IL.pixelVirtual

    def StockLogin(self):
        Stock.StockInfo.Login()
    
    def CoinLogin(self):
        Bitcoin.CoinInfo.setKey(self.access.get(), self.secret.get())
         