#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import os
from common import S_Log
from email.mime.text import MIMEText
from email.header import Header


current_dir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(current_dir)
logger=S_Log.LogClass()


class configMail:


    def __init__(self):
        # 第三方 SMTP 服务
        self.mail_host = "smtp.qq.com"  # 设置服务器
        self.mail_user = "842632533@qq.com"  # 用户名
        self.mail_pass = "pfddrerfidukbfdc"  # 口令
        self.sender = '842632533@qq.com'
        self.receivers = ['spf@youxiake.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱




    def getSendmsg(self,fileName):
        fp = open(parent_path + "\\relust\\"+fileName+".html", "r", encoding="UTF-8")
        self.msg = str(fp.read())
        self.message = MIMEText(self.msg, 'html', 'utf-8')
        self.message['From'] = Header("接口测试服务", 'utf-8')
        self.message['To'] = Header("接受者", 'utf-8')
        self.subject = '新鲜的接口测试报告出炉啦~~~~'
        self.message['Subject'] = Header(self.subject, 'utf-8')



    def send(self,fileName):
        self.getSendmsg(fileName)
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, self.message.as_string())
            logger.log_info("邮件发送成功")
        except smtplib.SMTPException as x:
            
            logger.log_info("Error: 无法发送邮件")
            logger.log_info(x)


if __name__ == "__main__":
    configMail().send("result202092020-09-25")








