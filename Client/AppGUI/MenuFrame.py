from tkinter import *
from . import MainGUI

Color_ListButton = '#464c58'
Color_ButtonIdle = '#525967'
Color_ButtonActive='#626a7b'

class Menu(object):
    def __init__(self, parent, parentGUI):
        self.ParentGUI = parentGUI

        self.Images = dict()
        self.Images['auto'] = PhotoImage(file='Resources/icons/auto.png')
        self.Images['bitcoin'] = PhotoImage(file='Resources/icons/bitcoin.png')
        self.Images['bookmark'] = PhotoImage(file='Resources/icons/bookmark.png')
        self.Images['favorites'] = PhotoImage(file='Resources/icons/favorites.png')
        self.Images['ghost'] = PhotoImage(file='Resources/icons/ghost.png')
        self.Images['liist'] = PhotoImage(file='Resources/icons/list.png')
        self.Images['news'] = PhotoImage(file='Resources/icons/news.png')
        self.Images['profile'] = PhotoImage(file='Resources/icons/profile.png')
        self.Images['search'] = PhotoImage(file='Resources/icons/search.png')
        self.Images['setting'] = PhotoImage(file='Resources/icons/setting.png')
        self.Images['stock'] = PhotoImage(file='Resources/icons/stock.png')

        self.Buttons = dict()

        #위쪽 pack
        #self.Buttons['Home'] = Button(parent, image=self.Images['liist'],
        #                   height=60, width=60, borderwidth=0, highlightthickness=0,
        #                   bg=Color_ListButton, activebackground=Color_ButtonActive, anchor='center',
        #                   command =lambda: self.ChangePage('home'))
        self.Buttons['Home'] = Label(parent, image=self.Images['liist'], bg = Color_ListButton, 
                                     height = 60, width = 60, borderwidth=0)
        self.Buttons['Home'].pack(side=TOP)
        self.Buttons['Favorites'] = Button(parent, image=self.Images['bookmark'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda:  self.ChangePage('favorites'))
        self.Buttons['Favorites'].pack(side=TOP)
        self.Buttons['Bitcoin'] = Button(parent, image=self.Images['bitcoin'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda:  self.ChangePage('bitcoin'))
        self.Buttons['Bitcoin'].pack(side=TOP)
        self.Buttons['Stock'] = Button(parent, image=self.Images['stock'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda:  self.ChangePage('stock'))
        self.Buttons['Stock'].pack(side=TOP)
        self.Buttons['News'] = Button(parent, image=self.Images['news'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda: self.ChangePage('news'))
        self.Buttons['News'].pack(side=TOP)
        self.Buttons['Auto'] = Button(parent, image=self.Images['auto'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda: self.ChangePage('auto'))
        self.Buttons['Auto'].pack(side=TOP)
       
        #아래쪽 pack
        self.Buttons['Settings'] = Button(parent, image=self.Images['setting'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda: self.ChangePage('settings'))
        self.Buttons['Settings'].pack(side=BOTTOM)
        self.Buttons['Developer'] = Button(parent, image=self.Images['ghost'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda: self.ChangePage('developers'))
        self.Buttons['Developer'].pack(side=BOTTOM)
        self.Buttons['Profile'] = Button(parent, image=self.Images['profile'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda: self.ChangePage('profile'))
        self.Buttons['Profile'].pack(side=BOTTOM)


    def ChangePage(self, tag):
        self.ParentGUI.Show_Frame(tag)