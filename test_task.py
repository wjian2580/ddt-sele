# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestTask(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.202.202.94:28080"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_task(self):
        driver = self.driver
        driver.get(self.base_url + "/OKRS/")
        driver.find_element_by_id("btLogin").click()
        driver.find_element_by_xpath("//li[@onclick='changePro()']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | p_frame | ]]
        driver.find_element_by_xpath("//ul[@id='projectList']/li[6]").click()
        driver.find_element_by_css_selector("img.gotoTask").click()
        driver.find_element_by_css_selector("#proName > img").click()
        driver.find_element_by_css_selector("td.taskInto").click()
        driver.find_element_by_css_selector("span.tastPro > img.taskpng").click()
        driver.find_element_by_css_selector("li.opt_tast.stage_addPre").click()
        driver.find_element_by_css_selector("td.taskInto > div.box-card > div.el-card_body > input.addInp").clear()
        driver.find_element_by_css_selector("td.taskInto > div.box-card > div.el-card_body > input.addInp").send_keys("tongji")
        driver.find_element_by_css_selector("button.btn_tast").click()
        driver.find_element_by_css_selector("i.taskTxt").click()
        driver.find_element_by_css_selector("li.opt_tast.stage_addNext").click()
        driver.find_element_by_css_selector("td.taskInto > div.box-card > div.el-card_body > input.addInp").clear()
        driver.find_element_by_css_selector("td.taskInto > div.box-card > div.el-card_body > input.addInp").send_keys("xiaji")
        driver.find_element_by_css_selector("button.btn_tast").click()
        driver.find_element_by_css_selector("b.intoChilerenTask").click()
        driver.find_element_by_css_selector("i.taskTxt").click()
        driver.find_element_by_css_selector("li.opt_tast.stage_addNext").click()
        driver.find_element_by_css_selector("td.taskInto > div.box-card > div.el-card_body > input.addInp").clear()
        driver.find_element_by_css_selector("td.taskInto > div.box-card > div.el-card_body > input.addInp").send_keys("xiaji1")
        driver.find_element_by_css_selector("button.btn_tast").click()
        driver.find_element_by_css_selector("img.change").click()
        driver.find_element_by_css_selector("th.stage_th > div.box-card > div.el-card_body > input.addInp").clear()
        driver.find_element_by_css_selector("th.stage_th > div.box-card > div.el-card_body > input.addInp").send_keys("phase1")
        driver.find_element_by_css_selector("button.btn.stagename").click()
        driver.find_element_by_css_selector("span.stageTxt").click()
        driver.find_element_by_css_selector("li.opt.stage_addNext").click()
        driver.find_element_by_css_selector("th.stage_th > div.box-card > div.el-card_body > input.addInp").clear()
        driver.find_element_by_css_selector("th.stage_th > div.box-card > div.el-card_body > input.addInp").send_keys("phase2")
        driver.find_element_by_css_selector("th.stage_th > div.box-card > div.el-card_body > button.btn").click()
        driver.find_element_by_css_selector("span.stageTxt").click()
        driver.find_element_by_css_selector("li.opt.stage_addPre").click()
        driver.find_element_by_css_selector("th.stage_th > div.box-card > div.el-card_body > input.addInp").clear()
        driver.find_element_by_css_selector("th.stage_th > div.box-card > div.el-card_body > input.addInp").send_keys("0")
        driver.find_element_by_css_selector("th.stage_th > div.box-card > div.el-card_body > button.btn").click()
        driver.find_element_by_css_selector("div.td > span").click()
        driver.find_element_by_css_selector("input.name").clear()
        driver.find_element_by_css_selector("input.name").send_keys(u"王健")
        driver.find_element_by_css_selector("li.lis").click()
        driver.find_element_by_css_selector("div.detail").click()
        driver.find_element_by_css_selector("span.laydate-btns-now").click()
        driver.find_element_by_id("textarea").click()
        driver.find_element_by_id("textarea").clear()
        driver.find_element_by_id("textarea").send_keys("123")
        driver.find_element_by_css_selector("input.btn").click()
    
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
