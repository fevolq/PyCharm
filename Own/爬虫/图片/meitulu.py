#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:https://www.meitulu.com

import requests
import re,os,time,random
from bs4 import BeautifulSoup

#url为待爬取页面的网址，url1为图片对应的显示网址，而不是图片本身的网址
def get_response(url,url1):
    headers = {
        'Referer':url1,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    return response

#得到title名和一共多少页
def get_title_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('.weizhi h1')[0].get_text()
    pages = soup.select('#pages a')[-2].get_text()
    return title,pages

#找出当前页面的图片的url
def get_photourl(html):
    photo_urls = []
    soup = BeautifulSoup(html,'html.parser')
    imgs = soup.select('.content center')
    img = imgs[0].select('img')
    for s in img:
        src = s['src']
        photo_urls.append(src)
    return photo_urls

#选择保存地址(以title作为文件夹名)
def select_path(path,title):
    path = path + '\\' + title
    if os.path.exists(path):
        path = path + '\\'
    else:
        os.makedirs(path)
        path = path + '\\'
    return path

#保存图片
def save(response,path,n):
    with open(path + '{}.jpg'.format(n),'wb') as f:
        f.write(response.content)

def main(start_url,path):
    html = get_response(start_url,start_url).text
    title_page = get_title_page(html)
    title = title_page[0]       #转码的问题
    pages = title_page[1]
    path = select_path(path,title)
    n = 1
    for i in range(1,int(pages)+1):
        if i == 1:
            url = start_url
        else:
            url = start_url[:-6] + '_' + str(i) + '.html'
        html = get_response(url,url).text
        photo_urls = get_photourl(html)
        for photo_url in photo_urls:
            response = get_response(photo_url,url)
            save(response,path,n)
            print('{}已保存'.format(n))
            for t in range(random.randint(1,3)):
                time.sleep(t)
            n += 1

if __name__ == '__main__':
    start_urls = [
        'https://www.meitulu.com/item/16556.html',
        'https://www.meitulu.com/item/18831.html',
    ]
    start_url = start_urls[1]
    path = 'C:\\Users\\15394\\Pictures\\爬虫\\meitulu'
    main(start_url,path)