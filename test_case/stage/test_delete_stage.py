# -*- coding: utf-8 -*-
from page.base import OkrTest
import unittest

class TestDeleteStage(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()
		self.create_stage()

	def test_delete_stage(self):
		self.click('css=span.stageTxt')
		self.click('css=li.opt.stage_delet')
		self.click('css=th.stage_th > div > div > button')
		self.sleep()
		text = self.get_text('css=span.stageTxt')
		self.assertNotEqual(text,'stage')

if __name__ == "__main__":
	unittest.main()