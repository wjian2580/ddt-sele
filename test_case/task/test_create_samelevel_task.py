# -*- coding: utf-8 -*-
from page.base import OkrTest
import pdb
import random
import unittest

class TestCreateSamelevelTask(OkrTest):

	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()

	def test_create_same_level_task(self):	

		self.click('css=img.taskpng')
		self.click('css=li.opt_tast.stage_addPre')
		self.send_keys('css=td.taskInto > div > div > input','samelevel')
		self.click('css=button.btn_tast')
		self.sleep()
		text = self.get_text('css=#project_one > tbody > tr:nth-child(2) > td.taskInto > span > i')
		self.assertEqual(text,'samelevel')

if __name__ == "__main__":
	unittest.main()
