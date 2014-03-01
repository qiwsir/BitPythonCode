#!/usr/bin/env python
#coding:utf-8

"""
创建一个函数,它接受一个单词列表,每个单词,发现元音的数量。每个单词的元音数量应放置在一个列表,以便元音的数量在同一元素作为它所代表的单词。返回的列表项。
"""

def count_vowels():
    words = []
    number_vowels = []
    vowels = 'aeiou'
    while True:
        input_str = raw_input("Please input words:\n").strip()  #输入单词
        if input_str == "q":
            break
        words.append(input_str)    #输入的单词追加到words

        #for item in words:    #循环得到words中的单词
        #    num = 0
        #    for char in item:   #循环得到每个字母
        #        if char in vowels:    #判断是否为原因
        #            num = num+1
        #    number_vowels.append(num)

#上述的引号中的是一种写法，下面另外一种方法
        
        num = 0
        for char in input_str:
            if char in vowels:
                num = num+1
        number_vowels.append(num)
        return number_vowels

if __name__ == "__main__":
    print count_vowels()
