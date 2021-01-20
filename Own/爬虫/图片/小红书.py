#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:小红书软件的图片下载（从网页爬取的图片有logo，需要直接从手机app上抓取）

import re,os
import random,time
import requests
from bs4 import BeautifulSoup
from atexit import register

def get_response(url1,url2):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        # 'Referer':url2,
    }
    try:
        response = requests.get(url1, headers=headers)
        # response.encoding = response.apparent_encoding
        return response
    except Exception as e:
        print(e)
        print('网址请求错误')
        return 0

#标题
def get_title(html):
    title_pattern = re.compile(r'data-v-0698d22a\sdata-v-f71fb898>(.*?)</h1>')
    title = re.findall(title_pattern,html)
    # print(title)
    title = title[0]
    return title

#图片数量
def get_number(html):
    soup = BeautifulSoup(html,'html.parser')
    div = soup.select('.small-pic div')
    number = len(div)
    return number

#图片地址
def get_photourls(html,number):
    urls = []
    photo_pattern = re.compile(r'"background-image:url(.*?);"')
    photos = re.findall(photo_pattern,html)
    for i in range(number):
        photo_url = 'https:' + photos[i][1:-1]
        # print(photo_url)
        urls.append(photo_url)
    return urls

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
def save(response,path,n):          #n用于图片命名
    with open(path + '{}.jpg'.format(n),'wb') as f:
        f.write(response.content)

#运行步骤
def run(start_url,path):
    print('开始时间：{}'.format(time.ctime()))
    html = get_response(start_url,start_url).text
    title = get_title(html)             #标题
    number = get_number(html)           #一共有多少张图片
    path = select_path(path,title)      #保存路径
    urls = get_photourls(html,number)   #所有的图片的url
    n = 0
    print('开始下载：{}'.format(title))
    print('共{}张'.format(number))
    for url in urls[n:]:
        n += 1
        response = get_response(url,start_url)
        save(response,path,n)           #保存图片
        print('{}已保存'.format(n))
        t = random.choice([0.2,0.5,0.8,1])      #随机延迟
        time.sleep(t)

@register
def _atexit():
    print('结束时间：{}'.format(time.ctime()))
    print('\nDone')

if __name__ == '__main__':
    path = 'C:\\Users\\15394\\Pictures\\爬虫\\小红书'
    start_url = """
    https://www.xiaohongshu.com/discovery/item/5db6394a000000000100b75c?xhsshare=CopyLink&appuid=5afa1b5e11be1060fb8eaf67&apptime=1572339408
    """
    run(start_url,path)

