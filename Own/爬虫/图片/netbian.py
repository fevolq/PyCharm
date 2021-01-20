#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2020.09.03
# Filename:http://pic.netbian.com/

import requests
import time,os,re
from bs4 import BeautifulSoup

def get_response(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response
    else:
        print('网址请求失败')
        return