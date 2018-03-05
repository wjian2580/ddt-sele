# -*- coding: utf-8 -*-
import time
from page.base import OkrTest
import pdb
import random
import unittest



class TestTask(OkrTest):
	''''''
	
	def test_task(self):
		driver = self.driver
		self.login(driver)
		time.sleep(2)
		self.create_project(driver)
		WebDriverWait(driver,5,0.5).until(EC.invisibility_of_element_located(By.CSS_SELECTOR,"img.gotoTask"))
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

if __name__ == "__main__":
	unittest.main()
