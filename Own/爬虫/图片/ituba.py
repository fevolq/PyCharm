#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:

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
    c = soup.select('.wrap')
    title = c[2].select('h1')[0].get_text()
    ul = soup.select('.pages ul')[0]
    pages = ul.select('a')[-3].get_text()
    print('一共有{}页'.format(pages))
    return title,pages

#找出当前页面的图片的url
def get_photourl(html):
    photo_urls = []
    soup = BeautifulSoup(html,'html.parser')
    img = soup.select('#ArticlePicBox1 img')
    photo_url = img[0]['src']
    photo_url = 'https:' + photo_url
    photo_urls.append(photo_url)
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
    title = title_page[0]
    pages = title_page[1]
    path = select_path(path,title)
    n = 1
    for i in range(1,int(pages)+1):
        if i == 1:
            url = start_url
        else:
            url = start_url[:-5] + '_' + str(i) + '.html'
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
        'https://www.ituba.cc/siwa/67701.html',
        'https://www.ituba.cc/siwa/67059.html',
        'https://www.ituba.cc/siwa/67708.html',
        'https://www.ituba.cc/siwa/67892.html',
        'https://www.ituba.cc/siwa/67872.html',
        'https://www.ituba.cc/siwa/66742.html',
        'https://www.ituba.cc/siwa/66734.html',
        'https://www.ituba.cc/siwa/66602.html',
        'https://www.ituba.cc/siwa/66713.html',
        'https://www.ituba.cc/siwa/66721.html',
        'https://www.ituba.cc/siwa/66773.html',
        'https://www.ituba.cc/siwa/66713.html',
        'https://www.ituba.cc/siwa/66644.html',
        'https://www.ituba.cc/siwa/66485.html',
        'https://www.ituba.cc/siwa/66539.html',
        'https://www.ituba.cc/belle/67887.html',
        'https://www.ituba.cc/belle/67896.html',
        'https://www.ituba.cc/belle/67867.html',
        'https://www.ituba.cc/belle/67839.html',
        'https://www.ituba.cc/sexy/67894.html',
        'https://www.ituba.cc/sexy/67860.html',
        'https://www.ituba.cc/sexy/67900.html',
        'https://www.ituba.cc/sexy/67899.html',
        'https://www.ituba.cc/sexy/67820.html',
        'https://www.ituba.cc/sexy/67810.html',
        'https://www.ituba.cc/model/67898.html',
        'https://www.ituba.cc/model/67902.html',
        'https://www.ituba.cc/xiurenmote/67905.html',
        'https://www.ituba.cc/feizhuliu/64140.html',
    ]
    start_url = start_urls[0]
    path = 'C:\\Users\\15394\\Pictures\\爬虫\\ituba'
    main(start_url, path)
    # for i in start_urls:
    #     start_url = i
    #     path = 'C:\\Users\\15394\\Pictures\\爬虫\\ituba'
    #     main(start_url,path)