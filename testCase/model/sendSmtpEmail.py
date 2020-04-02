# -- coding: utf-8 --
import smtplib#发送邮件模板
from email.mime.text import MIMEText#定义邮件内容
from email.header import Header#定义邮件标题
from email.mime.multipart import MIMEMultipart#用于传送附件

class sendSmptEmail():
    def send_email(Latest_Report):
        #读取最新测试报告的内容
        with open(Latest_Report,'rb') as e:
            mail_content=e.read()
            e.close()

            smtpserver = 'smtp.163.com'  # 发送邮件所用的服务器
            user = '***@163.com'
            password = '***'

            # 发送邮件地址和接收地址
            sender = '***@163.com'
            receives = ['***@qq.com']

            # 定义邮件标题和内容
            subject = '帝国CMS普通会员前台UI自动化测试报告'

            # msgRoot = MIMEText(mail_content, "html", 'utf-8')
            msgRoot = MIMEMultipart()
            msgRoot['Subject'] = Header(subject, 'utf-8')  # 标题类型
            msgRoot['From'] = sender
            msgRoot['To'] = ','.join(receives)

            # 发送附件
            att = MIMEText(mail_content, "base64", "utf-8")#base64表示附件;
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename="test_report.html"'  # 定义附件名称
            msgRoot.attach(att)  # 挂起

            smtp = smtplib.SMTP_SSL(smtpserver, 994)  # SSL协议端口号要使用465或994
            smtp.helo(smtpserver)  # HELO向服务器标志用户身份
            smtp.ehlo(smtpserver)  # 服务器返回结果确认
            smtp.login(user, password)

            print('start send Email...')
            smtp.sendmail(sender, receives, msgRoot.as_string())  # 发送地址；邮件接收地址；发送信息
            smtp.quit()
            print('send end...')






