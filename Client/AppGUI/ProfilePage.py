from tkinter import *
import tkinter.font
from . import UIMaker
from . import ImageLoader
import Stock
import Bitcoin

import Mail
import TeleBot

Col_back = '#333333'


class Page:
    def __init__(self, parent, IL, fav):
        self.fav = fav

        self.Font1 = tkinter.font.Font(family='NanumSquareEB', size=12, weight='bold')
        self.Font2 = tkinter.font.Font(family='나눔스퀘어', size=20, weight='bold')
        self.Font3 = tkinter.font.Font(family='나눔스퀘어', size=12, weight='normal')

        Label(parent, width=865, height=80, text=' ', bg='#3f3f3f', bd=0, fg='white', image=IL.Get('kiwoom'),
              anchor='w', compound=LEFT, padx=40).place(x=10, y=10)
        Label(parent, width=865, height=80, text=' ', bg='#3f3f3f', bd=0, fg='white', image=IL.Get('upbit'), anchor='w',
              compound=LEFT, padx=40).place(x=10, y=100)
        Button(parent, text='  Login', font=self.Font1, width=100, height=30, bd=0, highlightthickness=0,
               command=self.StockLogin,
               activebackground='#eb6148', bg='#eb6148', fg='white', image=IL.Get('check_yes'), compound=LEFT).place(
            x=280, y=50, anchor=E)
        Button(parent, text='  Login', font=self.Font1, width=100, height=30, bd=0, highlightthickness=0,
               command=self.CoinLogin,
               activebackground='#eb6148', bg='#eb6148', fg='white', image=IL.Get('check_yes'), compound=LEFT).place(
            x=580, y=140, anchor=E)
        Label(parent, text=' Access Key ', bg='#3f3f3f', bd=0, font=self.Font1, fg='white', anchor='w').place(x=180,
                                                                                                              y=115)
        Label(parent, text=' Secret Key ', bg='#3f3f3f', bd=0, font=self.Font1, fg='white', anchor='w').place(x=180,
                                                                                                              y=145)
        self.access = Entry(parent, bd=0)
        self.access.place(x=300, y=115)
        self.secret = Entry(parent, bd=0, show='●')
        self.secret.place(x=300, y=145)

        self.GmailAddress = StringVar()
        Label(parent, text='Gmail  ', bg=Col_back, fg='white', bd=0, font = self.Font1).place(x=25, y=220)
        Entry(parent, textvariable = self.GmailAddress, width = 15).place(x = 100, y = 220)
        Label(parent, text='@gmail.com  ', bg=Col_back, fg='white', bd=0, font = self.Font1).place(x=220, y=220)
        Button(parent, image=IL.Get('email1'), bd=0, bg=Col_back, command = self.SendEmail).place(x=330, y=220)

        Label(parent, text='Telegram  ', bg=Col_back, fg='white', bd=0, font = self.Font1).place(x=500, y=220)
        Label(parent, text='주비주비', bg=Col_back, fg='white', bd=0, font = self.Font1).place(x=580, y=220)
        Button(parent, image=IL.Get('telegram'), bd=0, bg=Col_back).place(x=730, y=215)

    def StockLogin(self):
        Stock.StockInfo.Login()

    def CoinLogin(self):
        Bitcoin.CoinInfo.setKey(self.access.get(), self.secret.get())

    def SendEmail(self):
        Mail.Mail.SendEmail(self.GmailAddress.get(), self.fav)
        pass

    def SetTelegram(self, fav):
        TeleBot.TeleBot.SetFav(fav)
        pass