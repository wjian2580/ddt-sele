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
    
    def test_project_1(self):
        driver = self.driver
        self.login(driver)
        #新增项目
        time.sleep(2)
        project_name = 'test' + str(random.randint(10,100))
        driver.find_element_by_link_text(u"新增").click()
        driver.find_element_by_css_selector("input.addInp").clear()
        driver.find_element_by_css_selector("input.addInp").send_keys(project_name)
        driver.find_element_by_id("addProjectBtn").click()
        #项目重命名
        driver.find_element_by_id("headName").click()
        driver.find_element_by_css_selector("li.rename").click()
        driver.find_element_by_id("proCarConfInput").clear()
        driver.find_element_by_id("proCarConfInput").send_keys("test4")
        driver.find_element_by_id("proCarConfirmBtn").click()
        #删除项目
        driver.find_element_by_id("headName").click()
        driver.find_element_by_css_selector("li.delete").click()
        driver.find_element_by_id("proCarConfirmBtn").click()
    
if __name__ == "__main__":
    unittest.main()
