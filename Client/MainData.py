import Stock
import Bitcoin
import threading
from AppGUI import StatusFrame

class MainData(object):
    def __init__(self, UI):
        self.UI = UI   # 메인 UI 객체 담아둠
        #self.CurrCoin = 0   # 현재 띄워진 비트코인
        #self.CurrStock = 0  # 현재 띄워진 주식
        self.Favorites = [list(), list()]   # 즐겨찾기
        self.Compare = [list(), list()]  # 코인 비교목록
        self.BindUI()

    def BindUI(self):
        self.UI.StatusGUI.SearchButton.configure(command = lambda : self.Search(0))
        self.UI.StatusGUI.Searchbar.bind("<Return>", self.Search)
        self.CoinPage = self.UI.Pages['bitcoin']
        self.StockPage = self.UI.Pages['stock']

    # 실시간 업데이트
    def UpdateCoin(self):
        self.UI.Pages['bitcoin'].UpdateCurr()

    def UpdateStock(self):
        self.UI.Pages['stock'].UpdateCurr()

    def UpdateNews(self):
        self.UI.Pages['news'].messageLoopWork()
        #if self.UI.Get_CurrFrame() != 'news':
        #    self.UI.Pages['news'].Rest(self.UI.StatusGUI.Searchbar)
        #else:
        #    self.UI.Pages['news'].Work(self.UI.StatusGUI.Searchbar)

    # 검색기능
    def Search(self, event):
        type = self.UI.Get_CurrFrame()
        name = self.UI.StatusGUI.SearchStr.get() # 검색창에 입력한 이름

        if type == 'bitcoin':
            print('비트코인 확인')
            result = Bitcoin.CoinInfo.SearchCoin(name)
            if result is not None:
                CurrCoin = Bitcoin.Bitcoin(result)
                self.UI.Pages[type].SetCurr(CurrCoin)
                self.UI.StatusGUI.Searchbar['fg'] = 'black'
            else :
                self.UI.StatusGUI.Searchbar['fg'] = 'red'

        if type == 'stock':
            if Stock.StockInfo.login == True:
                print('주식 확인')
                result = Stock.StockInfo.SearchStock(name)
                if result is not None:
                    CurrStock = Stock.Stock(result)
                    self.UI.Pages[type].SetCurr(CurrStock)
                    self.UI.StatusGUI.Searchbar['fg'] = 'black'
                else :
                    self.UI.StatusGUI.Searchbar['fg'] = 'red'
            else :
                self.UI.StatusGUI.Searchbar.configure(fg = 'red')
                self.UI.StatusGUI.SearchStr.set('로그인을 진행해주세요')

                
        if type == 'news':
            self.UI.Pages['news'].Search(name)