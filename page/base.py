# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
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
#		self.driver = webdriver.Chrome()
		self.driver = webdriver.PhantomJS()
		self.driver.implicitly_wait(5)
		self.driver.set_window_size(1124,500)
		self.base_url = "http://okrs.top/OKRS/"
		self.driver.get(self.base_url)

	def login(self):
		self.driver.get(self.base_url)
		self.send_keys('id=tbUsername','fengsijia')
		self.send_keys('id=tbPassword','123456')
		self.click('id=btLogin')   
		self.sleep()
		self.driver.find_element_by_xpath("//li[@onclick='changePro()']").click()
		self.driver.switch_to.frame('p_frame')
		self.sleep(3)

	def create_project(self,project_name='testing'):
		projects = self.driver.find_elements_by_css_selector('#projectList > li')
		for project in projects:
			if project.text == project_name:
				project.click()
				self.delete_project()
				break;
		self.click('text=新增')
		self.send_keys('css=input.addInp',project_name)
		self.click('id=addProjectBtn')
		self.sleep()

	def delete_project(self):
		self.click('id=headName')
		self.click('css=li.delete')
		self.click('id=proCarConfirmBtn')
		self.sleep()

	def rename_project(self,project_name):
		self.click('css=#projectList > li:last-child')
		self.click('id=headName')
		self.click('css=li.rename')
		self.send_keys('id=proCarConfInput',project_name)
		self.click('id=proCarConfirmBtn')
		self.sleep()

	def create_task(self,task_name='test_task'):
		self.click('css=i.taskTxt')
		self.send_keys('css=td.taskInto > div > div > input',task_name)
		self.click('css=button.btn_tast')
		self.sleep()

	def create_stage(self,stage_name='stage'):
		self.click('css=span.stageTxt')
		self.send_keys('css=th.stage_th > div > div > input',stage_name)
		self.click('css=button.btn.stagename')
		self.sleep()

	def create_leader(self,leader_name='王健'):
		self.click('css=img.change')
		element=self.driver.find_element_by_css_selector('input.name')
		element.send_keys(leader_name)
		element.send_keys(Keys.ENTER)
		self.click('css=li.lis')
		self.click('css=input.date')
		self.click('css=span.laydate-btns-now')
		self.click('css=input.btn')

	def logout(self):
		self.driver.switch_to.default_content()
		self.move_to_element('css=div.top_user')
		self.click('text=登出')

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
		self.click(element)
		self.find_element(element).clear()
		self.find_element(element).send_keys(text)

	def click(self, element):
		self.wait_element(element)
		self.find_element(element).click()

	def submit(self, element):
	    self.wait_element(element)
	    self.find_element(element).submit()

	def switch_to_frame(self, element):

	    self.wait_element(element)
	    self.driver.switch_to.frame(self.find_element(element))

	def get_attribute(self, element, attribute):
	    self.wait_element(element)
	    return self.find_element(element).get_attribute(attribute)

	def get_text(self, element):
	    self.wait_element(element)
	    return self.find_element(element).text

	def get_display(self, element):
	    self.wait_element(element)
	    return self.find_element(element).is_displayed()

	def right_click(self, element):
	    self.wait_element(element)
	    ActionChains(self.driver).context_click(self.find_element(element)).perform()

	def move_to_element(self, element):
	    self.wait_element(element)
	    ActionChains(self.driver).move_to_element(self.find_element(element)).perform()

	def double_click(self, element):
	    self.wait_element(element)
	    ActionChains(self.driver).double_click(self.find_element(element)).perform()

	def drag_and_drop(self, source_element, target_element):
	    self.wait_element(source_element)
	    self.wait_element(target_element)
	    ActionChains(self.driver).drag_and_drop(self.find_element(source_element), self.find_element(target_element)).perform()

	def sleep(self,times=1):
		time.sleep(times)

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

	def retry_element(self,locator):
		for _ in range(3):
			try:
				element = self.find_element(locator)
				return element
			except StaleElementReferenceException:
				self.sleep()
			except NoSuchElementException:
				self.sleep()
			except ElementNotVisibleException:
				self.sleep()

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
