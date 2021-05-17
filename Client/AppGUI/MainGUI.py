from tkinter import *
from . import HomeWnd

class MainGUI :
    def __init__(self) :
        #window = Tk()
        #self.image = PhotoImage(file='Image/pichu2.png')
        #self.lbl = Label(image=self.image)
        #self.lbl.pack()
        #frame = Frame(window)
        #frame.pack()
        #window.mainloop()

        #root = Tk()
        #root.geometry("1280x720+100+100")
        #self.image = PhotoImage(file='Image/pichu2.png')
        #frame = Frame(root)
        #frame.pack(side="right")
        #Pichu = Label(frame, image = self.image)
        #Pichu.pack()

        #root.mainloop()
        
        window = Tk()
        window.geometry("1024x768")

        self.menu = Frame(window, width = 60, height = 768, background = '#525967')
        self.menu.pack(side = LEFT)

        self.main = Frame(window, width = 964, height = 768)
        self.main.pack(side = RIGHT)

        self.status = Frame(self.main, width = 964, height = 60, background = '#4d95dc')
        self.status.pack(side = TOP)

        self.page = Frame(self.main, width = 964, height = 708, background = 'white')
        self.page.pack(side = BOTTOM)

        #self.homewnd = HomeWnd(self.main)

        window.mainloop()
