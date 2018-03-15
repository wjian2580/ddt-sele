# -*- coding: utf-8 -*-
from page.base import OkrTest
from selenium.webdriver.common.keys import Keys
import pdb
import random
import unittest

class TestNewLeader(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()
		self.create_stage()

	def test_new_leader(self):
		self.click('css=img.change')
		element=self.driver.find_element_by_css_selector('input.name')
		element.send_keys('宋玉玲')
		element.send_keys(Keys.ENTER)
		self.click('css=li.lis')
		self.click('css=input.date')
		self.click('css=span.laydate-btns-now')
		self.send_keys('css=#textarea','detail')

if __name__ == "__main__":
	unittest.main()
