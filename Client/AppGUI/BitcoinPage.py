from tkinter import *

Col_border = '#4e4e4e'
Col_title = '#3f3f3f'
Col_back = '#333333'
Col_line0 = '#3b3b3b'
Col_line1 = '#353535'
Col_red = '#eb6148'
Col_blue = '#008dd2'

class Page:
    def __init__(self, parent):
        self.Parent = parent
        self.Setup_Frame()

    def Setup_Frame(self):
        self.Frames = dict()
        #self.menu = Frame(window, relief = RIDGE, width = 60, background = '#525967')
        #self.menu.pack(side = LEFT, fill = BOTH)
        self.Frames['Left'] = Frame(self.Parent, relief = RIDGE, width=610, height = 708, bg='red')
        self.Frames['Left'].pack(side=LEFT, fill=BOTH, expand = YES)
        self.Frames['Right'] = Frame(self.Parent, width=353, bg=Col_back)
        self.Frames['Right'].pack(side=RIGHT, fill=BOTH, expand = YES)

        #leftside
        self.Parent = self.Frames['Left']
        self.Frames['CoinTitle'] = Frame(self.Parent, height=88, bg=Col_title)
        self.Frames['CoinTitle'].pack(side=TOP, fill=BOTH)
