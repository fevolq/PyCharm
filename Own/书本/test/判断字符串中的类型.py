#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:

def what_type(s):
    # print(type(s))
    if isinstance(s,int):
        print('为数字类型（整型）')
        return 1
    elif isinstance(s,str):
        print('为字符串str类型\n')
        return 2
    else:
        print('为其他类型')
        return 0

def what_element(s):        #传入的是一个字符串格式的变量
    '''直接判断字符串内是否为数字或字母或两者的组合'''
    # print(type(s),'\n')
    if s.isdigit():                 #必须全为数字(必须是非负整数)，才返回True。一旦有空格，分号或其他字符，则返回False。下同。
        print('全部为数字')
        return True
    elif s.isalpha():               #必须全为字母（不区分大小写），才返回True
        print('全部为字母')
        return True
    elif s.isalnum():               #必须是混合时才会返回True
        print('数字和字母的组合')
        return True
    else:
        print('为其他（组合）\n')
        return False

def is_number(s):       #传入整型或字符型都可
    '''判断是否为数字（包含整数，小数，负数，复数）'''
    try:
        a = float(s)            #只有数字类型（包括整数小数和负数）才可转换。（但有例外，如：'nan'(包括随便哪个字母大写),'INF','inf','-INF','-inf'也可顺利转换）
        print(a,type(a))
        if str(a) == 'nan' or str(a) == 'inf' or str(a) == '-inf':
            print('不是数字类型')
            return False
        else:
            print('是数字类型')
            return True
    except:
        print('不是数字类型')
    #复数
    try:
        b = complex(s)
        print(b,type(b))
        print('是复数类型')
        return True
    except:
        print('不是复数类型')
        return False

def _main():
    while True:
        s = input('输入一个字符串(输入over结束)：')
        if s == 'over':
            break
        w = what_element(s)
        if w:
            pass
        else:
            is_number(s)
            pass

if __name__ == '__main__':
    _main()

"""
isdigit	    数字
isalpha	    字母
isalnum	    字母或数字
isspace	    空格
isdecimal	十进制数字
islower	    小写字母
isupper	    大写字母
istitle	    单词首字母大写
"""