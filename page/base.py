# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re
import random
import pdb


class OkrTest(unittest.TestCase):
	''''''

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(5)
		self.base_url = "http://10.202.202.94:28080/OKRS"
		self.driver.get(self.base_url)

	def login(self):
		self.driver.get(self.base_url)
		self.send_keys('id=tbUsername','fengsijia')
		self.send_keys('id=tbPassword','123456')
		self.click('id=btLogin')   
		self.click("xpath=//li[@onclick='changePro()']")   
		self.driver.switch_to.frame('p_frame')
		time.sleep(2)

	def create_project(self,project_name='testing'):
		self.click('text=新增')
		self.send_keys('css=input.addInp',project_name)
		self.click('id=addProjectBtn')
		time.sleep(2)

	def delete_project(self):
		self.click('css=#projectList > li:last-child')
		self.click('id=headName')
		self.click('css=li.delete')
		self.click('id=proCarConfirmBtn')
		time.sleep(2)

	def rename_project(self,project_name):
		self.click('css=#projectList > li:last-child')
		self.click('id=headName')
		self.click('css=li.rename')
		self.send_keys('id=proCarConfInput',project_name)
		self.click('id=proCarConfirmBtn')
		time.sleep(2)


	def find_element(self,element):

		if "=" not in element:
			raise NameError("SyntaxError: invalid syntax, lack of '='.")

		by = element.split("=")[0]
		value = element.split("=",1)[1]

		if by == "id":
			return self.driver.find_element_by_id(value)
		elif by == "name":
			return self.driver.find_element_by_name(value)
		elif by == "class":
			return self.driver.find_element_by_class_name(value)
		elif by == "text":
			return self.driver.find_element_by_link_text(value)
		elif by == "text_part":
			return self.driver.find_element_by_partial_link_text(value)
		elif by == "xpath":
			return self.driver.find_element_by_xpath(value)
		elif by == "css":
			return self.driver.find_element_by_css_selector(value)
		else:
			raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")

	def send_keys(self, element, text):
		self.wait_element(element)
		self.find_element(element).clear()
		self.find_element(element).send_keys(text)

	def click(self, element):
		self.wait_element(element)
		self.find_element(element).click()


	def wait_element(self, element, seconds=5):

		if "=" not in element:
			raise NameError("SyntaxError: invalid syntax, lack of '='.")

		by = element.split("=")[0]
		value = element.split("=",1)[1]

		if by == "id":
			WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.ID, value)))
		elif by == "name":
			WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.NAME, value)))
		elif by == "class":
			WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
		elif by == "text":
			WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
		elif by == "xpath":
			WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.XPATH, value)))
		elif by == "css":
			WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
		else:
			raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")
		
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