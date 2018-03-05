# -*- coding: utf-8 -*-
import unittest
from ddt import ddt,data,unpack,file_data
import base
from page import login

@ddt
class TestLogin(login.TestLogin):

    @file_data('login.yml')
    @unpack
    def test_login(self,username,password):
        driver = self.driver
        userName_loc = driver.find_element(*self.userName_loc)
        userName_loc.clear()
        userName_loc.send_keys(username)
        password_loc = driver.find_element(*self.password_loc)
        password_loc.clear()
        password_loc.send_keys(password)
        driver.find_element(*self.loginButton_loc).click()       
        self.assertTrue(self.is_element_present('xpath',"//i[text()='欢迎，冯思佳']"))
    
if __name__ == "__main__":
    unittest.main()
