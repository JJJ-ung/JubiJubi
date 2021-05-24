import pyupbit
import threading
import requests

class CoinInfo():
    data = requests.get("https://api.upbit.com/v1/market/all").json()

    def SearchCoin(str):
        for coin in CoinInfo.data:
            if coin['market'].startswith("KRW"):
                if coin['market'].lower().endswith(str.lower()) or coin['korean_name'] == str or coin['english_name'].lower() == str.lower():
                    return coin


class Bitcoin(threading.Thread):
    def __init__(self, info):
        self.ticker = info['marker']
        self.koreanName = info['korean_name']
        self.englishName = info['english_name']
        