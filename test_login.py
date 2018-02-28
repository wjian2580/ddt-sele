# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from ddt import ddt,data,unpack,file_data

@ddt
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = "http://10.202.202.94:28080"
        self.verificationErrors = []
        self.accept_next_alert = True

    @file_data('login.yml')
    @unpack
    def test_login(self,username,password):
        driver = self.driver
        driver.get(self.base_url + "/OKRS/")
        user_name = driver.find_element_by_id("tbUsername")
        user_name.clear()
        user_name.send_keys(username)
        pass_word = driver.find_element_by_id("tbPassword")
        pass_word.clear()
        pass_word.send_keys(password)
        driver.find_element_by_id("btLogin").click()       
        self.assertTrue(self.is_element_present('xpath',"//i[contains(text(),'欢迎，冯思佳')]"))

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
