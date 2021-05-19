from tkinter import *
import tkinter.font
from . import GUIHelper

Col_title = '#3f3f3f'
Col_titleR = '#4a4a4a'
Col_back = '#333333'
Col_line0 = '#3b3b3b'
Col_line1 = '#353535'
Col_red = '#eb6148'
Col_blue = '#008dd2'
Col_SubFont = '#bbbbbb'

class Page:
    def __init__(self, parent):
        self.Frames = dict()
        #self.menu.pack(side = LEFT, fill = BOTH)
        self.Frames['Left'] = GUIHelper.PackFix(Frame(parent, width = 610, bg='red'), LEFT, BOTH, NO)
        self.Frames['Right'] = GUIHelper.PackFix(Frame(parent, width = 355, bg='blue'), RIGHT, BOTH, NO)
        
        P = self.Frames['Left']
        self.Frames['Name'] = GUIHelper.PackFix(Frame(P, height = 88, bg = 'yellow'), TOP, BOTH, NO)
        self.Frames['Graph'] = GUIHelper.PackFix(Frame(P, height = 380, bg = 'green'), TOP, BOTH, NO)
        self.Frames['Daily'] = GUIHelper.PackFix(Frame(P, bg = 'red'), TOP, BOTH, YES)

        P = self.Frames['Right']
        self.Frames['Compare'] = GUIHelper.PackFix(Frame(P, height = 468, bg = 'white'), TOP, BOTH, NO)
        self.Frames['Functions'] = GUIHelper.PackFix(Frame(P, bg = 'blue'), TOP, BOTH, YES)

        P = self.Frames