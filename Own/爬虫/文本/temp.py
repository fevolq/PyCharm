#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:临时使用

import requests
import time,random,re
from bs4 import BeautifulSoup
from atexit import register

def get_response(start_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
    }
    response = requests.get(start_url, headers=headers)
    response.encoding = response.apparent_encoding
    return response

#得到所有章节名称和对应的url
def get_title_url(html):
    titles = []
    urls = []
    soup = BeautifulSoup(html, 'html.parser')
    dl = soup.select('.inner .chapterlist')[0]
    dd = dl.select('dd')
    for i in dd:
        a = i.select('a')[0]
        url = 'https://www.ggdown.cc' + a['href']
        title = a.get_text()
        # print(url,title)
        titles.append(title)
        urls.append(url)
    return titles,urls

#每章的内容
def get_txt(html):
    txt_match = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;')
    html = re.sub(txt_match, '123', html)
    soup = BeautifulSoup(html, 'html.parser')
    txt = soup.select('#BookText')[0].get_text()
    return txt

#保存
def save(path,title,txt):
    with open(path,'ab') as f:
        # title = title.replace('/', '')
        # f.write(title.encode('gb18030'))
        # f.write('\r\n'.encode('gb18030'))
        txt = txt.replace('/', '')
        txt = txt.replace('123', '\r\n       ')
        f.write(txt.encode('gb18030'))
        f.write('\r\n\r\n\r\n'.encode('gb18030'))

def main(start_url):
    html = get_response(start_url).text
    title_url = get_title_url(html)
    titles = title_url[0]
    urls = title_url[1]
    path = r'C:\Users\15394\Desktop\香烟爱上火柴.txt'
    l = len(titles)
    print('一共有{}章'.format(l))
    n = 1      #i.第x章 已保存，就改成i+1
    for i in range(n-1,l):
        # i = i-1
        title = titles[i]
        if title == titles[i-1] and i != 0:
            continue
        url = urls[i]
        html = get_response(url).text
        txt = get_txt(html)
        save(path,title,txt)
        print('{}.{}  已保存'.format(i+1,title))
        t = random.random()
        time.sleep(t)

@register
def _atexit():      #程序退出时运行的函数
    print('\n运行结束')

if __name__ == '__main__':
    start_url = 'https://www.ggdown.cc/book/5989/'
    main(start_url)