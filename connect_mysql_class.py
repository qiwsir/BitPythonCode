#!/usr/bin/env python
# -- coding:utf-8 --

import logging
import MySQLdb

class _MySQL(object):
     def __init__(self, host, port, user, passwd, db, charset='utf8'):
        self.conn = MySQLdb.connect(
                host = host,
                port = port,
                user = user,
                passwd = passwd,
                db = db,
                charset = charset)

    def get_cursor(self):
        return self.conn.cursor()

    def query(self, sql):
        cursor = self.get_cursor()  
        try:
            cursor.execute(sql, None)
            result = cursor.fetchall()  
        except Exception, e:
            logging.error("mysql query error: %s", e)
            return None
        finally:
            cursor.close()
        return result

    def execute(self, sql, param=None):
        cursor = self.get_cursor()
        try:
            cursor.execute(sql, param)
            self.conn.commit()
            affected_row = cursor.rowcount
        except Exception, e:
            logging.error("mysql execute error: %s", e)
            return 0
        finally:
            cursor.close()
        return affected_row

    def executemany(self, sql, params=None):
        cursor = self.get_cursor()
        try:
            cursor.executemany(sql, params)
            self.conn.commit()
            affected_rows = cursor.rowcount
        except Exception, e:
            logging.error("mysql executemany error: %s", e)
            return 0
        finally:
            cursor.close()
        return affected_rows

    def close(self):
        try:
            self.conn.close()
        except:
            pass

    def __del__(self):
        self.close()


host = 'localhost'
port = 3306
user = 'root'
passwd = '123456'
db = 'foo'

mysql = _MySQL(host, port, user, passwd, db)

def create_table():
    table = """
            CREATE TABLE IF NOT EXISTS `watchdog`(
                `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                `name` varchar(100),
                `price` int(11) NOT NULL DEFAULT 0
            ) ENGINE=InnoDB charset=utf8;
            """
    print mysql.execute(table)

def insert_data():
    params = [('dog_%d' % i, i) for i in xrange(12)]
    sql = "INSERT INTO `watchdog`(`name`,`price`) VALUES(%s,%s);"   
    print mysql.executemany(sql, params) 

if __name__ == '__main__':
    create_table()
    insert_data()

