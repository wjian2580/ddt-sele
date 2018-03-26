# -*- coding: utf-8 -*-

import unittest
from page.base import OkrTest

class TestStage(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.login()
		self.create_project()
		self.create_task()
		self.create_stage()

	def test_new_stage(self):
		text = self.get_text('css=span.stageTxt')
		self.assertEqual(text,'stage')

	def test_create_pre_stage(self):
		self.click('css=span.stageTxt')
		self.click('css=li.opt.stage_addPre')
		self.send_keys('css=th.stage_th > div > div > input','pre_stage')
		self.click('css=th.stage_th > div > div > button')
		self.sleep()
		text = self.get_text('css=#project_one > thead > tr > th:nth-child(2) > span')
		self.assertEqual(text,'pre_stage')

	def test_create_next_stage(self):
		self.click('css=span.stageTxt')
		self.click('css=li.opt.stage_addNext')
		self.send_keys('css=th.stage_th > div > div > input','nextStage')
		self.click('css=th.stage_th > div > div > button')
		self.sleep()
		text = self.get_text('css=#project_one > thead > tr > th:nth-child(3) > span')
		self.assertEqual(text,'nextStage')

	def test_rename_stage(self):
		self.click('css=span.stageTxt')
		self.click('css=li.opt.resetName')
		self.send_keys('css=th.stage_th > div > div > input','renamed')
		self.click('css=th.stage_th > div > div > button')
		self.sleep()
		text = self.get_text('css=span.stageTxt')
		self.assertEqual(text,'renamed')

	def test_delete_stage(self):
		self.click('css=span.stageTxt')
		self.click('css=li.opt.stage_delet')
		self.click('css=th.stage_th > div > div > button')
		self.sleep()
		text = self.get_text('css=span.stageTxt')
		self.assertNotEqual(text,'stage')

if __name__ == "__main__":
	unittest.main()
