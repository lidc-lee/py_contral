# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: py_main.py
@time: 2016/10/14 14:38
"""
import os
import poplib
import smtplib
from email.header import decode_header
from email.mime.text import MIMEText
import email
import time


def read():
    a = 1
    return a


# 关机
def guanji():
    pwd = 'dnzgnjhxcruhhhfh'
    sent = smtplib.SMTP('smtp.qq.com')
    sent.login('1499117534@qq.com', pwd)
    to = ['1499117534@qq.com']
    content = MIMEText('')
    content['Subject'] = 'guan'
    content['From'] = '1499117534@qq.com'
    content['To'] = ','.join(to)
    sent.sendmail('1499117534@qq.com', to, content.as_string())
    sent.close()


if __name__ == '__main__':

    if read() == 0:
        os.system('shutdown -s -t 50')  # 关机
    if read() == 1:
        os.system(' shutdown -r')  # 重启
