import xml
import json
import re
import fake_useragent
import requests
import time
import random
from bs4 import BeautifulSoup


ua = fake_useragent.UserAgent()

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Cookie': 'ActListPageSize=10; enableSIH=true; steamLoginSecure=76561199142306040%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MENGMl8yMjAzNEJCM181RTE0QiIsICJzdWIiOiAiNzY1NjExOTkxNDIzMDYwNDAiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY3NTYxOTM1NCwgIm5iZiI6IDE2NjY4OTE4MzYsICJpYXQiOiAxNjc1NTMxODM2LCAianRpIjogIjBDRjRfMjIwMzRCQUFfNzEwQTAiLCAib2F0IjogMTY3NTUzMTgzNiwgInJ0X2V4cCI6IDE2OTM3MTIzOTYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIxNzguNDYuMTAzLjE4NyIsICJpcF9jb25maXJtZXIiOiAiMTc4LjQ2LjEwMy4xODciIH0.5wYQHMCqns4IuPKKpISTcIpfWQGfVKt0gJJRsgt0hnSVshLDDwLyybaz1XGLZBf67NDWhbrZej7C2s_Z0pT_Bw; browserid=2716269035775147421; timezoneOffset=18000,0; _ga=GA1.2.1729894480.1675531847; _gid=GA1.2.481607494.1675531847; strInventoryLastContext=730_2; sessionid=feb965c88a82165d11dee81c; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1675555537%7D; steamCurrencyId=5; steamCountry=RU%7C98f1609d8252010311af57ee025fd495',
    'If-Modified-Since': 'Sun, 05 Feb 2023 09:33:05 GMT',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': ua.random,
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }


def get_full_data(url_page, headers):
    time.sleep(random.randint(6, 10))
    rs = requests.get(url_page, headers=headers)
    m = re.search(r'var line1=(.+);', rs.text)
    data_str = m.group(1)

    return json.loads(data_str)


def get_sell_data(url_page_itemorderhistory, headers):
    response = requests.get(url_page_itemorderhistory, headers = headers)
    obj = json.loads(response.text)

    return(obj['sell_order_graph'])
    
    

def get_buy_data(url_page_itemorderhistory):
    response = requests.get(url_page_itemorderhistory, headers = headers)
    
    response = requests.get(url_page_itemorderhistory, headers = headers)
    obj = json.loads(response.text)

    return(obj['buy_order_graph'])


