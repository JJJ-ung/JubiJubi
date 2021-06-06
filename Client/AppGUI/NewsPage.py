from tkinter import *
from cefpython3 import cefpython as cef
import threading

class Page:
    def __init__(self, parent, IL):
        self.URL = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=일론머스크"
        self.run = True
        
        sys.excepthook = cef.ExceptHook
        self.search = cef.WindowInfo(parent.winfo_id())
        self.search.SetAsChild(parent.winfo_id(), [0,0, 964, 708])

        self.Search()

        #self.thread = threading.Thread(target=self.Search)
        #self.thread.setDaemon(True)
        #self.thread.start()

    def Search(self):
        cef.Initialize(settings={"multi_threaded_message_loop": True})
        self.browser = cef.CreateBrowserSync(self.search, url=self.URL)

    def Rest(self):
        if self.run:
            self.run = False

    def Work(self):
        if not self.run:
            self.run = True
            #self.thread = threading.Thread(target=self.Search)
            #self.thread.setDaemon(True)
            #self.thread.start()
