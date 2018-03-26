# -*- coding: utf-8 -*-

import unittest
from page.base import OkrTest
from selenium.common.exceptions import TimeoutException

class TestLeader(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.login()
		self.create_project()
		self.create_task()
		self.create_stage()
		self.create_leader()

#	@unittest.skip('reason')
	def test_new_leader(self):
		leader = self.get_text('css=p.td_name')
		self.assertEqual(leader,'王健')

#	@unittest.skip('reason')
	def test_mark_done(self):
		self.click('css=p.td_name')
		self.click('css=input.checkbox')
		self.click('css=input.btn')
		self.sleep(2)
		text = self.get_text('css=p.td_tip')
		self.assertEqual(text,'已完成')	

#	@unittest.skip('reason')
	def test_delete_leader(self):
		self.move_to_element('css=div.td')
		self.click('css=img.cardclose')
		self.click('css=#delet_car_conf')
		self.sleep(2)
		with self.assertRaises(TimeoutException):
			self.get_text('css=p.td_name')

if __name__ == "__main__":
	unittest.main()
