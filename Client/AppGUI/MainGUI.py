from tkinter import *
from . import MenuFrame
from . import StatusFrame
from . import BitcoinPage
from . import StockPage
from . import NewsPage
from . import FavoritesPage
from . import ProfilePage
from . import DevelopersPage
from . import SettingsPage
from . import AutoPage

Color_Page = '#333333'

class MainGUI :
    def __init__(self) :
        window = Tk()
        window.geometry("1024x768")
        window.resizable(width=False, height=False)

        self.menu = Frame(window, relief = RIDGE, width = 60, background = '#525967')
        self.menu.pack(side = LEFT, fill = BOTH)

        self.main = Frame(window)
        self.main.pack(side = RIGHT, fill = BOTH, expand = YES)

        self.status = Frame(self.main, height = 60, background = '#eb6148')
        self.status.pack(side = TOP, fill = BOTH)

        self.page = Frame(self.main, bg=Color_Page)
        self.page.pack(side=BOTTOM, fill=BOTH, expand=YES)

        self.SetUp_Frames(self.page)

        self.MenuGUI = MenuFrame.Menu(self.menu, self)
        self.StatusGUI = StatusFrame.Status(self.status)

        self.Pages = dict()
        self.Pages['bitcoin'] = BitcoinPage.Page(self.Frames['bitcoin'])
        self.Pages['stock'] = StockPage.Page(self.Frames['stock'])
        self.Pages['news'] = NewsPage.Page(self.Frames['news'])
        self.Pages['favorites'] = FavoritesPage.Page(self.Frames['favorites'])
        self.Pages['profile'] = ProfilePage.Page(self.Frames['profile'])
        self.Pages['developers'] = DevelopersPage.Page(self.Frames['developers'])
        self.Pages['settings'] = SettingsPage.Page(self.Frames['settings'])
        self.Pages['settings'] = AutoPage.Page(self.Frames['auto'])

        self.Show_Frame('stock')

        window.mainloop()


    def Show_Frame(self, page_name):
        frame=self.Frames[page_name]
        frame.tkraise()


    def SetUp_Frames(self, parent):
        self.Frames = dict()
        self.Frames['home'] = Frame(parent, background = Color_Page, width = 964, height = 708)
        self.Frames['home'].grid(row=0, column=0, sticky='nsew')
        self.Frames['home'].grid_propagate(0)
        self.Frames['bitcoin'] = Frame(parent, background = Color_Page, width = 964, height = 708)
        self.Frames['bitcoin'].grid(row=0, column=0, sticky='nsew')
        self.Frames['bitcoin'].grid_propagate(0)
        self.Frames['stock'] = Frame(parent, background = Color_Page, width = 964, height = 708)
        self.Frames['stock'].grid(row=0, column=0, sticky='nsew')
        self.Frames['stock'].grid_propagate(0)
        self.Frames['news'] = Frame(parent, background = Color_Page, width = 964, height = 708)
        self.Frames['news'].grid(row=0, column=0, sticky='nsew')
        self.Frames['news'].grid_propagate(0)
        self.Frames['favorites'] = Frame(parent, background = Color_Page, width = 964, height = 708)
        self.Frames['favorites'].grid(row=0, column=0, sticky='nsew')
        self.Frames['favorites'].grid_propagate(0)
        self.Frames['profile'] = Frame(parent, background = Color_Page, width = 964, height = 708)
        self.Frames['profile'].grid(row=0, column=0, sticky='nsew')
        self.Frames['profile'].grid_propagate(0)
        self.Frames['developers'] = Frame(parent, background = Color_Page, width = 964, height = 708)
        self.Frames['developers'].grid(row=0, column=0, sticky='nsew')
        self.Frames['developers'].grid_propagate(0)
        self.Frames['settings'] = Frame(parent, background = Color_Page, width = 964, height = 708)
        self.Frames['settings'].grid(row=0, column=0, sticky='nsew')
        self.Frames['settings'].grid_propagate(0)
        self.Frames['auto'] = Frame(parent, background = Color_Page, width = 964, height = 708)
        self.Frames['auto'].grid(row=0, column=0, sticky='nsew')
        self.Frames['auto'].grid_propagate(0)

