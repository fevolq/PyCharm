import requests
from bs4 import BeautifulSoup
import os,re,time
from threading import Thread
import threading

def get_response(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    return response

#影视分类
def get_class(html):
    soup = BeautifulSoup(html,'html.parser')
    lis = soup.select('.sddm #sddm')[0].select('li')
    # print(li)
    url_class = {}
    for li in lis[1:]:
        a_s = li.select('a')
        for a in a_s:
            url = 'http://www.jisudhw.com' + a['href']
            name = a.get_text()
            # print(url,name)
            urls = {name:url}
            url_class.update(urls)
    # print(urls_class)
    return url_class

#共有多少页
def get_pages(html):
    soup = BeautifulSoup(html,'html.parser')
    pages = soup.select('.xing_vb .pages')[0].get_text()
    # print(pages)
    p = re.compile(r'(\d+)页')
    page = p.findall(pages)
    page = int(page[0])
    return page

#每页的所有视频详情地址
def get_movie_url(html):
    soup = BeautifulSoup(html,'html.parser')
    span = soup.select('.xing_vb .xing_vb4')
    urls = []
    for s in span:
        href = 'http://www.jisudhw.com' + s.select('a')[0]['href']
        # print(a)
        urls.append(href)
    return urls

#每个视频的信息
def get_message(html):
    soup = BeautifulSoup(html,'html.parser')
    div = soup.select('.warp .vodh')[0]
    movie_name = div.select('h2')[0].get_text()
    # print(movie_name)
    r = re.compile(r'/>(.*?)\.m3u8<')
    txt = r.findall(html)
    txts = []
    for t in txt:
        t = t + '.m3u8'
        t = movie_name + t.replace('$', '，')
        # print(t)
        txts.append(t)
    return txts

#每个线程的操作
def everyone(url,path,name,lock):
    lock.acquire()
    html = get_response(url).text
    txts = get_message(html)
    for txt in txts:
        save(path,name,txt)
    lock.release()

def save(path,name,txt):
    # txt = txt.encode('gbk')
    with open(path + '\{}.txt'.format(name),'ab') as f:
        f.write(txt.encode("gbk","ignore"))
    with open(path + '\{}.txt'.format(name),'a') as f:
        f.write('\r\n')

def main(url,path,name):
    html = get_response(url).text
    url_class = get_class(html)
    # print(url_class)
    if name not in url_class:
        print('请确认后重新输入')
        name = input('请输入选择的类型（如：动作片）：')
        main(url, path, name)
        return
    else:
        url = url_class[name]
        # print(url)
        html = get_response(url).text
        pages = get_pages(html)     #共有多少页
        print('共有{}页'.format(pages))
        for page in range(1,pages+1):       #每页
            page_url = url[:-5] + '-pg-{}.html'.format(page)
            # print(page_url)
            page_html = get_response(page_url).text
            movie_urls = get_movie_url(page_html)       #所有行的链接

            threads = []                    #对每页进行多线程
            lock = threading.Lock()
            for i in range(1,len(movie_urls)+1):
                movie_url = movie_urls[i-1]
                t = Thread(target=everyone,args=(movie_url,path,name,lock))
                threads.append(t)
            for i in range(len(movie_urls)):
                threads[i].start()
            for i in range(len(movie_urls)):
                threads[i].join()
            # break   #32s
        return

if __name__ == '__main__':
    url = 'http://www.jisudhw.com/'
    path = r'C:\Users\RLY\Desktop\spider'
    name = input('请输入选择的类型（如：动作片）：')
    # name = '日本剧'

    start_time = time.time()
    print('开始时间：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)))

    main(url,path,name)

    end_time = time.time()
    print('结束时间：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)))
    use_time = end_time - start_time
    struct_time = time.gmtime(use_time)
    print('使用了{}年{}月{}日{}小时{}分钟{}秒'.format(
        struct_time.tm_year - 1970,
        struct_time.tm_mon - 1,
        struct_time.tm_mday - 1,
        struct_time.tm_hour,
        struct_time.tm_min,
        struct_time.tm_sec
    ))