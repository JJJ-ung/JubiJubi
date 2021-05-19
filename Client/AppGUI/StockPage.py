from tkinter import *

class Page:
    def __init__(self, parent):
        self.Test = Label(parent, text='Stock', height = 1)
        self.Test.place(relx=0.5, rely=0.5, anchor = CENTER)
