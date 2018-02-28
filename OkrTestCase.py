# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import pdb




class OkrTestCase(unittest.TestCase):

	@classmethod
	def setUp(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.implicitly_wait(5)
		cls.base_url = "http://10.202.202.94:28080/OKRS/"
		cls.verificationErrors = []
		cls.accept_next_alert = True


#测试登陆	
	def test_1(self):
		driver = self.driver
		driver.get(self.base_url)
		user_name = driver.find_element_by_id("tbUsername")
		user_name.clear()
		user_name.send_keys('fengsijia')
		password = driver.find_element_by_id("tbPassword")
		password.clear()
		password.send_keys('123456')
		driver.find_element_by_id("btLogin").click()
		
		self.is_element_present('xpath',"//i[contains(text(),'欢迎，冯思佳')]")

#进入看板并切换frame
	def test_2(self):
		driver=self.driver
		driver.find_element_by_xpath("//li[@onclick='changePro()']").click()	
		driver.switch_to.frame('p_frame')

#测试新增项目"test"
		lis = driver.find_elements_by_css_selector('#projectList >li')
		for li in lis:
			if li.text == 'test':
				li.click()
				driver.find_element_by_id('headName').click()
				driver.find_element_by_css_selector('#pro_opt > li.delete')
				driver.find_element_by_id('proCarConfirmBtn').click()
				break		
		driver.find_element_by_link_text(u'新增').click()
		driver.find_element_by_xpath("//input[@type='text']").send_keys("test")
		driver.find_element_by_id("addProjectBtn").click()

# 		driver.find_element_by_xpath("//table[@id='project_one']/tbody/tr/td/span/i").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys("test")
# 		driver.find_element_by_xpath("//table[@id='project_one']/tbody/tr/td/div/div/button").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[2]/span").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
# 		driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("1")
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[2]/div/div/button/span").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[2]/img").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[2]/ul/li[3]").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
# 		driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("0")
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[2]/div/div/button").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[3]/img").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[3]/ul/li[4]").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
# 		driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys("2")
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[3]/div/div/button/span").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/tbody/tr/td[2]/div/span").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[7]").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[7]").clear()
# 		driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys(u"王健")
# 		driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys(Keys.ENTER)
# 		driver.find_element_by_xpath("//div[5]/div[2]/div/ul/li").click()
# 		driver.find_element_by_xpath("//div[@id='layui-laydate1']/div/div[2]/table/tbody/tr[3]/td[7]").click()
# 		driver.find_element_by_id("textarea").click()
# 		driver.find_element_by_id("textarea").clear()
# 		driver.find_element_by_id("textarea").send_keys("nihao")
# 		driver.find_element_by_xpath(u"//input[@value='确认']").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/tbody/tr/td[2]/div/p").click()
# 		driver.find_element_by_xpath("//input[@type='checkbox']").click()
# 		driver.find_element_by_xpath(u"//input[@value='确认']").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/tbody/tr/td[3]/div/span").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[7]").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[7]").clear()
# 		driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys(u"王健")
# 		driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys(Keys.ENTER)
# 		driver.find_element_by_xpath("//div[5]/div[2]/div/ul/li").click()
# 		driver.find_element_by_xpath("//div[@id='layui-laydate3']/div/div[2]/table/tbody/tr[3]/td[5]").click()
# 		driver.find_element_by_id("textarea").click()
# 		driver.find_element_by_id("textarea").clear()
# 		driver.find_element_by_id("textarea").send_keys(u"呵呵")
# 		driver.find_element_by_xpath(u"//input[@value='确认']").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/tbody/tr/td[3]/div/p").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[7]").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[7]").clear()
# 		driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys(u"宋")
# 		driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys(Keys.ENTER)
# 		driver.find_element_by_xpath("//div[5]/div[2]/div/ul/li").click()
# 		driver.find_element_by_xpath("//div[5]/div[4]").click()
# 		driver.find_element_by_xpath("//b/img").click()
# 		driver.find_element_by_xpath(u"//input[@value='确认']").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/tbody/tr/td[2]/img").click()
# 		driver.find_element_by_xpath("//button[@id='delet_car_conf']/span").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[2]/img").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[2]/ul/li").click()
# 		driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
# 		driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("0.5")
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[2]/div/div/button").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[2]/img").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[4]/span").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[4]/ul/li[2]").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[4]/div/div/button").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[3]/img").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[3]/img").click()
# 		driver.find_element_by_xpath("//table[@id='project_one']/thead/tr/th[3]").click()
# 		driver.find_element_by_xpath("//div[@id='main']/div").click()
# 		driver.close()
	
	def is_element_present(self, how, what):
		try:
			if how == 'id':
				self.driver.find_element_by_id(what)
				return True
			elif how == 'xpath':
				self.driver.find_element_by_xpath(what)
				return True 	
			elif how == 'link_text':
				text = self.driver.find_element_by_link_text(what)
				return True 
			elif how == 'partial_link_text':
				self.driver.find_element_by_partial_link_text(what)
				return True 
		except NoSuchElementException:
			return False
	
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

	@classmethod
	def tearDown(cls):
		driver = cls.driver
		driver.quit()
	

if __name__ == "__main__":
	unittest.main()
