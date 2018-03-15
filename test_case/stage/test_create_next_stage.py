# -*- coding: utf-8 -*-
from page.base import OkrTest
import unittest

class TestCreateNextStage(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()
		self.create_stage()

	def test_create_next_stage(self):
		self.click('css=span.stageTxt')
		self.click('css=li.opt.stage_addNext')
		self.send_keys('css=th.stage_th > div > div > input','nextStage')
		self.click('css=th.stage_th > div > div > button')
		self.sleep()
		text = self.get_text('css=#project_one > thead > tr > th:nth-child(3) > span')
		self.assertEqual(text,'nextStage')

if __name__ == "__main__":
	unittest.main()