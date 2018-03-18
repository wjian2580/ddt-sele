#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from tools import tools
from tools.HtmlTestRunner import HTMLTestRunner

case_dir,report = tools.get_path()

try:		
	fp = open(report,'wb')
	cover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py')
	runner = HTMLTestRunner(stream=fp,title='OKR测试报告',description='测试结果：')
	runner.run(cover)
finally:
	fp.close()
tools.send_mail(report)
