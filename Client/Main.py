from tkinter import *
import MainGUI
import MainData
        
window = Tk()
window.geometry("1024x768")
window.resizable(width=False, height=False)
        
UI = MainGUI.MainGUI(window)
Data = MainData.MainData(UI)

window.mainloop()
