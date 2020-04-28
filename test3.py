# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header


sender = 'ly0572530@163.com'
receiver = ['ly0572531@163.com']

message = MIMEText('test','plain','utf-8')
message['From'] = "{}".format(sender)
message['To'] =",".join(receiver)

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
#
try:
    smtp = smtplib.SMTP_SSL('smtp.163.com',465)

    # smtp.connect('smtp.163.com',25)

    smtp.login('ly0572530@163.com','ly0572530')

    smtp.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

