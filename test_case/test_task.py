# -*- coding: utf-8 -*-
import time
from page.base import OkrTest
import pdb
import random
import unittest



class TestTask(OkrTest):
	''''''
	def test_task(self):
		driver = self.driver
		self.login(driver)
		time.sleep(2)
		self.create_project(driver)
		self.click('css=img.gotoTask')
		self.click('css=#proName > img')
		self.click('css=td.taskInto')
		self.click('css=span.tastPro > img.taskpng')
		self.click('css=li.opt_tast.stage_addPre')
		self.send_keys('css=td.taskInto > div.box-card > div.el-card_body > input.addInp','tongji')
		self.click('css=button.btn_tast')
		self.click('css=i.taskTxt')
		self.click('css=li.opt_tast.stage_addNext')
		self.send_keys('css=td.taskInto > div.box-card > div.el-card_body > input.addInp','xiaji')
		self.click('css=button.btn_tast')
		self.click('css=b.intoChilerenTask')
		self.click('css=i.taskTxt')
		self.click('css=li.opt_tast.stage_addNext')
		self.send_keys('css=td.taskInto > div.box-card > div.el-card_body > input.addInp','xiaji1')
		self.click('css=button.btn_tast')
		self.click('css=img.change')
		self.send_keys('css=th.stage_th > div.box-card > div.el-card_body > input.addInp','phase1')
		self.click('css=button.btn.stagename')
		self.click('css=span.stageTxt')
		self.click('css=li.opt.stage_addNext')
		self.send_keys('css=th.stage_th > div.box-card > div.el-card_body > input.addInp','phase2')
		self.click('css=th.stage_th > div.box-card > div.el-card_body > button.btn')
		self.click('css=span.stageTxt')
		self.click('css=li.opt.stage_addPre')
		self.send_keys('css=th.stage_th > div.box-card > div.el-card_body > input.addInp','0')
		self.click('css=th.stage_th > div.box-card > div.el-card_body > button.btn')
		self.click('css=div.td > span')
		self.send_keys('css=input.name','王健')
		self.click('css=li.lis')
		self.click('css=div.detail')
		self.click('css=span.laydate-btns-now')
		self.click('id=textarea')
		self.send_keys('id=textarea','123')
		self.click('css=input.btn')

if __name__ == "__main__":
	unittest.main()
