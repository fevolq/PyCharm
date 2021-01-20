#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:

import requests
import os

def get_response(url):
    response = requests.get(url)
    return response

def save(response):
    with open('C:\\Users\\15394\\Desktop\\1.mp4','wb') as f:
        f.write(response.content)
    print('\nDone')

def run(url):
    response = get_response(url)
    save(response)

if __name__ == '__main__':
    url = 'https://rbv01.ku6.com/wifi/o_1dmdc6nu97guvac1ag4m6v7dd17kvs'
    run(url)

