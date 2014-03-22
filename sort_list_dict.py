#!/usr/bin/env python
#coding:utf-8

"""
有一个列表，列表里面是字典。把这个列表中的字典，按照字典中的某个键中的value排序。
举个例子。

aList=[{'a':'f','b':'1'},{'a':'y',b:'2'},{'a':'x',b:'3'},{'a':'g',b:'4'},]
要求：根据key'a'中的value：'f'和'g' 'x' 'y'进行排序,得到：
aList=[{'a':'f','b':'1'},{'a':'g',b:'4'},{'a':'x',b:'3'},{'a':'y',b:'2'},]
"""

alist=[{'a':'f','b':1},{'a':'y','b':'2'},{'a':'x','b':'3'},{'a':'g','b':'4'},]

tmp = []
for item in alist:
    tmp.append(item['a'])
tmp = sorted(tmp)

print tmp

num = []
for item in tmp:
    for item2 in alist:
        if item == item2['a']:
            num.append(item2)

print num

"""
if __name__ == "__main__":
    print count_vowels()
"""
