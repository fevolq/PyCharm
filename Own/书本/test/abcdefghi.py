#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:123456789,每个数选一次组成三个三位数，使abc + def = ghi成立

def Sum(l):
    sum = []
    for x in l:
        for y in l:
            for z in l:
                if x == y or x == z or y == z:
                    pass
                else:
                    sum.append(x*100+y*10+z)
    sum.sort()
    # print(sum[len(sum)//2])
    return sum

def search(sum):
    all = []
    num = len(sum)
    # for x in range(num//2 + 1):
    for x in range(num):
        a = sum[x]
        if a >=493:
            break
        a1 = a // 100
        a2 = (a // 10) % 10
        a3 = a % 10
        for y in range(x+1,num-1):
            b = sum[y]
            b1 = b // 100
            b2 = (b // 10) % 10
            b3 = b % 10
            dict = {a1,a2,a3,b1,b2,b3}
            if len(dict) != 6:
                continue
            for z in range(y+1,num):
                c = sum[z]
                c1 = c // 100
                c2 = (c // 10) % 10
                c3 = c % 10
                dict = {a1, a2, a3, b1, b2, b3,c1,c2,c3}
                if len(dict) != 9:
                    continue
                if a + b == c:
                    # print('{} + {} = {}  '.format(a,b,c))
                    r = '{} + {} = {}      '.format(a,b,c)
                    all.append(r)
    return all

def write(l):
    with open('C:\\Users\\15394\\Desktop\\算式.txt','w+') as f:
        for i in range(len(l)):
            f.write(l[i])
            if (i+1)%6 == 0:
                f.write('\n')

def main(l):
    sum = Sum(l)
    all = search(sum)
    write(all)

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9]
    main(l)
    print('\nDone')



