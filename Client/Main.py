from tkinter import *
import MainGUI
        
window = Tk()
window.geometry("1024x768")
window.resizable(width=False, height=False)
        
MainUI = MainGUI.MainGUI(window)

window.mainloop()
