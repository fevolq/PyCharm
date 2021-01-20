#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:用于临时爬取图片的，随用随改

import requests
from bs4 import BeautifulSoup
import time,random,os

def get_response(url):
    headers = {
        # 'Referer': url1,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    response = requests.get(url,headers=headers)
    return response

def get_path(path):         #路径是否存在
    if os._exists(path):
        pass


def save(response,path,n):
    with open(path + '\\'+'{}.jpg'.format(n),'wb') as f:
        f.write(response.content)
    print('{}已保存'.format(n))

def get_src(html):
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.select('.picmainer #p')[0]
    center = div.select('center')[0]
    img = center.select('img')[0]
    src = img['lazysrc']
    return src

# def main(url,path):
#     urls = [url,]
#     _url = url[0:-7]
#     for i in range(2,101):
#         url = _url + '_' + str(i) + '.html#p'
#         urls.append(url)
#     l = len(urls)
#     print('一共有{}张图片'.format(l))
#     n = 1           #从第一张开始
#     for i in range(n,l+1):
#         start_url = urls[i-1]
#         html = get_response(start_url).text
#         src = get_src(html)
#         response = get_response(src)
#         save(response,path,i)
#         t = random.random() + 1
#         time.sleep(t)

def main(start_url,path):
    response = get_response(start_url)
    save(response,path,1)

if __name__ == '__main__':
    path = r'C:\Users\15394\Pictures\爬虫\套图'
    start_url = 'http://p.maicaoren.net/soutu/pic/323/8.jpg'
    main(start_url,path)