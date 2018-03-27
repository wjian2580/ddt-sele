# -*- coding: utf-8 -*-

import unittest
from page.base import OkrTest

class TestTask(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.login()
		self.create_project()
		self.create_task()

#	@unittest.skip('reason')
	def test_new_task(self):	
		text = self.get_text('css=#project_one > tbody > tr > td.taskInto > span > i')
		self.assertEqual(text,'test_task')


#	@unittest.skip('reason')
	def test_create_same_level_task(self):	
		self.click('css=img.taskpng')
		self.click('css=li.opt_tast.stage_addPre')
		self.send_keys('css=td.taskInto > div > div > input','samelevel')
		self.click('css=button.btn_tast')
		self.sleep()
		text = self.get_text('css=#project_one > tbody > tr:nth-child(2) > td.taskInto > span > i')
		self.assertEqual(text,'samelevel')

#	@unittest.skip('reason')
	def test_create_subordinate_task(self):		
		self.click('css=i.taskTxt')
		self.click('css=li.opt_tast.stage_addNext')
		self.send_keys('css=td.taskInto > div > div > input','sub')
		self.click('css=button.btn_tast')
		self.click('css=td.taskInto > span > b')
		text = self.get_text('css=i.taskTxt')
		self.assertEqual(text,'sub')

#	@unittest.skip('reason')
	def test_rename_task(self):
		self.click('css=i.taskTxt')
		self.click('css=li.opt_tast.resetName')
		self.send_keys('css=td.taskInto > div > div > input','renamed')
		self.click('css=button.btn_tast')
		self.sleep()
		text = self.get_text('css=i.taskTxt')
		self.assertEqual(text,'renamed')
	
#	@unittest.skip('reason')
	def test_delete_task(self):
		self.click('css=i.taskTxt')
		self.click('css=li.opt_tast.stage_delet')
		self.click('css=button.btn_tast')
		self.sleep()
		text = self.get_text('css=i.taskTxt')
		self.assertNotEqual(text,'test_task')

if __name__ == "__main__":
	unittest.main()
