from tkinter import *
import tkinter.font

Color_Back = '#4d95dc'

class Status(object):
    def __init__(self, parent):
        self.MainFont = tkinter.font.Font(family='나눔스퀘어라운드', size=10, weight='bold')

        self.Images=dict()
        self.Images['logo'] = PhotoImage(file='Resources/menu/logo.png')
        self.Images['searchbar'] = PhotoImage(file='Resources/menu/searchbar.png')
        self.Images['search'] = PhotoImage(file='Resources/menu/search.png')
        self.Images['toggle0'] = PhotoImage(file='Resources/menu/toggle_0.png')
        self.Images['toggle1'] = PhotoImage(file='Resources/menu/toggle_1.png')

        self.Logo = Label(parent, image=self.Images['logo'], width = 80, height = 60,
                                        bg = Color_Back, borderwidth=0)
        self.Logo.pack(side=LEFT)

        self.Searchbar = Label(parent,
                                        text='검색어를 입력해주세요', fg='#1e1e1e', compound='center', font=self.MainFont,
                                        image=self.Images['searchbar'], bg = Color_Back, borderwidth=0)
        self.Searchbar.pack(side=LEFT)

        self.SearchButton = Button(parent, image=self.Images['search'],
                           height=60, width=70, borderwidth=0, highlightthickness=0,
                           bg=Color_Back, activebackground=Color_Back, anchor='center')
        self.SearchButton.pack(side=LEFT)

        self.AutoON = True
        self.Toggle = Button(parent, image=self.Images['toggle0'],
                           width = 100, height=60, borderwidth=0, highlightthickness=0,
                           bg=Color_Back, activebackground=Color_Back, anchor='center', command=self.Click_Toggle)
        self.Toggle.pack(side=RIGHT)

    def Click_Toggle(self):
        if self.AutoON :
            self.Toggle['image'] = self.Images['toggle1']
        else :
            self.Toggle['image'] = self.Images['toggle0']
        self.AutoON = not self.AutoON
