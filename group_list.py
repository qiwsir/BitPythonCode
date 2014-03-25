#!/usr/bin/env python
#coding:utf-8

#对列表进行分组，l为列表，block为每个组中的元素数量，如果末尾不足，则将该元素全部归为其中

def group_list(l,block):
    size = len(l)
    return [l[i:i+block] for i in range(0,size,block)]

if __name__=='__main__':
    print group_list(l,block)
