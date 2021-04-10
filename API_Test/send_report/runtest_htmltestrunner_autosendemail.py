# coding=utf-8
import unittest
from API_Test.HwTestReport.HwTestReport import HTMLTestReport
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#2.定义：取最新测试报告，参数为报告路径
def new_file(test_dir):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(test_dir)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(test_dir,lists[-1])
    return file_path

#3.定义：发送邮件，发送最新测试报告html
def send_email(newfile):
    try:
        f=open(newfile,'rb')
        mail_body=f.read()
        f.close()
        #发送邮箱服务器
        smtpserver = 'smtp.163.com'
        user = '13628165081'
        password='AXZFPNMGEGVHFKWY' #授权码
        #发送邮箱
        sender='13628165081@163.com'
        receiver=['13628165081@163.com']
        #发送邮件主题
        subject = '接口自动化测试报告'

        #编写 HTML类型的邮件正文
        msg=MIMEMultipart('mixed')

        #注意：由于msg_html在msg_plain后面，所以msg_html以附件的形式出现
        #text = "Dear all!\n附件是最新的测试报告。\n麻烦下载下来看，用谷歌浏览器打开查看，附件包含所有案例执行详情。\n请知悉，谢谢。"
        #msg_plain = MIMEText(text,'plain', 'utf-8')
        #msg.attach(msg_plain)

        msg_html2 = MIMEText(mail_body,'html','utf-8')
        msg.attach(msg_html2)

        msg_html = MIMEText(mail_body,'html','utf-8')
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html)

        #要加上msg['From']这句话，否则会报554的错误。
        msg['From'] = '13628165081@163.com <13628165081@163.com>'
        msg['To'] = ";".join(receiver)
        msg['Subject']=Header(subject,'utf-8')

        #连接发送邮件
        smtp=smtplib.SMTP()
        smtp.connect(smtpserver,25)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception as e:
        print("发送邮件失败：" + str(e))

if __name__=='__main__':
    #1.执行测试用例，生成最新的测试用例
    test_dir = 'G:\LocalGit\github\QiuW\API_Test\\test'
    test_report_dir='G:\LocalGit\github\QiuW\API_Test\Test_Report'
    discover=unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    now=time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report_dir+'\\'+ now + 'result.html'
    fp=open(filename ,'wb')
    runner = HTMLTestReport(stream=fp,title=u'测试报告',description=u'用例执行情况，结果详见html附件')
    runner.run(discover)
    fp.close()
    
    #2.取最新测试报告
    new_report=new_file(test_report_dir)

    #3.发送邮件，发送最新测试报告html
    send_email(new_report)
