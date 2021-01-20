#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2020.11.03
# Filename: https://www.gqxz.com/

import requests
import os,time
from bs4 import BeautifulSoup

def get_response(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    response = requests.get(url,headers=headers)
    return response

def get_urls_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('.hd h1')[0].get_text()
    if '(' in title:
        n = title.index('(')
        title = title[0:n]
        # print(title)
    else:
        pass
    a = soup.select('#main #page')[0].select('a')
    # page = soup.select('.col #page')
    # a = page[0].select('a')
    urls = []
    for i in range(1,len(a)-1):
        url = 'https://www.gqxz.com' + a[i]['href']
        urls.append(url)
    return title,urls

#得到图片的地址
def get_picture(html):
    soup = BeautifulSoup(html, 'html.parser')
    img = soup.select('#endtext img')
    photo_url = img[0]['src']
    return photo_url

#选择保存地址(以title作为文件夹名)
def select_path(path,title):
    path = path + '\\' + title
    if os.path.exists(path):
        path = path + '\\'
    else:
        os.makedirs(path)
        path = path + '\\'
    return path

def save(response,path,i):
    with open(path + '{}.jpg'.format(i),'wb') as f:
        f.write(response.content)

def main(start_url,path):
    html = get_response(start_url).text
    ut = get_urls_title(html)
    title = ut[0]
    urls = ut[1]
    # print(title)
    path = select_path(path,title)
    print('{}共有{}张'.format(title,len(urls)))
    for i in range(len(urls)):
        html = get_response(urls[i]).text
        photo_url = get_picture(html)
        response = get_response(photo_url)
        save(response,path,i+1)
        print(i+1)
        time.sleep(0.5)
    print('Done')

if __name__ == '__main__':
    path = r'C:\Users\15394\Pictures\爬虫\gqxz'
    # start_url = 'https://www.gqxz.com/beauty/2/8426_1.html'
    # main(start_url,path)
    start_urls = ['https://www.gqxz.com/wallpaper/2/2344_1.html','https://www.gqxz.com/wallpaper/2/2599_1.html',
                  'https://www.gqxz.com/wallpaper/2/5223_1.html','https://www.gqxz.com/wallpaper/2/5356_1.html',
                  'https://www.gqxz.com/wallpaper/5/8573_1.html','https://www.gqxz.com/wallpaper/2/8191_1.html',
                  'https://www.gqxz.com/wallpaper/2/8336_1.html','https://www.gqxz.com/wallpaper/2/680_1.html',
                  'https://www.gqxz.com/beauty/2/8541_1.html','https://www.gqxz.com/beauty/3/6250_1.html',
                  'https://www.gqxz.com/beauty/6/6414_1.html']
    for start_url in start_urls:
        main(start_url,path)