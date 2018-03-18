# -*- coding: utf-8 -*-

import unittest
from page.base import OkrTest

class TestCreatePreStage(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()
		self.create_stage()

	def test_create_pre_stage(self):
		self.click('css=span.stageTxt')
		self.click('css=li.opt.stage_addPre')
		self.send_keys('css=th.stage_th > div > div > input','pre_stage')
		self.click('css=th.stage_th > div > div > button')
		self.sleep()
		text = self.get_text('css=#project_one > thead > tr > th:nth-child(2) > span')
		self.assertEqual(text,'pre_stage')

if __name__ == "__main__":
	unittest.main()