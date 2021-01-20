#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2020.11.09
# Filename:http://www.xiaoqiangxs.org/

#手机端网址：http://wap.xiaoqiangxs.org/

import requests
from bs4 import BeautifulSoup
import os,time

def get_response(url):
    # headers = {'user-agent':'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36'}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    return response

def get_title_urls(html):
    soup = BeautifulSoup(html,'html.parser')
    Title = soup.select('#maininfo #info')[0].select('h1')[0].get_text()    #标题
    dd = soup.select('.box_con #list')[0].select('dd')
    urls = []       #章节url
    titles = []     #章节名
    for d in dd:
        url = 'http://www.xiaoqiangxs.org' + d.select('a')[0]['href']
        urls.append(url)
        title = d.select('a')[0].get_text()
        titles.append(title)
    return Title,urls,titles

def get_text(html):
    soup = BeautifulSoup(html,'html.parser')
    txt = soup.select('.box_con #content')[0].get_text()
    # print(txt)
    return txt

def save(path,Title,txt,title=None):
    if os.path.exists(path):
        path = path + '\\'
    else:
        os.makedirs(path)
        path = path + '\\'
    with open(path + '{}.txt'.format(Title),'ab') as f:
        if title:
            f.write(title.encode('utf-8'))
            f.write('\r\n\r\n'.encode('utf-8'))
        f.write(txt.encode('utf-8'))
        f.write('\r\n\r\n\r\n'.encode('utf-8'))

def main(path,start_url):
    html = get_response(start_url).text
    print(html)
    tu = get_title_urls(html)
    Title = tu[0]           #文件名
    urls = tu[1]            #章节url
    titles = tu[2]          #章节名
    # new_titles = [titles[1],titles[3],titles[5],titles[7],titles[9]] + titles[10:20] + titles[21:24] + titles[26:-3] + titles[-2:]
    # # print(new_titles)
    # new_urls = [urls[1],urls[3],urls[5],urls[7],urls[9]] + urls[10:20] + urls[21:24] + urls[26:-3] + urls[-2:]
    # l = len(new_urls)
    l = len(urls)
    print('{} 共有{}章'.format(Title,l))
    for i in range(l):
        txt_html = get_response(urls[i]).text
        txt = get_text(txt_html)
        # save(path,Title,txt,titles[i])
        save(path, Title, txt)
        print('{}-{}.{} 已下载'.format(l,i+1,titles[i]))
    print('Done')

#单章title
def get_title_one(html):
    soup = BeautifulSoup(html,'html.parser')
    div = soup.select('.box_con .bookname')[0]
    title = div.select('h1')[0].get_text()
    # print(title)
    return title

#单章
def main_one(path,start_url):
    html = get_response(start_url).text
    title = get_title_one(html)
    txt = get_text(html)
    save(path,title,txt)
    print('{} 已下载'.format(title))

if __name__ == '__main__':
    path = r'C:\Users\15394\Documents\Spider'
    start_url = 'http://www.xiaoqiangxs.org/2_12416/'
    main(path, start_url)

    # l = [13387,12786]
    # for i in l:
    #     number = str(i)
    #     start_url = 'http://www.xiaoqiangxs.org/2_{}/'.format(number)
    #     main(path,start_url)
    #     time.sleep(3)
    pass

    #单章页面
    # start_url = 'http://www.xiaoqiangxs.org/2_2338/159764.html'
    # main_one(path,start_url)
