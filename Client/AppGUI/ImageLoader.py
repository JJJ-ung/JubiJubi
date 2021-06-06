import urllib
import urllib.request
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk

class Loader:
    def Get(self, tag) :
        return self.Images[tag]

    def ImgFromURL(self, Path, width, height):
        if self.Images.get(Path) is not None:
            return self.Images[Path]
        u = urllib.request.urlopen(Path)
        raw_data=u.read()
        img = Image.open(BytesIO(raw_data))
        IconImg = ImageTk.PhotoImage(img.resize((width, height)))
        self.Images[Path] = IconImg
        return IconImg


    def __init__(self):
        self.Images = dict()
        self.pixelVirtual = PhotoImage(width = 1, height = 1)

        #icons
        self.Images['add'] = PhotoImage(file = 'Resources/icons/add.png')
        self.Images['auto'] = PhotoImage(file = 'Resources/icons/auto.png')
        self.Images['auto_on'] = PhotoImage(file = 'Resources/icons/auto_on.png')
        self.Images['bitcoin'] = PhotoImage(file = 'Resources/icons/bitcoin.png')
        self.Images['bookmark'] = PhotoImage(file = 'Resources/icons/bookmark.png')
        self.Images['bookmarksel'] = PhotoImage(file = 'Resources/icons/bookmark_sel.png')
        self.Images['boxminus'] = PhotoImage(file = 'Resources/icons/boxminus.png')
        self.Images['boxminus_small'] = PhotoImage(file = 'Resources/icons/boxminus_small.png')
        self.Images['boxplus'] = PhotoImage(file = 'Resources/icons/boxplus.png')
        self.Images['check_no'] = PhotoImage(file = 'Resources/icons/check_no.png')
        self.Images['check_yes'] = PhotoImage(file = 'Resources/icons/check_yes.png')
        self.Images['delete'] = PhotoImage(file = 'Resources/icons/delete.png')
        self.Images['dice'] = PhotoImage(file = 'Resources/icons/dice.png')
        self.Images['dice_on'] = PhotoImage(file = 'Resources/icons/dice_on.png')
        self.Images['graph'] = PhotoImage(file = 'Resources/icons/graph.png')
        self.Images['graph_on'] = PhotoImage(file = 'Resources/icons/graph_on.png')
        self.Images['favorites'] = PhotoImage(file = 'Resources/icons/favorites.png')
        self.Images['favorites_on'] = PhotoImage(file = 'Resources/icons/favorites_on.png')
        self.Images['ghost'] = PhotoImage(file = 'Resources/icons/ghost.png')
        self.Images['list'] = PhotoImage(file = 'Resources/icons/list.png')
        self.Images['minus'] = PhotoImage(file = 'Resources/icons/minus.png')
        self.Images['news'] = PhotoImage(file = 'Resources/icons/news.png')
        self.Images['profile'] = PhotoImage(file = 'Resources/icons/profile.png')
        self.Images['search'] = PhotoImage(file = 'Resources/icons/search.png')
        self.Images['setting'] = PhotoImage(file = 'Resources/icons/setting.png')
        self.Images['stock'] = PhotoImage(file = 'Resources/icons/stock.png')
        self.Images['email'] = PhotoImage(file = 'Resources/icons/email.png')
        self.Images['email1'] = PhotoImage(file = 'Resources/icons/email1.png')
        self.Images['telegram'] = PhotoImage(file = 'Resources/icons/telegram.png')

        #menu
        self.Images['logo'] = PhotoImage(file = 'Resources/menu/logo.png')
        self.Images['toggle0'] = PhotoImage(file = 'Resources/menu/toggle_0.png')
        self.Images['toggle1'] = PhotoImage(file = 'Resources/menu/toggle_1.png')
        #dice
        self.Images['dice_1'] = PhotoImage(file = 'Resources/dogedice/dice_1.png')
        self.Images['dice_2'] = PhotoImage(file = 'Resources/dogedice/dice_2.png')
        self.Images['dice_3'] = PhotoImage(file = 'Resources/dogedice/dice_3.png')
        self.Images['dice_4'] = PhotoImage(file = 'Resources/dogedice/dice_4.png')
        self.Images['dice_5'] = PhotoImage(file = 'Resources/dogedice/dice_5.png')
        self.Images['dice_6'] = PhotoImage(file = 'Resources/dogedice/dice_6.png')
        #buttons
        self.Images['Auto_Off'] = PhotoImage(file = 'Resources/buttons/Button0_Off.png')
        self.Images['Graph_Off'] = PhotoImage(file = 'Resources/buttons/Button1_Off.png')
        self.Images['Fav_Off'] = PhotoImage(file = 'Resources/buttons/Button2_Off.png')
        self.Images['Auto_On'] = PhotoImage(file = 'Resources/buttons/Button0_On.png')
        self.Images['Graph_On'] = PhotoImage(file = 'Resources/buttons/Button1_On.png')
        self.Images['Fav_On'] = PhotoImage(file = 'Resources/buttons/Button2_On.png')
        self.Images['Graph1_On'] = PhotoImage(file = 'Resources/buttons/Button3_On.png')
        self.Images['Graph1_Off'] = PhotoImage(file = 'Resources/buttons/Button3_Off.png')
        #images
        self.Images['sample'] = PhotoImage(file = 'Image/sample.png')
        self.Images['kiwoom'] = PhotoImage(file = 'Image/kiwoom.png')
        self.Images['upbit'] = PhotoImage(file = 'Image/upbit.png')