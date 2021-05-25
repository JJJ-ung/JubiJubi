from tkinter import *
import MainGUI
import MainData
import threading
import time
        
class Main():
    def __init__(self):
        self.wnd = Tk()
        self.wnd.geometry("1024x768")
        self.wnd.resizable(width=False, height=False)
        self.UI = MainGUI.MainGUI(self.wnd)
        self.Data = MainData.MainData(self.UI)
        self.Update()
        self.wnd.mainloop()

    def Update(self):
        self.Data.Update()
        self.wnd.after(100, self.Update)

Main()