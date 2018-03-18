# -*- coding: utf-8 -*-

import pdb
import random
import unittest
from page.base import OkrTest
from selenium.webdriver.common.keys import Keys

class TestNewLeader(OkrTest):
	''''''
	def setUp(self):
		super().setUp()
		self.create_project()
		self.create_task()
		self.create_stage()

	@unittest.skip('reason')
	def test_new_leader(self):
		expect_leader = '王健'
		self.create_leader(expect_leader)
		leader = self.get_text('css=p.td_name')
		self.assertEqual(leader,expect_leader)

if __name__ == "__main__":
	unittest.main()
