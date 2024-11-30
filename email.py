import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# 邮件配置信息
smtp_server = "smtp.gmail.com"  # SMTP 服务器地址
smtp_port = 587  # SMTP 端口
email_user = "cryptotangyou@gmail.com"  # 发送者邮箱
email_password = "abc84845389"  # 发送者邮箱密码（或应用密码）
recipient_email = "farmerlesheng@gmail.com"  # 接收者邮箱

def send_email():
    try:
        # 创建邮件对象
        message = MIMEMultipart()
        message["From"] = email_user
        message["To"] = recipient_email
        message["Subject"] = "Hello World"  # 邮件主题

        # 邮件正文
        body = "Hello World"
        message.attach(MIMEText(body, "plain"))

        # 连接到 SMTP 服务器
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # 启用 TLS 加密
            server.login(email_user, email_password)  # 登录 SMTP 服务器
            server.send_message(message)  # 发送邮件
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# 每隔 60 秒发送邮件
while True:
    send_email()
    time.sleep(60)
