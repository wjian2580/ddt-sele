#coding: utf-8
import unittest
from page import base
from selenium import webdriver
from ddt import ddt,data,unpack,file_data
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import pdb

@ddt
class TestLogin(base.OkrTest):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.base_url = "http://okrs.top/OKRS/"
        self.driver.get(self.base_url)  
    
    # @unittest.skip('reason')          
    @file_data('../../data/login.yml')
    @unpack
    def test_login(self,username,password,expected):
        self.send_keys('id=tbUsername',username)
        self.send_keys('id=tbPassword',password)
        self.click('id=btLogin')
        try:
            #登陆成功，获取欢迎信息
            text = self.get_text('css=div.top_user > i')
        except TimeoutException:
            #登陆失败，获取报错信息
            text = self.get_text('id=result')
        self.assertEqual(text,expected)
        
    # @unittest.skip('reason')
    def test_logout(self):
        self.login()
        self.driver.switch_to.default_content()
        self.move_to_element('css=div.top_user')
        self.click('text=登出')
        self.assertEqual(self.driver.current_url,self.base_url)

if __name__ == "__main__":
    unittest.main()
