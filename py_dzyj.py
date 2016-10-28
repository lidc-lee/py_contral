# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: py_dzyj.py
@time: 2016/10/14 14:25
"""
# 电子邮件远程控制


import poplib
import smtplib
from email.header import decode_header
from email.mime.text import MIMEText
import email

# 如何读取邮件
read = poplib.POP3('')