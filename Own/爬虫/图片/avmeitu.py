#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:https://www.avmeitu.net

import requests
import re,os,time
from bs4 import BeautifulSoup

def get_response(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    response = requests.get(url,headers=headers)
    return response

#得到title名和一共多少页
def get_title_page(html):
    title_pattern = re.compile(r'<h1 class="albumTitle">(.*?)</h1>')
    page_pattern = re.compile(r'onclick="msxfApp\(\)">(.*?)<')
    # page_pattern = re.compile(r'<a href="javascript:;" onclick="msxfApp()">(.*?)</a>')
    title = re.findall(title_pattern,html)
    try:
        title = title[0]
    except:
        title = 0
        print('title查找错误')
    page = re.findall(page_pattern,html)
    # page1 = re.search(page_pattern,html)
    # a = page1.group()
    try:
        page = page[1]
    except:
        page = 0
        print('page查找错误')
    return title,page

#找出当前页面的图片的url
def get_photourl(html):
    soup = BeautifulSoup(html,'html.parser')
    img = soup.select('.albumBody img')
    try:
        src = img[0]['src']
        photo_url = 'https://www.avmeitu.net' + src
    except:
        print('src查找错误')
        photo_url = '0'
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

#保存图片
def save(response,path,i):
    with open(path + '{}.jpg'.format(i),'wb') as f:
        f.write(response.content)

def main(start_url,path):
    html = get_response(start_url).text
    title_page = get_title_page(html)
    title = title_page[0]
    page = title_page[1]
    path = select_path(path,title)
    print('共有{}张'.format(page))
    for i in range(1,int(page)):        #最后一张的地址导向是假的
        url = start_url[:-5] + '-' + str(i) + '.html'
        html = get_response(url).text
        photo_url = get_photourl(html)
        response = get_response(photo_url)
        save(response,path,i)
        print('{}已保存'.format(i))
        time.sleep(1)

if __name__ == '__main__':
    start_url = 'https://www.avmeitu.net/album/view-194.html'
    path = 'C:\\Users\\15394\\Pictures\\爬虫\\avmeitu'
    main(start_url,path)
    print('\nDone')

def urls():
    urls = [
        'https://www.avmeitu.net/album/view-584.html',
        ''
    ]




















