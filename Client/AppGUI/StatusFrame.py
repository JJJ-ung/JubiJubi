from tkinter import *
import tkinter.font

Color_Back = '#eb6148'

class Status(object):
    def __init__(self, parent, Main, Stock, Bitcoin, IL):
        self.Main = Main
        self.Stock = Stock
        self.Bitcoin = Bitcoin
        self. IL = IL
        self.SearchStr = ''
        self.MainFont = tkinter.font.Font(family='나눔스퀘어', size=10, weight='bold')
        self.SubFont = tkinter.font.Font(family='나눔스퀘어', size=10, weight='normal')

        self.Images=dict()
        self.Images['logo'] = PhotoImage(file='Resources/menu/logo.png')
        self.Images['searchbar'] = PhotoImage(file='Resources/menu/searchbar.png')
        self.Images['search'] = PhotoImage(file='Resources/icons/search.png')
        self.Images['toggle0'] = PhotoImage(file='Resources/menu/toggle_0.png')
        self.Images['toggle1'] = PhotoImage(file='Resources/menu/toggle_1.png')

        self.Logo = Label(parent, image=self.IL.Images['logo'], width = 80, height = 60,
                                        bg = Color_Back, borderwidth=0)
        self.Logo.pack(side=LEFT)

        self.Searchbar = Entry(parent, bd = 0)
        self.Searchbar.bind("<Return>", self.Click_Search)
        self.Searchbar.place(relx = 0.085, rely = 0.5, anchor = W, width = 400, height = 22)

        self.SearchButton = Button(parent, image=self.IL.Images['search'],
                           height=60, width=70, borderwidth=0, highlightthickness=0,
                           bg=Color_Back, activebackground=Color_Back, anchor='center', command = lambda: self.Click_Search(0))
        self.SearchButton.place(relx = 0.5, rely = 0.5, anchor = W)

        self.AutoON = True
        self.Toggle = Button(parent, image=self.IL.Images['toggle0'],
                           width = 100, height=60, borderwidth=0, highlightthickness=0,
                           bg=Color_Back, activebackground=Color_Back, anchor='center', command=self.Click_Toggle)
        self.Toggle.pack(side=RIGHT)


    def Click_Search(self, event):
        self.Searchbar['text'] = "앙 눌림"
        if self.Main.CurrFrame == 'bitcoin' :
            print('비트코인')
            self.Bitcoin.Change_Name(self.Searchbar.get())
        if self.Main.CurrFrame == 'stock' :
            print('주식')
            self.Stock.Change_Name(self.Searchbar.get())


    def Click_Toggle(self):
        if self.AutoON :
            self.Toggle['image'] = self.IL.Images['toggle1']
        else :
            self.Toggle['image'] = self.IL.Images['toggle0']
        self.AutoON = not self.AutoON
