# -*- coding: utf-8 -*-
from page.base import OkrTest
import pdb
import random
import unittest

class TestNewTask(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.create_project()

	def test_new_task(self):
		self.create_task('new_task')
		text = self.get_text('css=#project_one > tbody > tr > td.taskInto > span > i')
		self.assertEqual(text,'new_task')

if __name__ == "__main__":
	unittest.main()
