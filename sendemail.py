import smtplib
from email.mime.text import MIMEText
from email.header import Header
class sendemail:
    def __init__(self):
        self.sender = '445660334@qq.com'
        self.mail_host = 'smtp.qq.com'
        self.mail_user = '445660334@qq.com'
        self.mail_pass = 'uvxuiqgppxnlbjee'

    def send(self,subject,content,to):
        message = MIMEText(content,'html','utf-8')
        message['From'] = Header('445660334<445660334@qq.com>','ascii')
        message['To'] = Header('dear','ascii')
        message['Subject'] = Header(subject,'utf-8')
        try:
            smtp_obj = smtplib.SMTP_SSL(self.mail_host)
            smtp_obj.login(self.mail_user,self.mail_pass)
            smtp_obj.sendmail(str(self.sender),to,message.as_string())
            smtp_obj.quit()
        except smtplib.SMTPException as e:
            print e.as_string()
            pass 


