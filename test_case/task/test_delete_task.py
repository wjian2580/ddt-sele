# -*- coding: utf-8 -*-
from page.base import OkrTest
import pdb
import random
import unittest



class TestDeleteTask(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()

	def test_delete_task(self):
		self.click('css=i.taskTxt')
		self.click('css=li.opt_tast.stage_delet')
		self.click('css=button.btn_tast')
		self.sleep()
		text = self.get_text('css=i.taskTxt')
		self.assertNotEqual(text,'test_task')

if __name__ == "__main__":
	unittest.main()
