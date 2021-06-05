from tkinter import *
import MainGUI
import MainData
import threading
import time
import sys
        
class Main():
    def __init__(self):
        self.wnd = Tk()
        self.wnd.geometry("1024x768")
        self.wnd.resizable(width=False, height=False)
        self.UI = MainGUI.MainGUI(self.wnd)
        self.Data = MainData.MainData(self.UI)
        self.UpdateCoin()
        self.UpdateStock()
        print(sys.version)
        self.wnd.mainloop()
        
    def UpdateCoin(self):
        self.Data.UpdateCoin()
        self.wnd.after(100, self.UpdateCoin)
    
    def UpdateStock(self):
        self.Data.UpdateStock()
        self.wnd.after(1000, self.UpdateStock)
       

Main()
