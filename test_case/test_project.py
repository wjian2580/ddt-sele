# -*- coding: utf-8 -*-

import unittest
from page.base import OkrTest

class TestProject(OkrTest):

	def setUp(self):
		super().setUp()
		self.login()
		self.create_project()
		
	def test_create_project(self):
		project = self.get_text('css=#projectList > li:last-child')
		self.assertEqual(project,'testing')

	def test_rename_project(self):
		self.rename_project('renamed')
		project = self.get_text('css=#projectList > li:last-child')
		self.assertEqual(project,'renamed')
		self.delete_project()

	def test_delete_project(self):
		self.delete_project()
		project = self.get_text('css=#projectList > li:last-child')
		self.assertNotEqual(project,'testing')
	
if __name__ == "__main__":
	unittest.main()
