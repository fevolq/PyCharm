#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:https://www.umei.fun/
#网址需开ip代理才能访问???
#部分网页需要登陆账号才可查看（此处使用了“临时”的请求cookie来登陆）

import requests
import re,os,time,random
from bs4 import BeautifulSoup
from threading import Thread
from atexit import register

#url为待爬取页面的网址，url1为图片对应的显示网址，而不是图片本身的网址
def get_response(url,url1='https://www.umei.fun/'):
    cookie = {
        '__cfduid': 'd069b9d13ff5c13bdb8375bd4d984f7181604580012',
        # '_ga': 'GA1.2.880489818.1571991338',
        # '_gid': 'GA1.2.308639808.1572249864',
        # 'remember_user_token':'W1s1MDYyNl0sIiQyYSQxMSQ5S2xGQTdBRHB1anRCWVIwSmJIQlR1IiwiMTU3MTk5MTUzNy43Mzk5OTg4Il0%3D--f31962cb5a3b9ef3380d44a4dff74f06678bf74f',
        # '_gat_gtag_UA_118378815_1':'1',
        '_abc_session': 'TFY0WXRaSU1OMGVMdFVvd1JHS0lURDBIcTlkeXhoOFJrbG5ueTEwczVMT053ZG9yRlV3WmZjalE0MEVTa2kxVE1LQWk4Um9jVkFFay9jT1pSWVR6UGJZNWJiVUM0K3kyQTBTcHJFcXNzWmdaV1RCYlBjZHlGWGRnTHNKM015RXpxempYWXBILzBqWkh6RUMwSndGRmFVd09TQ1hNTEZUczRHS3BjUllia09BSVRMSTQ3akVIV1RFaVI1NXpUS1J3ZlJ3aEFKSWVuZXpUbVUvZnpKWEdNRmR4K2VHcHYyWWRteDlBU0ZuYzJ5NWxOa0IyWWQxT0R2NTBFOXZPNmcxRlJrMWd3akdkNWo0QjBWS0NMZ1MyYVBqbTFWa0dFNGdkaURHMklaTnd2OXNyZ1NOcDVWMDVWM29MWUE5aHYvMUdyeTk3OU52WjJabFRoK0xLVmJ0cU8vRHhGWmI2bHZCZktxT1BYekc3OEJRV01MZ3RlcVpVTEpvTzRPY0svTDhKZ2d4MEtSTFloNUNVcUFvMVRmTG9BbXhzdHBsNm43VHpVcFl3SWJsSUtWOGZpZTB0ai9qdjgvZ0IyUmhLaUczOVpBLzJSTVdjRk91bmJyS0wrd0s5TDZaRlI0Qm1uandVdlBseGZDUzlFV2M9LS1QZHcranVnZDhiRERNenBJNDBFVVd3PT0%3D--0c53a24e0d226a75b4d5cf9f332b7c14276e311a',
    }
    headers = {
        'Referer':url1,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    try:
        response = requests.get(url,headers=headers,cookies=cookie)
        # print(response)
        response.encoding = response.apparent_encoding
        return response
    except Exception as e:
        print(e)
        print('网址请求错误，可能需要更换cookie或稍后再试')
        return 0

#专用于得到图片信息的response，若使用上一个函数，则时间大大延长？？？
def get_photo_response(photo_url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
    cookie = {'__cfduid' : 'd069b9d13ff5c13bdb8375bd4d984f7181604580012'}
    response = requests.get(photo_url,headers=headers,cookies=cookie)
    return response

#得到title名
def get_title_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    c = soup.select('.container .row')
    title = c[0].select('h2')[0].get_text()
    return title

#找出当前页面的图片的url
def get_photourl(html):
    photo_urls = []
    soup = BeautifulSoup(html,'html.parser')
    c = soup.select('.container .row')[0]
    imgs = c.select('.card img')
    for img in imgs:
        src = img['src']
        photo_urls.append(src)
    print('一共有{}张图片'.format(len(photo_urls)))
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

#保存一张图片的流程（用于多线程）
def everyone(photo_url,path,n):
    response = get_photo_response(photo_url)
    save(response, path, n)
    print('{}已保存，{}'.format(n,time.ctime()))

#打印html文本，用于检验
def _html(html):
    with open('C:\\Users\\15394\\Pictures\\爬虫\\umei\\umei_html.txt','w+') as f:
        f.write(html)

#判断是否该网址已经下载过
def wheather_exist(path,url):
    l = os.listdir(path)
    names = []
    for i in l:
        name_pattern = re.compile(r'(\d+)\s')
        name = re.findall(name_pattern, i)
        if len(name) == 0:
            name = '0'
        else:
            name = name[0]  #字符串格式
        names.append(name)
    number_pattern = re.compile(r'(\d+)')
    number = re.findall(number_pattern, url)[0]     #找到网址最后用来命名文件夹的数字
    if number in names:
        print('\n警告：该网址（{}）图片可能已下载，请在文件夹内确认后再重新执行\n'.format(url))
        return False
    else:
        return True

#主程序
def _main(start_url,path,w):
    wheather = wheather_exist(path,start_url)
    if wheather:    #该网址是否已下载过
        pass
    else:
        pass
        return 0
    print('准备下载：{}'.format(start_url))
    html = get_response(start_url).text
    # _html(html)
    # print(html)
    title = get_title_page(html)
    if title == '欢迎回来':     #需要登陆的情况
        num_pattern = re.compile(r'.*?(\d+)')
        num = re.findall(num_pattern,start_url)
        title = '{} 未下载'.format(num[0])
        print('{}需登陆'.format(title))
    else:
        num_pattern = re.compile(r'.*?(\d+)')
        num = re.findall(num_pattern, start_url)
        title = num[0] + ' ' + title
    pages = 1
    path = select_path(path,title)
    n = 1      #初始为1，续下载则改成下一个编号。且需把116行的“return 0”注释掉
    for i in range(1,int(pages)+1):
        #只有一页，所以html可重用
        photo_urls = get_photourl(html)
        if w == '1':
        #多线程
            threads = []
            for i in range(n, len(photo_urls) + 1):
                photo_url = photo_urls[i-1]
                t = Thread(target=everyone,args=(photo_url,path,n))     #对每个title内的多张图片使用多线程
                threads.append(t)
                n += 1
            for i in range(len(threads)):
                threads[i].start()              #开始线程
            for i in range(len(threads)):
                threads[i].join()               #可不使用
        elif w == '2':
        #单线程
            for i in range(n,len(photo_urls)+1):
                photo_url = photo_urls[i-1]
                everyone(photo_url,path,n)
                t = random.choice([0.2,0.5,0.7,1])
                time.sleep(t)
                n += 1

@register
def _atexit():      #注册一个退出函数，在程序退出时执行。（注意：需要提前导入该模块）
    print('结束时间：{}'.format(time.ctime()))
    print('\nDone')

if __name__ == '__main__':
    w = '2'     #'1'则使用多线程，'2'则使用单线程
    path = 'C:\\Users\\15394\\Pictures\\爬虫\\umei'
    #自选网址
    # start_url = 'https://www.umei.fun/posts/8239'       #
    # print('开始时间：{}'.format(time.ctime()))
    # _main(start_url, path,w)
    l = [8027,5915,6310,3803,6516,4464,7669,3771,1983,1498,4668,8033,6568,6565,]
    for i in l:
        start_url = 'https://www.umei.fun/posts/' + str(i)
        print('开始时间：{}'.format(time.ctime()))
        _main(start_url, path, w)
        time.sleep(5)

    #从txt文件读取网址
    # with open('umei网址.txt','r') as f:
    #     start_urls = f.readlines()
    # for i in start_urls[22:]:     #7267
    #     start_url = i
    #     print('开始时间：{}'.format(time.ctime()))
    #     _main(start_url,path,w)