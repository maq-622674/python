#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import getpass

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')
from_addr = "lws__xinlang@sina.com"
password = "liwenshuai1"
to_addr = "lws__xinlang@sina.com"



#from_addr = input("请输入你的账户:")
#passwd = getpass.getpass("请输入你的密码:")
#to_addr = input("输入你发往邮箱的地址 目前只支持新浪邮箱，若想其他请联系管理员:")
#smtp_server = "smtp.sina.com.cn"

#加密SWTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587


msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()