import smtplib
from email.mime.text import MIMEText
import unittest
from HTMLTestRunner import HTMLTestRunner
import time,os
from email.mime.multipart import MIMEMultipart
from email.header import Header
#发送带邮件的函数、动作
def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()
    #基本信息
    smtpserver='smtp.163.com'
    pwd='wcc668439'
    #定义邮件主题
    msg=MIMEMultipart()
    msg['subject']=Header('自动化测试报告','utf-8')
    msg['from']='wu_chengcheng0606@163.com'
    msg['to']='wu_chengcheng0606@163.com'
    #html邮件正文 直接发送邮件的代码片段
    body=MIMEText(mail_body,'html','utf-8')
    msg.attach(body)
    att=MIMEText(mail_body,'base64','utf-8')
    att['Content-Type']='application/octet-stream'
    att['Content-Disposition']='attachment;filname="test_report,html"'
    msg.attach(att)
    #连接邮件服务器发送邮件
    smtp=smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(msg['from'],pwd)
    smtp.sendmail(msg['from'],msg['to'],msg.as_string())
    print('邮件发送成功')
#发送最新邮件
def new_file(test_dir):
    result_dir=test_dir
    lists=os.listdir(result_dir)
    print(lists)
    lists.sort()
    file=[x for x in lists if x.endswith('.html')]
    file_path=os.path.join(result_dir,file[-1])
    return file_path
if __name__ == '__main__':
    test_case_ = os.path.dirname(os.path.realpath(__file__))
    test_case = os.path.join(test_case_, 'test_case')
    test_report = os.path.join(test_case_, 'report')
    test_list = unittest.defaultTestLoader.discover(test_case, pattern='test*.py')

    now=time.strftime('%Y_%m_%d_%H_%M_%S')
    filename=test_report +'\\' +now +'_result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,
                          title='百度测试项目',
                          description='win7 Chrome broeser 55.0 version')
    runner.run(test_list)
    fp.close()
    new_report=new_file(test_report)
    send_mail(new_report)