# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestLogin(unittest.TestCase):
	def setUp(self):
		self.userName_loc = (By.ID,'tbUsername')
		self.password_loc = (By.ID,'tbPassword')
		self.loginButton_loc = (By.ID,'btLogin')

		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(5)
		self.base_url = "http://10.202.202.94:28080"
		self.driver.get(self.base_url + "/OKRS/")


	def tearDown(self):
		self.driver.quit()

	def is_element_present(self, how, what):
	    try: self.driver.find_element(by=how, value=what)
	    except NoSuchElementException as e: return False
	    return True
	
	def is_alert_present(self):
	    try: self.driver.switch_to_alert()
	    except NoAlertPresentException as e: return False
	    return True
	
	def close_alert_and_get_its_text(self):
	    try:
	        alert = self.driver.switch_to_alert()
	        alert_text = alert.text
	        if self.accept_next_alert:
	            alert.accept()
	        else:
	            alert.dismiss()
	        return alert_text
	    finally: self.accept_next_alert = True
