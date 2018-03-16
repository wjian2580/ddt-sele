# -*- coding: utf-8 -*-
from page.base import OkrTest
from selenium.webdriver.common.keys import Keys
import pdb
import random
import unittest

class TestMarkDone(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()
		self.create_stage()
		self.create_leader()

#	@unittest.skip('reason')
	def test_mark_done(self):
		self.move_to_element('css=div.td')
		self.click('css=img.cardclose')
		self.click('css=#delet_car_conf')
		self.sleep(2)
		try:
			self.get_text('css=p.td_name')
		
		self.assertEqual(text,'已完成')

if __name__ == "__main__":
	unittest.main()
