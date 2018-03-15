# -*- coding: utf-8 -*-
import unittest
from page import base

class TestRenameProject(base.OkrTest):

	def setUp(self):
		super().setUp()
		self.create_project()
		
	def test_rename_project(self):
		self.rename_project('renamed')
		project = self.get_text('css=#projectList > li:last-child')
		self.assertEqual(project,'renamed')
	
if __name__ == "__main__":
	unittest.main()
