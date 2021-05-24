from tkinter import *
import MainGUI
import MainData
import threading
import time
        
class Main:
    def __init__(self):
        self.wnd = Tk()
        self.wnd.geometry("1024x768")
        self.wnd.resizable(width=False, height=False)
        self.UI = MainGUI.MainGUI(self.wnd)
        self.Data = MainData.MainData(self.UI)
        self.count = 0
        self.Update()
        self.wnd.mainloop()

    def Update(self):
        self.count += 1
        print(self.count)
        self.Data.Update()
        #now = time.strftime("%H:%M:%S")
        #print(now)
        self.wnd.after(1000, self.Update)
        #timer = threading.Timer(1, self.Update)
        #timer.start()

Main()