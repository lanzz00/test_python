# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test0930(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.26.162.200:7084/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_0930(self):
        driver = self.driver
        driver.get(self.base_url + "/admin")
        driver.find_element_by_link_text(u"发布信息").click()
        driver.find_element_by_link_text(u"教育动态").click()
        driver.find_element_by_link_text(u"新增教育动态").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"test-教育动态-标题1")
        driver.find_element_by_name("author").clear()
        driver.find_element_by_name("author").send_keys(u"作者作者作者作者作者作者")
        driver.find_element_by_name("author").clear()
        driver.find_element_by_name("author").send_keys(u"作者作者作者作者作者")
        driver.find_element_by_name("description").clear()
        driver.find_element_by_name("description").send_keys(u"test-教育动态-描述")
        driver.find_element_by_id("btn-submit").click()
        driver.find_element_by_id("fileupload").clear()
        driver.find_element_by_id("fileupload").send_keys("C:\\Users\\Administrator\\Desktop\\feiyue\\yoona1.jpg")
        driver.find_element_by_id("btn-submit").click()
        driver.find_element_by_xpath("//div[@id='alertModal']/div/div/div[2]/h4").click()
    
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
