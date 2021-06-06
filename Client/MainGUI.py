from tkinter import *
from AppGUI import MenuFrame
from AppGUI import StatusFrame
from AppGUI import BitcoinPage
from AppGUI import StockPage
from AppGUI import NewsPage
from AppGUI import FavoritesPage
from AppGUI import ProfilePage
from AppGUI import DevelopersPage
from AppGUI import SettingsPage
from AppGUI import AutoPage
from AppGUI import ImageLoader

#Color_Page = '#333333'
Color_Page = '#3f3f3f'

class MainGUI :
    def __init__(self, window) :
        self.IL = ImageLoader.Loader()

        self.menu = Frame(window, relief = RIDGE, width = 60, background = '#525967')
        self.menu.pack(side = LEFT, fill = BOTH)

        self.main = Frame(window)
        self.main.pack(side = RIGHT, fill = BOTH, expand = YES)

        self.status = Frame(self.main, height = 60, background = '#eb6148')
        self.status.pack(side = TOP, fill = BOTH)

        self.page = Frame(self.main, bg=Color_Page)
        self.page.pack(side=BOTTOM, fill=BOTH, expand=YES)

        self.SetUp_Frames(self.page)

        self.CurrFrame = ''

        self.Pages = dict()
        self.Pages['favorites'] = FavoritesPage.Page(self.Frames['favorites'], self.IL)
        self.Pages['bitcoin'] = BitcoinPage.Page(self.Frames['bitcoin'], self.IL, self.Pages['favorites'])
        self.Pages['stock'] = StockPage.Page(self.Frames['stock'], self.IL, self.Pages['favorites'])
        self.Pages['news'] = NewsPage.Page(self.Frames['news'], self.IL)
        self.Pages['profile'] = ProfilePage.Page(self.Frames['profile'], self.IL)
        self.Pages['developers'] = DevelopersPage.Page(self.Frames['developers'], self.IL)
        self.Pages['settings'] = SettingsPage.Page(self.Frames['settings'], self.IL)
        self.Pages['settings'] = AutoPage.Page(self.Frames['auto'], self.IL)

        self.MenuGUI = MenuFrame.Menu(self.menu, self, self.IL)
        self.StatusGUI = StatusFrame.Status(self.status, self, self.IL)

        self.Show_Frame('favorites')


    def Get_CurrFrame(self):
        return self.CurrFrame


    def GetPage(self, tag):
        return self.Pages[tag]


    def Show_Frame(self, page_name):
        self.CurrFrame = page_name
        self.Frames[page_name].tkraise()


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
        self.Frames['profile'] = Frame(parent, background = '#333333', width = 964, height = 708)
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

