# -*- coding: utf-8 -*-
from page.base import OkrTest
import pdb
import random
import unittest



class TestTask(OkrTest):
	''''''
	def test_task(self):
		self.login()
		self.create_project()
		self.click('css=td.taskInto')
		self.send_keys('css=td.taskInto > div > div > input','test_task')
		self.click('css=td.taskInto > div > div > button')

		self.click('css=img.taskpng')
		self.click('css=li.opt_tast.stage_addPre')
		self.send_keys('css=td.taskInto > div > div > input','tongji')
		self.click('css=button.btn_tast')
		self.sleep()

		self.click('css=#project_one > tbody > tr:nth-child(1) > td.taskInto > span > i')
		self.click('css=li.opt_tast.stage_addNext')
		self.send_keys('css=td.taskInto > div > div > input','xiaji')
		self.click('css=button.btn_tast')
		self.click('css=td.taskInto > span > b')
		text = self.get_text('css=i.taskTxt')
		self.assertEqual(text,'xiaji')

		# driver.find_element_by_css_selector('th.stage_th > span').click()
		# driver.find_element_by_css_selector('th.stage_th > div > div > input').send_keys('phase1')
		# driver.find_element_by_css_selector('th.stage_th > div > div > button').click()
		# driver.find_element_by_css_selector('th.stage_th > span').click()
		# driver.find_element_by_css_selector('li.opt.stage_addPre').click()
		# driver.find_element_by_css_selector('th.stage_th > div > div > input').send_keys('phase0')
		# driver.find_element_by_css_selector('th.stage_th > div > div > button').click()
		# driver.find_element_by_css_selector('th.stage_th > span').click()
		# driver.find_element_by_css_selector('li.opt.stage_addNext').click()
		# driver.find_element_by_css_selector('th.stage_th > div > div > input').send_keys('phase2')
		# driver.find_element_by_css_selector('th.stage_th > div > div > button').click()
		# driver.find_element_by_css_selector('img.change').click()
		# driver.find_element_by_css_selector('div.leader > input').send_keys('王健')
		# driver.find_element_by_css_selector('div.leader > input').click()
		# driver.find_element_by_css_selector('div.duetime > div > input').click()
		# driver.find_element_by_css_selector('span.laydate-btns-now').click()
		# driver.find_element_by_css_selector('span.laydate-btns-now').click()
		# driver.find_element_by_css_selector('span.laydate-btns-now').click()
		# driver.find_element_by_css_selector('#textarea').send_keys('详情')
		# driver.find_element_by_css_selector('body > div.detail > input').click()

		# self.click()

		# self.click('css=img.change')
		# self.send_keys('css=th.stage_th > div.box-card > div.el-card_body > input.addInp','phase1')
		# self.click('css=button.btn.stagename')
		# self.click('css=span.stageTxt')
		# self.click('css=li.opt.stage_addNext')
		# self.send_keys('css=th.stage_th > div.box-card > div.el-card_body > input.addInp','phase2')
		# self.click('css=th.stage_th > div.box-card > div.el-card_body > button.btn')
		# self.click('css=span.stageTxt')
		# self.click('css=li.opt.stage_addPre')
		# self.send_keys('css=th.stage_th > div.box-card > div.el-card_body > input.addInp','0')
		# self.click('css=th.stage_th > div.box-card > div.el-card_body > button.btn')
		# self.click('css=div.td > span')
		# self.send_keys('css=input.name','王健')
		# self.click('css=li.lis')
		# self.click('css=div.detail')
		# self.click('css=span.laydate-btns-now')
		# self.click('id=textarea')
		# self.send_keys('id=textarea','123')
		# self.click('css=input.btn')

if __name__ == "__main__":
	unittest.main()
