#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:https://1.yasee8.com

import requests
import re,os
from bs4 import BeautifulSoup
from atexit import register

def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    return response

def get_title(html):
    soup = BeautifulSoup(html,'html.parser')
    title = soup.select('.article-header .article-title')[0].get_text()
    return title

def get_txt(html):
    # txt_match = re.compile(r'<div class="ad-box" id="cdaas-rand"></div>(.*?)</div>')
    # txt = re.findall(txt_match,html)
    # print(txt)
    # try:
    #     txt = txt[0]
    #     return txt
    # except:
    #     print('txt内容查找错误')
    #     return None
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.select('.novel-list-box div')[2]
    txt = div.get_text()
    return txt

def save(txt,title,path):
    if os.path.exists(path):
        path = path + '\\'
    else:
        os.makedirs(path)
        path = path + '\\'
    with open(path+'{}.txt'.format(title),'wb') as f:
        f.write(title.encode("gbk"))
        txt = txt.replace('\n','\r\n')
        f.write(txt.encode('gb18030'))
    print('{}已保存'.format(title))

def save_html(html):
    with open('E:\\pycharm_project\\爬虫\\文本\\html.txt','wb') as f:
        f.write(html.encode('gb18030'))

def _main(start_url,path):
    html = get_response(start_url).text
    # save_html(html)
    title = get_title(html)
    txt = get_txt(html)
    save(txt,title,path)

@register
def _atexit():      #程序退出时运行的函数
    print('\nDone')

if __name__ == '__main__':
    path = 'C:\\Users\\15394\\Documents\\Spider'
    # url = 'https://1.yasee8.com/novel-56251'
    # url = 'https://1.yasee8.com/novel-56250'
    url = 'https://1.yasee8.com/novel-56245'
    _main(url,path)