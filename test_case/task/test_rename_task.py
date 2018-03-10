# -*- coding: utf-8 -*-
from page.base import OkrTest
import unittest

class TestTask(OkrTest):

	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()

	def test_task(self):
		self.click('css=td.taskInto')
		self.click('css=li.opt_tast.resetName')
		self.send_keys('css=td.taskInto > div > div > input','renamed')
		self.click('css=button.btn_tast')
		self.sleep()
		text = self.get_text('css=i.taskTxt')
		self.assertEqual(text,'renamed')

if __name__ == "__main__":
	unittest.main()
