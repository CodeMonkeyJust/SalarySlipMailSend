# encoding= utf-8
# ------------------------------------------------------------------
# Author:zhulijun
# Created:2021-09-09
# Description:邮件发送
# ------------------------------------------------------------------
import smtplib
from email.mime.text import MIMEText
from log_unit import write_log
from workspace import get_log_filename, get_config_filename
from config_unit import get_config

# 设置服务器所需信息
# 邮箱服务器地址
mail_host = ''
# 1用户名
mail_user = ''
# 密码(部分邮箱为授权码)
mail_pass = ''
# 邮件发送方邮箱地址
mail_sender = ''


def sendmail(subject, content, receivers):
    # 登录并发送邮件
    try:
        load_config()
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 设置email信息
        # 邮件内容，三个参数：第一个为文本内容，第二个 html 设置文本格式plain.html，第三个 utf-8 设置编码
        message = MIMEText(content, 'html', 'utf-8')
        # 邮件主题
        message['Subject'] = subject
        # 发送方信息
        message['From'] = mail_sender
        # 接受方信息
        message['To'] = receivers[0]
        # 发送
        smtpObj.sendmail(
            mail_sender, receivers, message.as_string())
        # 发送完毕后退出smtp
        smtpObj.quit()
        write_log(get_log_filename(), str(subject) + ' ' + str(receivers) + '[发送成功]')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误
        write_log(get_log_filename(), str(subject) + ' ' + str(receivers) + str(e) + '[发送失败]')


def load_config():
    global mail_host, mail_user, mail_pass, mail_sender
    mail_host = get_config(get_config_filename(), 'send', 'mail_host')
    mail_user = get_config(get_config_filename(), 'send', 'mail_user')
    mail_pass = get_config(get_config_filename(), 'send', 'mail_pass')
    mail_sender = get_config(get_config_filename(), 'send', 'mail_sender')


if __name__ == '__main__':
    sendmail('6月工资条-张小米', '邮件信息，内容为空', ['zhulj@pde.com.cn'])  # 调用发送邮箱的函数
