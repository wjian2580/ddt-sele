# -*- coding: utf-8 -*-
from page.base import OkrTest
import pdb
import random
import unittest



class TestCreateSubordinateTask(OkrTest):

	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()

	def test_create_subordinate_task(self):
		
		self.click('css=i.taskTxt')
		self.click('css=li.opt_tast.stage_addNext')
		self.send_keys('css=td.taskInto > div > div > input','sub')
		self.click('css=button.btn_tast')
		self.click('css=td.taskInto > span > b')
		text = self.get_text('css=i.taskTxt')
		self.assertEqual(text,'sub')

if __name__ == "__main__":
	unittest.main()
