from tkinter import *

Color_ListButton = '#464c58'
Color_ButtonIdle = '#525967'
Color_ButtonActive='#626a7b'

class Menu(object):
    def __init__(self, parent, parentGUI, IL):
        self.ParentGUI = parentGUI
        self.IL = IL

        self.Buttons = dict()

        self.Buttons['Home'] = Label(parent, image=self.IL.Images['list'], bg = Color_ListButton, 
                                     height = 60, width = 60, borderwidth=0)
        self.Buttons['Home'].pack(side=TOP)
        self.Buttons['Favorites'] = Button(parent, image=self.IL.Images['bookmark'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda:  self.ChangePage('favorites'))
        self.Buttons['Favorites'].pack(side=TOP)
        self.Buttons['Bitcoin'] = Button(parent, image=self.IL.Images['bitcoin'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda:  self.ChangePage('bitcoin'))
        self.Buttons['Bitcoin'].pack(side=TOP)
        self.Buttons['Stock'] = Button(parent, image=self.IL.Images['stock'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda:  self.ChangePage('stock'))
        self.Buttons['Stock'].pack(side=TOP)
        self.Buttons['News'] = Button(parent, image=self.IL.Images['news'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda: self.ChangePage('news'))
        self.Buttons['News'].pack(side=TOP)
        self.Buttons['Auto'] = Button(parent, image=self.IL.Images['auto'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda: self.ChangePage('auto'))
        self.Buttons['Auto'].pack(side=TOP)
       
        #아래쪽 pack
        self.Buttons['Settings'] = Button(parent, image=self.IL.Images['setting'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda: self.ChangePage('settings'))
        self.Buttons['Settings'].pack(side=BOTTOM)
        self.Buttons['Developer'] = Button(parent, image=self.IL.Images['ghost'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda: self.ChangePage('developers'))
        self.Buttons['Developer'].pack(side=BOTTOM)
        self.Buttons['Profile'] = Button(parent, image=self.IL.Images['profile'],
                           height=60, width=60, borderwidth=0, highlightthickness=0,
                           bg=Color_ButtonIdle, activebackground=Color_ButtonActive, anchor='center',
                           command =lambda: self.ChangePage('profile'))
        self.Buttons['Profile'].pack(side=BOTTOM)


    def ChangePage(self, tag):
        self.ParentGUI.Show_Frame(tag)