from tkinter import *

class MainGUI :
    def __init__(self) :
        #window = Tk()
        #self.image = PhotoImage(file='Image/pichu2.png')
        #self.lbl = Label(image=self.image)
        #self.lbl.pack()
        #frame = Frame(window)
        #frame.pack()
        #window.mainloop()
        root = Tk()
        root.geometry("1280x720+100+100")
        self.image = PhotoImage(file='Image/pichu2.png')
        frame = Frame(root)
        frame.pack(side="right")
        Pichu = Label(frame, image = self.image)
        Pichu.pack()

        root.mainloop()