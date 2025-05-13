# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(3)

    def wait_for_element(self, by, value, timeout=10):
        try:
            return WebDriverWait(self.wd, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            raise AssertionError(f"Element not found: {by}={value}")

    def test_add_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

        self.wait_for_element(By.NAME, "user").send_keys("admin")
        self.wait_for_element(By.NAME, "pass").send_keys("secret")
        self.wait_for_element(By.XPATH, "//input[@value='Login']").click()
        self.wait_for_element(By.LINK_TEXT, "groups").click()
        self.wait_for_element(By.NAME, "new").click()
        group_name = self.wait_for_element(By.NAME, "group_name")
        group_name.click()
        group_name.clear()
        group_name.send_keys("new_group")
        group_header = self.wait_for_element(By.NAME, "group_header")
        group_header.click()
        group_header.clear()
        group_header.send_keys("logo")
        self.wait_for_element(By.NAME, "submit").click()
        self.wait_for_element(By.LINK_TEXT, "group page").click()
        self.wait_for_element(By.LINK_TEXT, "Logout").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
            return True
        except NoSuchElementException:
            return False

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
            return True
        except NoAlertPresentException:
            return False

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()