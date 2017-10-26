import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart

my_sender = 'shift_1220@163.com'  # 发件人邮箱账号
my_pass = 'password'  # 发件人邮箱密码(即授权码就是登录密码，授权码在所在的邮箱中设置)
my_user = '172667104@qq.com'  # 收件人邮箱账号，我这边发送给自己

def mail():
    ret = True
    try:
        msg = MIMEText('测试邮件', 'plain', 'utf-8') #邮件正文
        msg['From'] = formataddr(["Change", my_sender])  # 发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["Fuck you", my_user])  # 收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "发送邮件测试"  # 邮件的主题
        server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的服务器，即SMTP中的SSL服务端口，465或994
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件,可发送给多人
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret

#
ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")