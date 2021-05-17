from tkinter import *
from . import MenuFrame
from . import StatusFrame

class MainGUI :
    def __init__(self) :
        window = Tk()
        window.geometry("1024x768")

        self.menu = Frame(window, relief = RIDGE, width = 60, background = '#525967')
        self.menu.pack(side = LEFT, fill = BOTH)

        self.main = Frame(window)
        self.main.pack(side = RIGHT, fill = BOTH, expand = YES)

        self.status = Frame(self.main, height = 60, background = '#4d95dc')
        self.status.pack(side = TOP, fill = BOTH)

        self.page = Frame(self.main, background = 'white')
        self.page.pack(fill = BOTH, expand = YES)

        self.MenuGUI = MenuFrame.Menu(self.menu)
        self.StatusGUI = StatusFrame.Status(self.status)

        window.mainloop()
        