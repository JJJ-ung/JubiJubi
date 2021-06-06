from tkinter import *
import sys
import os
from cefpython3 import cefpython as cef

class Page:
    def __init__(self, parent, IL):
        self.URL = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=일론머스크"
        self.run = True
        self.browser = None
        self.parent = parent
        self.CreateBrowser()

    def CreateBrowser(self):
        sys.excepthook = cef.ExceptHook
        self.search = cef.WindowInfo(self.parent.winfo_id())
        self.search.SetAsChild(self.parent.winfo_id(), [0,0, 964, 708])
        cef.Initialize()
        self.browser = cef.CreateBrowserSync(self.search, url=self.URL)

    def messageLoopWork(self):
        cef.MessageLoopWork()

    def Rest(self, searchbar):
        if self.browser != None:
            if self.run:
                self.run = False
                searchbar.focus_set()

    def Work(self, searchbar):
        if self.browser != None:
            if not self.run:
                self.run = True
                self.browser.LoadUrl(self.URL)
                searchbar.focus_set()

    def Search(self, str):
        self.browser.StopLoad()
        self.URL = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=" + str
        self.browser.LoadUrl(self.URL)