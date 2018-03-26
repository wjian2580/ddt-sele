# -*- coding: utf-8 -*-

import os
import pdb
import time
import yaml
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  
from email.mime.application import MIMEApplication

def _config_parse(item):
	with open('tools/email.yml',encoding='utf-8') as y:
		config = yaml.load(y)
	if config.get(item):
		return config[item]
	else:
		raise KeyError('配置项：%s不存在'% item)


def get_path():
	day = time.strftime("%Y-%m-%d")
	times = time.strftime("%H_%M_%S")

	root = os.getcwd()
	case_dir = os.path.join(root,r'test_case')
	report_dir = os.path.join(root,'test_report')
	report_day = os.path.join(report_dir,day)
	file_name = times + '-report.html'

	report = os.path.join(report_day,file_name)
	if not os.path.exists(report_day):
		os.mkdir(report_day)
	return case_dir,report


def send_mail(report):
	email = _config_parse('email')
	from_addr,to_addr,smtp_server,port,password = [email[i] for i in email]
	now_time = time.strftime("%Y-%m-%d")

	msg = MIMEMultipart()
	msg['Subject'] = Header(now_time+'-OKR测试报告', 'utf-8').encode()
	msg['From'] = from_addr
	for receiver in to_addr:
		msg['To'] = receiver

	text = '''hi,all:\n\n\t本次测试结果见附件'''
	msg.attach(MIMEText(text, 'plain', 'utf-8'))

	part = MIMEApplication(open(report,'rb').read())  
	part.add_header('Content-Disposition', 'attachment', filename="report.html")  
	msg.attach(part)  

	server = smtplib.SMTP_SSL(smtp_server, port) 
	server.helo(smtp_server)
	server.ehlo(smtp_server)
	server.login(from_addr, password)
	server.sendmail(from_addr, to_addr, msg.as_string())
	server.quit()
