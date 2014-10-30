#!/usr/bin/env python
#coding:utf-8

import warnings
warnings.filterwarnings("ignore")

import MySQLdb
import xdrlib
import xlrd

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def open_excel(x_file='file.xls'):
    try:
        data = xlrd.open_workbook(x_file)
        return data
    except Exception,e:
        print str(e)

#根据索引获取excel表格中的数据
#参数：
#-x_file:excel文件路径
#-colnameindex:表头列所在行的索引
#-by_index:表的索引

def excel_table_byindex(x_file='file.xls', colnameindex=0, by_index=0):     #colnameindex一般是文件第一行，为各列的名称
    data = open_excel(x_file)
    table = data.sheets()[by_index]
    nrows = table.nrows    #行数
    ncols = table.ncols    #列数
    colnames = table.row_values(colnameindex)   #列名称一行的数据
    
    lst = []

    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            lst.append(app)
    return lst




if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost',user='root', passwd='123123', db='db_edusoho',charset='utf8')
    cur = con.cursor()
    tables = excel_table_byindex("medu1.xls")
    for row in tables:
        email = row["email"]
        truename = row["truename"]
        city = row["city"]
        company = row["company"]
        job = row["job"]
        segment = row["segment"]
        business = row["business"]
        keyWord = row["keyWord"]
        contact = row["contact"]
        mobile = row["mobile"]
        qq = row["qq"]
    
        cur.execute("insert into user (email) values (%s)",(email))
        cur.execute("insert into user_profile (truename,city,company,job,segment,business,keyWord,contact,mobile,qq) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(truename,city,company,job,segment,business,keyWord,contact,mobile,qq))
    con.commit()

