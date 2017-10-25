import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

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

#创建一个带附件的实例
msgRoot = MIMEMultipart('related')
msgRoot["From"] = Header("Change","utf-8")
msgRoot["To"] = Header("Test","utf-8")
msgRoot['Subject'] = subject
msgRoot.attach(MIMEText("TEST attachment!!!","plain","utf-8"))

#构造附件内容
att_file = open('E:\\selenium_py\\20171024\\geckodriver.log','rb').read()
att = MIMEText(att_file,'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="geckodriver.log"'
msgRoot.attach(att)


#连接发送邮件
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msgRoot.as_string())
    smtp.quit()
    print("邮件发送成功!")
except smtplib.SMTPException:
    print("邮件发送失败！")