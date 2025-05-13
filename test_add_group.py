# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group

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
        self.open_home_page(wd)
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_group(Group(name="new_group", header="logo"))
        self.return_to_groups_page()
        self.logout()

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_group(Group(name="", header=""))
        self.return_to_groups_page()
        self.logout()

    def logout(self):
        self.wait_for_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self):
        self.wait_for_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        # init group creation
        self.wait_for_element(By.NAME, "new").click()
        # fill group form
        group_name = self.wait_for_element(By.NAME, "group_name")
        group_name.click()
        group_name.send_keys(group.name)
        group_header = self.wait_for_element(By.NAME, "group_header")
        group_header.click()
        group_header.clear()
        group_header.send_keys(group.header)
        # submit group creation
        self.wait_for_element(By.NAME, "submit").click()

    def open_group_page(self):
        self.wait_for_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        self.wait_for_element(By.NAME, "user").send_keys(username)
        self.wait_for_element(By.NAME, "pass").send_keys(password)
        self.wait_for_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

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