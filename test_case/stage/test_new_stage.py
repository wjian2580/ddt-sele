# -*- coding: utf-8 -*-

import unittest
from page.base import OkrTest

class TestNewStage(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()

	def test_new_stage(self):
		self.create_stage()
		text = self.get_text('css=span.stageTxt')
		self.assertEqual(text,'stage')

if __name__ == "__main__":
	unittest.main()
