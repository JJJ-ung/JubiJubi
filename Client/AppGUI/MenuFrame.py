from tkinter import *

class Menu(object):
    def __init__(self, parent):
        self.image_auto_idle = PhotoImage(file='Resources/buttons/auto_0.png')
        self.button_auto = Button(parent, image = self.image_auto_idle, borderwidth = 0, highlightthickness=0)
        self.button_auto.pack(side = TOP)