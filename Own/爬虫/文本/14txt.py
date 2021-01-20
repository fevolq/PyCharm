#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:https://m.14txt.net
#68   140   234

import requests
import re,os,time,random
from bs4 import BeautifulSoup
from atexit import register

def get_response(url,refer_url):
    # requests.packages.urllib3.disable_warnings()
    headers = {
        # 'Referer': refer_url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    }
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    return response

#得到所有章节的url
def get_chapter(html):
    urls = []
    titles = []
    soup = BeautifulSoup(html, 'html.parser')
    Title = soup.select('#top span')[0].get_text()
    # Title = soup.select('#main #info')[0].get_text()
    print(Title)
    p = soup.select('#chapterlist p')
    l = len(p)
    for i in range(1,l-1):
        a = p[i].select('a')[0]
        href = a['href']
        title = a.get_text()
        url = 'https://www.114txt.cc' + href
        titles.append(title)
        urls.append(url)
    return Title,titles,urls           #文件名，章节名合集，章节url合集

#标题
def get_title(html):
    soup = BeautifulSoup(html,'html.parser')
    div = soup.select('.box_con .bookname')[0]
    title = div.select('h1')[0].get_text()
    # print(title)
    # select_match = re.compile(r'\S+')
    # title = re.findall(select_match,title)[0]
    return title

#文本内容
def get_txt(html,l):
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.select('.box_con #content')[0].get_text()
    #对内容进行处理加工
    txt_match = re.compile(r'\s+')
    txt = re.sub(txt_match,'123',div)
    page_match = re.compile(r'/(\d+)页')
    pages = re.findall(page_match,txt[0:50+l])
    try:
        pages = pages[0]
        print('有%s页' % pages)
    except Exception as e:
        pages = 1
        print(e)
        print('只有1页？')
    # pages = txt[20+l:21+l]
    # txt = txt[120+l:-(39+l)]
    txt = txt[49 + l:-50]                      #根据文章内容修改数字
    # print(txt)
    return txt,pages

#保存
def save(txt,Title,path,title=0):       #Title是文件名，title是章节名
    if os.path.exists(path):
        path = path + '\\'
    else:
        os.makedirs(path)
        path = path + '\\'
    with open(path+'{}.txt'.format(Title),'ab') as f:
        if title:
            f.write(title.encode('gb18030'))
        else:
            pass
        txt = txt.replace('\n', '\r\n')
        txt = txt.replace('123','\r\n\r\n       ')
        f.write(txt.encode('gb18030'))
        # f.write('\r\n\r\n'.encode('gb18030'))     #章节后换行
        # f.write('\r\n'.encode('gb18030'))

#查看网页的html
def save_html(html):
    with open('E:\\pycharm_project\\爬虫\\文本\\html.txt','wb') as f:
        f.write(html.encode())

#运行顺序
#单章
def main_single(start_url,path,Title=0):
    html = get_response(start_url,start_url).text
    # print(html)
    # save_html(html)
    title = get_title(html)
    # print(title)
    l = len(title)  #标题的长度
    content = get_txt(html,l)
    txt = content[0]
    pages = content[1]
    if Title:
        save(txt, Title, path)      #正文内包含章节名时
        # save(txt,Title,path,title)      #有多章的时候（使用main_many函数时）
    else:
        Title = title
        save(txt, Title, path)          #只有一章的时候使用
    # print(start_url,'\n',title,'\n','第1页已保存')
    try:
        pages = int(pages)
        for i in range(2,pages+1):
            url = start_url[:-5] + '_' + str(i) + '.html'
            html = get_response(url,start_url).text
            txt = get_txt(html,l)[0]
            save(txt, Title, path)
            # print('第{}页已保存'.format(i))
    except Exception as e:
        print('只有1页？？')
        # print(e)

#多章
def main_many(start_url,path):
    start_url = 'https://m.114txt.cc/1/' + start_url[24:]
    # print(start_url)
    html = get_response(start_url,start_url).text
    chapter = get_chapter(html)
    Title = chapter[0]      #总标题，即文件名
    titles = chapter[1]     #章节名
    urls = chapter[2]       #每章的url
    # print(Title,titles,urls)
    l = len(urls)
    print('{}、{}一共{}章'.format(start_url[22:-1],Title,l))
    n = 1               #需要从第n章开始，则改成n
    # for i in range(n, 3):
    for i in range(n,l+1):         #l+1
        print('{}.{} 开始下载'.format(i, titles[i-1]))
        url = urls[i-1]
        main_single(url,path,Title=Title)
        print('{}.{} 已下载'.format(i,titles[i-1]))

"""另一种模式"""
#书名
def get_Title(html):
    soup = BeautifulSoup(html,'html.parser')
    h1 = soup.select('#info h1')
    Title = h1[0].get_text()
    return Title

#每章的章节名和url
def get_title_url(html):
    titles = []
    urls = []
    soup = BeautifulSoup(html,'html.parser')
    dl = soup.select('#list dl')[0]
    # print(dl)
    dds = dl.select('dd')
    l = len(dds)
    if l >= 24:
        for dd in dds[12:]:
            a = dd.select('a')[0]
            url = 'https://www.1114txt.com' + a['href']
            title = a.get_text()
            titles.append(title)
            urls.append(url)
    else:
        for dd in dds[l//2:]:
            a = dd.select('a')[0]
            url = 'https://www.1114txt.com' + a['href']
            title = a.get_text()
            titles.append(title)
            urls.append(url)
    # print(titles,urls)
    return titles,urls

def get_txt_other(html):
    txt_match = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;')
    html = re.sub(txt_match, '123', html)
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.select('.box_con #content')[0]
    txt = div.get_text()
    # txt = '       ' + txt[72:-53]
    txt = txt[69:-53]
    # print(txt)
    return txt

def main_other(n,start_url,path):
    html = get_response(start_url,start_url).text
    Title = get_Title(html)
    title_url = get_title_url(html)
    titles = title_url[0]
    urls = title_url[1]
    l = len(urls)
    print('{} 一共{}章'.format(Title,l))
    for i in range(n,l+1):
    # for i in range(1,3):
        t = random.random() + 1
        time.sleep(t)
        if __name__ == '__main__':
            title = titles[i - 1]
            url = urls[i - 1]
            html = get_response(url,start_url).text
            txt = get_txt_other(html)
            save(txt, Title, path, title)  # 正文中需要打印title时
            # save(txt, Title, path)
            print('{}-{}.{}······已保存'.format(l,i, title))
        else:
            try:
                title = titles[i-1]
                url = urls[i-1]
                # print(1)
                html = get_response(url,start_url).text
                txt = get_txt_other(html)
                save(txt,Title,path,title)      #正文中需要打印title时
                # save(txt, Title, path)
                print('{}-{}.{}······已保存'.format(l,i,title))
            except:
                return i
    return False

@register
def _atexit():      #程序退出时运行的函数
    print('\n程序结束')

if __name__ == '__main__':
    n = 1  # 需要从第几开始就改成几
    path = 'C:\\Users\\15394\\Documents\\Spider'
    # url = 'https://m.14txt.net/16/16089/1268585.html'
    # main_single(url,path)          #使用的是第一页内容的网址，eg：https://m.14txt.net/1/1133/276013.html

    # url = 'https://www.114txt.cc/5/5548/'
    # main_many(url,path)              #使用的是书的详情页网址，eg：https://m.14txt.net/book/4146

    l = [,]   #
    for i in l:
        url = 'https://www.1114txt.com/5/{}/'.format(i)
        main_other(n,url,path)
        print('{}已完成'.format(i))
        time.sleep(3)