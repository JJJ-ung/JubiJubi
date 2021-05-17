from tkinter import *

Color_ListButton = '#464c58'
Color_ButtonIdle = '#525967'
Color_ButtonActive='#626a7b'

class Menu(object):
    def __init__(self, parent):
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
        self.Buttons['Liist'] = Button(parent, image=self.Images['liist'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ListButton, activebackground='#ff0000', anchor='center')
        self.Buttons['Liist'].pack(side=TOP)
        self.Buttons['Bitcoin'] = Button(parent, image=self.Images['bitcoin'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center')
        self.Buttons['Bitcoin'].pack(side=TOP)
        self.Buttons['Stock'] = Button(parent, image=self.Images['stock'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center')
        self.Buttons['Stock'].pack(side=TOP)
        self.Buttons['News'] = Button(parent, image=self.Images['news'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center')
        self.Buttons['News'].pack(side=TOP)
        self.Buttons['Favorites'] = Button(parent, image=self.Images['favorites'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center')
        self.Buttons['Favorites'].pack(side=TOP)
        
        #아래쪽 pack
        self.Buttons['Settings'] = Button(parent, image=self.Images['setting'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center')
        self.Buttons['Settings'].pack(side=BOTTOM)
        self.Buttons['Developer'] = Button(parent, image=self.Images['ghost'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center')
        self.Buttons['Developer'].pack(side=BOTTOM)
        self.Buttons['Profile'] = Button(parent, image=self.Images['profile'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center')
        self.Buttons['Profile'].pack(side=BOTTOM)
