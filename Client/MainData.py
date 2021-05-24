import Stock
import Bitcoin
from AppGUI import StatusFrame

Coin = 0
Stock = 1
End = 2

class MainData(object):
    def __init__(self, UI):
        self.UI = UI   # 메인 UI 객체 담아둠
        self.CurrCoin = 0   # 현재 띄워진 비트코인
        self.CurrStock = 0  # 현재 띄워진 주식
        self.Favorites = [list(), list()]   # 즐겨찾기
        self.Compare = [list(), list()]  # 코인 비교목록
        self.BindUI()


    def BindUI(self):
        self.UI.StatusGUI.SearchButton.configure(command = lambda : self.Search(0))
        self.UI.StatusGUI.Searchbar.bind("<Return>", self.Search)
        self.CoinPage = self.UI.Pages['bitcoin']
        self.StockPage = self.UI.Pages['stock']


    # 실시간 업데이트
    def Update(self):
        self.Update_CoinUI(self.CurrCoin.Update())
        self.Update_StockUI(self.CurrStock.Update())
        for type in range(0, End) :
            for item in Favorites[type] :
                self.Update_FavUI(type, item.Update())
            for item in Compare[type]:
                self.Update_CompareUI(type, item.Update())

    # 검색기능
    def Search(self, event):
        type = self.UI.Get_CurrFrame()
        name = self.UI.StatusGUI.Searchbar.get() # 검색창에 입력한 이름
        if type == 'bitcoin':
            print('비트코인 확인')
            #여기에 검색하는 기능 추가, 위에 받아온 name으로 검색, Bitcoin 객체 받아오도록
            result = CoinInfo.SearchCoin(name)
            if result is not None:
                self.CurrCoin = Bitcoin(result)
            #self.UI.Pages[type].Change_Name(name) # 이제 name 대신 ㄴ
        if type == 'stock':
            print('주식 확인')
            #여기에 검색하는 기능 추가, 위에 받아온 name으로 검색, Stock 객체 받아오도록
            self.UI.Pages[type].Change_Name(name)

    def Update_CoinUI(self, item):
        pass

    def Update_StockUI(self, item):
        pass

    def Update_FavUI(self, type, item):
        pass

    def Update_CompareUI(self, type, item):
        pass
