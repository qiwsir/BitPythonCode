#!/usr/bin/env python
#coding:utf-8

#让开发人员在IDE中打印出对象的所有函数和它们的doc string
#接收任何含有函数或者方法的对象
#使用方法，
#from find_object_doc import info
#info(object)
#也可以增加参数。

def info(object,spacing=10,collapse=1):    #声明函数，有三个变量，后面两个是可选参数
    """Print methods and doc strings.    #多行doc string，介绍函数功能
    Takes module,class,list,dictionary,or string."""

    methodList = [method for method in dir(object) if callable(getattr(object,method))]
    #dir 函数返回任意对象的属性和方法列表，包括模块对象、函数对象、字符串对象、列表对象、字典对象...
    #callable 函数，接收任何对象做为参数，如果参数对象是可调用的，返回True;否则返回False.可调用对象包括函数、类方法，甚至类自身
    #getattr 函数，可以得到一个直到运行时才知道名称的函数引用

    processFunc = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)
    #lambda 函数：在参数列表周围没有括号，忽略了return关键字。没有函数名称。可以赋值给一个变量调用
    #不需要将它赋值给一个变量。
    #可以接收任意多个参数并且返回单个表达式的值。
#不能包含命令，包含的表达式不能超过一个。
#不要试图向lambda函数中塞入太多的东西。如果需要复杂的东西，应该定义普通函数

    print "\n".join(["%s%s"%
                    (method.ljust(spacing),
                    processFunc(str(getattr(object,method).__doc__)))
                    for method in methodList])
#ljust 用空格填充字符串以符合指定长度，如果指定的长度小于字符串长度，将返回未变化的字符串，不会截取字符串。

if __name__ == "__main__":    #这样允许这个程序独立运行，又不妨碍做为其它程序的模块使用
    print info.__doc__
