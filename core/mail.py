#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from cfg.R import getconfig

__all__ = ['sendmail','sendreport']

sender = getconfig('mail', 'sender')
passwd = getconfig('mail', 'senderPasswd')
receiver = getconfig('mail', 'receiver')

smtpServer = getconfig('mail', 'smtpServer')
smtpPort = getconfig('mail', 'smtpPort')

ipchange: str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jarvis' report</title>
</head>
<body>
<h2>Your cloud has been changed, Sir</h2>
<ul><li>New home address is: {}, please check it.</li></ul>
</body>
</html>
"""

statusReport: str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jarvis' report</title>
</head>
<body>
<h2>Sir, your system has some mistake, I'm trying to fix it.</h2>
<ul><li>New home address is: {}, please check it.</li></ul>
</body>
</html>
"""


def sendreport():
    message = MIMEText(statusReport, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header('A mail from Jarvis', 'utf-8')

    try:
        smtp = smtplib.SMTP(smtpServer, smtpPort)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, passwd)
        smtp.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
        print("Error: 无法发送邮件")


def sendmail(ipaddr: str):
    message = MIMEText(ipchange.format(ipaddr), 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header('A mail from Jarvis', 'utf-8')

    try:
        smtp = smtplib.SMTP(smtpServer, smtpPort)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, passwd)
        smtp.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
        print("Error: 无法发送邮件")
