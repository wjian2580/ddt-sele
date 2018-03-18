# -*- coding: utf-8 -*-

import unittest
from page import base

class TestDeleteProject(base.OkrTest):

	def setUp(self):
		super().setUp()
		self.create_project()
	
	def test_delete_project(self):
		self.delete_project()
		project = self.get_text('css=#projectList > li:last-child')
		self.assertNotEqual(project,'testing')
	
if __name__ == "__main__":
	unittest.main()
