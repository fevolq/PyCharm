#!-*-coding:utf-8 -*-
#!@Author：fuq666@qq.com

import re

# path ='C:\\Users\\15394\\Desktop\\正则.txt'
path = '正则.txt'
with open(path,'r') as f:
    txt = f.read()

# a1_match = re.compile(r'bat|bit|but|hat|hit|hut')
# print(a1_match.findall(txt))            #['bit']
# a2_match = re.compile(r'f.o')
# print(a2_match.findall(txt))            #['fbo', 'foo', 'f.o', 'fko', 'fQo', 'fuo', 'fEo', 'fYo', 'f3o', 'f2o']
# a3_match = re.compile(r'.ab')
# print(a3_match.findall(txt))            #['Wab', 'aab', 'iab', 'Pab', ',ab', 'lab', 'wab', 'Bab', 'Wab', '1ab', '6ab', 'Wab', 'uab', 'bab']
# a4_match = re.compile(r'.\.d')
# print(a4_match.findall(txt))            #['l.d', 'h.d', 'i.d', 'Z.d', 'a.d', '..d', 'I.d', 'k.d',···]
# a5_match = re.compile(r'.*3$')
# print(a5_match.findall(txt))            #['ZX2k3']
# a6_match = re.compile(r'\Bam')
# print(a6_match.findall(txt))
# a7_match = re.compile(r'b[aeiou]t')
# print(a7_match.findall(txt))            #['bit', 'bot']
# a8_match = re.compile(r'[abc][123][dp][45678]')
# print(a8_match.findall(txt))              #['c1d4']
# a9_match = re.compile(r'[^d-z].[0-3]')
# print(a9_match.findall(txt))                #['y92', 'y50', 'zV3', 'zD0', 'yD0',···]
# a10_match = re.compile(r'[0-9]{3}')         #['927', '865', '999', '627', '310', '885',···]
# print(a10_match.findall(txt))

# b1_pattern = re.compile(r'\d+\.\d+')          #['87.2', '6.4', '2.748', '3.0', '7.1', '6.2',
# print(re.findall(b1_pattern,txt))           #返回的是一个列表 或None
# print(re.finditer(b1_pattern,txt))          #返回的是一个迭代器，对每个匹配，该迭代器返回一个匹配对象
# print(re.match(b1_pattern,txt))
# print(re.search(b1_pattern,txt))            #返回一个匹配对象，否则返回None

c = '123a456a789'
# c1_pattern = re.compile(r'a')
# print(re.split(c1_pattern,c))           #按正则表达式内的字符进行分隔，返回一个列表。['123', '456', '789']
# print(re.sub(c1_pattern,'b',c))         #替换
# c2_pattern = re.compile(r'(\d+)\w?(\d+)\w?(\d+)')
# c2 = re.search(c2_pattern,c)
# print(c2.group(),c2.group(2),c2.groups())   #123a456a789 456 ('123', '456', '789')
c ='abc def 123'
# c3_pattern = re.compile(r'abc|123')
# c3 = re.search(c3_pattern,c)
# print(c3.group())       #全文查找首个匹配的对象
# c4_pattern = re.compile(r'def')
# c4 = re.match(c4_pattern,c)     #从起始处开始匹配正则表达式，没有则返回None
# if c4 is not None:
#     print(c4.group())i
