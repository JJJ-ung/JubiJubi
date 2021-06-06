from tkinter import *
from cefpython3 import cefpython as cef
import threading

class Page:
    def __init__(self, parent, IL):
        self.URL = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=일론머스크"
        self.run = True
        self.browser = None
        self.parent = parent
        
        self.thread = threading.Thread(target=self.CreateBrowser)
        self.thread.setDaemon(True)
        self.thread.start()

    def CreateBrowser(self):
        sys.excepthook = cef.ExceptHook
        self.search = cef.WindowInfo(self.parent.winfo_id())
        self.search.SetAsChild(self.parent.winfo_id(), [0,0, 964, 708])
        cef.Initialize()
        self.browser = cef.CreateBrowserSync(self.search, url=self.URL)
        cef.MessageLoop()

    def Rest(self, searchbar):
        if self.browser != None:
            if self.run:
                self.run = False
                self.browser.StopLoad()
                searchbar.icursor(0)

    def Work(self):
        if self.browser != None:
            if not self.run:
                self.run = True
                self.browser.LoadUrl(self.URL)

    def Search(self, str):
        self.browser.StopLoad()
        self.URL = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=" + str
        self.browser.LoadUrl(self.URL)