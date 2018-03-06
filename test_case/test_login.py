#coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time, re
from ddt import ddt,data,unpack,file_data
from page import base

@ddt
class TestLogin(base.OkrTest):

    @file_data('../data/login.yml')
    @unpack
    def test_login(self,username,password,expected):
        driver = self.driver
        driver.get(self.base_url+'OKRS')
        self.send_keys('id=tbUsername',username)
        self.send_keys('id=tbPassword',password)
        self.click('id=btLogin')
        try:
            #登陆成功，获取欢迎信息
            text = self.find_element('css=div.top_user > i').text
        except NoSuchElementException:
            #登陆失败，获取报错信息
            text = self.find_element('id=result').text
        self.assertEqual(text,expected)

if __name__ == "__main__":
    unittest.main()
