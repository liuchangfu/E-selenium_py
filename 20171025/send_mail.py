import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮件服务器
smtpserver = "192.168.10.3"

#发送邮件用户名和密码
user = 'liucf@cm.mail'
password = 'lcfwku'

#发送邮箱
sender = 'liucf@cm.mail'
# 接收邮件
receiver = 'liucf@cm.mail'

#发送邮件主题
subject = 'Python email test!!'

#编写HTML类型的邮件正文
msg = MIMEText('Hello world!!','plain','utf-8')
#发件人名称
msg['From'] = Header("刘昌富", 'utf-8')
#收件人名称
msg['To'] =  Header("刘昌富1", 'utf-8')
msg['Subject'] = Header(subject,'utf-8')

#连接发送邮件
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print("邮件发送成功!")
except smtplib.SMTPException:
    print("邮件发送失败！")