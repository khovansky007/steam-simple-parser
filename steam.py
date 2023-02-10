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
    'Cookie': 'ActListPageSize=10; enableSIH=true;',
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


