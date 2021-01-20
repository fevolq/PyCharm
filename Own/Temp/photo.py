#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:
# Filename:

import requests
import re
from bs4 import BeautifulSoup

def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    return response

def get_title(html):
    # re_pattren = re.compile(r'target="_blank" title="{.*?}" href')
    # goods_url = re_pattren.findall(html)
    soup = BeautifulSoup(html, 'html.parser')
    goods_url = soup.select('#J_goodsList ul')
    print(goods_url, '\n\n\n')

def save_html(html):
    with open(r'C:\Users\15394\Desktop\html.txt','wb') as f:
        f.write(html.encode('utf-8'))
    print('\nDone')

url = 'https://list.jd.com/list.html?cat=737,752,757'
html = get_response(url).text
# save_html(html)
get_title(html)