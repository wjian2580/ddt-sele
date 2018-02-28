# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random

class Project(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.202.202.94:28080"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_project(self):
        driver = self.driver
        driver.get(self.base_url + "/OKRS/")
        user_name = driver.find_element_by_id("tbUsername")
        user_name.clear()
        user_name.send_keys('fengsijia')
        password = driver.find_element_by_id("tbPassword")
        password.clear()
        password.send_keys('123456')
        driver.find_element_by_id("btLogin").click()     
        driver.find_element_by_xpath("//li[@onclick='changePro()']").click()  
        driver.switch_to.frame('p_frame')

        project_name = 'test' + str(random.randint(10,100))
        driver.find_element_by_link_text(u"新增").click()
        driver.find_element_by_css_selector("input.addInp").clear()
        driver.find_element_by_css_selector("input.addInp").send_keys(project_name)
        driver.find_element_by_id("addProjectBtn").click()
        driver.find_element_by_id("headName").click()
        driver.find_element_by_css_selector("li.rename").click()
        driver.find_element_by_id("proCarConfInput").clear()
        driver.find_element_by_id("proCarConfInput").send_keys("test4")
        driver.find_element_by_id("proCarConfirmBtn").click()
        driver.find_element_by_id("headName").click()
        driver.find_element_by_css_selector("li.delete").click()
        driver.find_element_by_id("proCarConfirmBtn").click()

        #收藏和取消收藏
        sc
    
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
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
