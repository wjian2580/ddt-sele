# -*- coding: utf-8 -*-
import unittest
from page import base

class TestCreateProject(base.OkrTest):
		
	def test_create_project(self):
		self.create_project('create')
		project = self.get_text('css=#projectList > li:last-child')
		self.assertEqual(project,'create')
	
if __name__ == "__main__":
	unittest.main()
