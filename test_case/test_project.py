# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random
import pdb
from page import base

class Project(base.OkrTest):
	
	def test_create_project(self):
		self.login()
		self.create_project()
		project = self.find_element('css=#projectList > li:last-child').text
		try:
			self.assertEqual(project,'test_project')
		finally:
			self.delete_project()

	def test_rename_project(self):
		self.login()
		self.rename_project()
		project = self.find_element('css=#projectList > li:last-child').text
		try:
			self.assertEqual(project,'rename_project')
		finally:
			self.delete_project()


	# def test_rename_project(self):
	# 	self.rename_project()
	# 	self.delete_project()
	
if __name__ == "__main__":
	unittest.main()
