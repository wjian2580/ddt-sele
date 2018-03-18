# -*- coding: utf-8 -*-

import pdb
import random
import unittest
from page.base import OkrTest
from selenium.webdriver.common.keys import Keys

class TestMarkDone(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()
		self.create_stage()
		self.create_leader()

	@unittest.skip('reason')
	def test_mark_done(self):
		self.click('css=p.td_name')
		self.click('css=input.checkbox')
		self.click('css=input.btn')
		self.sleep(2)
		text = self.get_text('css=p.td_tip')
		self.assertEqual(text,'已完成')

if __name__ == "__main__":
	unittest.main()
