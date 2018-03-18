# -*- coding: utf-8 -*-

import unittest
from page.base import OkrTest

class TestNewStage(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()
		self.create_stage()

	def test_new_stage(self):
		self.click('css=span.stageTxt')
		self.click('css=li.opt.resetName')
		self.send_keys('css=th.stage_th > div > div > input','renamed')
		self.click('css=th.stage_th > div > div > button')
		self.sleep()
		text = self.get_text('css=span.stageTxt')
		self.assertEqual(text,'renamed')

if __name__ == "__main__":
	unittest.main()
