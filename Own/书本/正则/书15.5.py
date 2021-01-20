#!-*-coding:utf-8 -*-
#!@Author：fuq666@qq.com

import re

data2 = 'arrw.aer asd zxc wqevs:af'
# a2_pattern = re.compile(r'\.(\w+) (\w+)')
# a2 = re.search(a1_pattern,data)
# print(a2.groups())
data3 = 'faef S.abc qwe faef'
# a3_pattern = re.compile(r'\w\.\w+ \w+')
# a2 = re.search(a3_pattern,data1)
# print(a3.group())
data5 = '341 qr qer fq rg'
# a5_pattern = re.compile(r'\d+( \w+)+')
# a5 = re.search(a5_pattern,data5)
# print(a5.group())
data6 = 'www.daeg.com www.freg.net'
# a6_pattern = re.compile(r'(w{3})\.(\w+).(com|edu|net)')
# a6 = re.search(a6_pattern,data6)
# print(a6.group())
data11 = 'deq afg21@fex.comaf dre'
# a11_pattern = re.compile(r'((\w+)@(\w+)\.(com))')
# a11 = re.search(a11_pattern,data11)
# print(a11.group(1))
data12 = 'https://www.baidu.com/'
# a12_pattern = re.compile(r'(http)s?(://)(.*?)(/)')
# a12 = re.search(a12_pattern,data12)
# print(a12.group())
data13 = type(0)
# a13_pattern = re.compile(r"'(.*?)'")
# a13 = re.search(a13_pattern,str(data13))
# print(a13.group())
data14 = '2019-11-09'
# a14_pattern = re.compile(r'1[0-2]')
# print(re.findall(a14_pattern,data14)[0])
# a14 = re.search(a14_pattern,data14)
# print(a14.group())
data15_1 = '3627-824475-12442'
a15_pattern_1 = re.compile(r'\d{4}-\d{6}-[0-9]{5}')
a15_1 = re.search(a15_pattern_1,data15_1)
print(a15_1.group())
data15_2 = '1957-3195-2357-9123'
a15_pattern_2 = re.compile(r'[0-9]{4}-\d{4}-\d{4}-\d{4}')
a15_2 = re.search(a15_pattern_2,data15_2)
print(a15_2.group())