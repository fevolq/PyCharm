#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
# Update time:2020.12.24
#!Filename:https://www.tujigu.com/

import requests
import re,os,time,random
from bs4 import BeautifulSoup
from threading import Thread
from atexit import register

#url为待爬取页面的网址，url1为图片对应的显示网址，而不是图片本身的网址
def get_response(url,url1='https://www.tujigu.com'):
    headers = {
        'Referer': url1,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    try:
        response = requests.get(url,headers=headers)
        response.encoding = response.apparent_encoding
        return response
    except Exception as e:
        print(e)
        print('网址请求错误，可能需要更换cookie或稍后再试')
        return 0

#专用于得到图片信息的response
def get_photo_response(photo_url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
    response = requests.get(photo_url,headers=headers)
    return response

#得到title名
def get_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    d = soup.select('head title')[0].get_text()
    # print(d)
    # title = d[0].select('h1')[0].get_text()
    # print(title)
    # return title
    return d

#得到总页数
def get_pages(html,start_url):
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.select('#pages a')[-2]
    number = a.get_text()
    urls = [start_url]
    try:
        for i in range(2,int(number)+1):
            page_url = start_url + '{}.html'.format(i)
            urls.append(page_url)
    except:     #只有一页
        pass
    return urls

#找出当前页面的图片的url
def get_photourl(html):
    photo_urls = []
    soup = BeautifulSoup(html,'html.parser')
    imgs = soup.select('.content img')
    for img in imgs:
        src = img['src']
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

#得到图片的编号
def get_photo_number(code,photo_url):
    l_1 = len(photo_url)
    l_2 = len(str(code))
    number = photo_url[27+l_2:l_1-4]
    return number

#保存一张图片的流程（用于多线程）
def save_one_photo(photo_url,path,number):
    response = get_photo_response(photo_url)
    with open(path + '{}.jpg'.format(number),'wb') as f:
        f.write(response.content)

#判断是否该网址已经下载过
def wheather_exist(path,code):
    l = os.listdir(path)
    codes = []
    for i in l:
        name_pattern = re.compile(r'(\d+)\s')
        file_code = re.findall(name_pattern, i)
        if len(file_code) == 0:
            file_code = '0'
        else:
            file_code = file_code[0]  # 字符串格式
        codes.append(file_code)
    if str(code) in codes:
        print('\n警告：该网址（{}）图片可能已下载，请在文件夹内确认后再重新执行\n'.format(code))
        return False
    else:
        return True

#单页的运行流程（找出图片并保存）
def one_page(url,path,code):
    html = get_response(url).text
    photo_urls = get_photourl(html)
    threads = []
    for i in range(1, len(photo_urls) + 1):
        photo_url = photo_urls[i - 1]
        number = get_photo_number(code,photo_url)
        t = Thread(target=save_one_photo, args=(photo_url, path,number))  # 对每页内的多张图片使用多线程
        threads.append(t)
    for i in range(len(threads)):
        threads[i].start()  # 开始线程
    for i in range(len(threads)):
        threads[i].join()

#主程序
def _main(code,path):
    wheather = wheather_exist(path,code)
    if wheather:    #该网址是否已下载过(已存在)
        pass
    else:
        pass
        return 0
    start_url = 'https://www.tujigu.com/a/{}/'.format(code)
    print('准备下载：{}'.format(start_url))
    html = get_response(start_url).text
    title = str(code) + ' ' +  get_title(html)
    urls = get_pages(html,start_url)    #每页的url
    path = select_path(path,title)
    threads = []
    for i in range(1, len(urls) + 1):
        url = urls[i - 1]
        t = Thread(target=one_page, args=(url, path,code))  # 对每个title的多页使用多线程
        threads.append(t)
    for i in range(len(threads)):
        threads[i].start()  # 开始线程
    for i in range(len(threads)):
        threads[i].join()

@register
def _atexit():      #注册一个退出函数，在程序退出时执行。（注意：需要提前导入该模块）
    print('\nDone')

if __name__ == '__main__':
    path = 'C:\\Users\\15394\\Pictures\\爬虫\\tujigu'
    l = []
    for code in l:
        # s = time.time()
        _main(code, path)
        # e = time.time()
        # print('耗时{}'.format(e-s))
        print('{}已保存'.format(code))
        time.sleep(random.choice([0.2,0.5,0.7,1]))
