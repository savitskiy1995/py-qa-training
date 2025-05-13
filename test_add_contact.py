# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact

class TestAddContact(unittest.TestCase):
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

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(username="admin", password="secret")
        self.open_add_contact_page()
        self.fill_contact_form(Contact(
            firstname="John",
            lastname="Smith",
            company="Google",
            home_phone="+7999999999",
            email="johnsmith@gmail.com"
        ))
        self.submit_contact_creation()
        self.return_to_home_page()
        self.logout()

    def logout(self):
        self.wait_for_element(By.LINK_TEXT, "Logout").click()

    def return_to_home_page(self):
        self.wait_for_element(By.LINK_TEXT, "home page").click()

    def submit_contact_creation(self):
        self.wait_for_element(By.XPATH, "//div[@id='content']/form/input[20]").click()

    def fill_contact_form(self, contact):
        self.wait_for_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.wait_for_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.wait_for_element(By.NAME, "company").send_keys(contact.company)
        self.wait_for_element(By.NAME, "home").send_keys(contact.home_phone)
        self.wait_for_element(By.NAME, "email").send_keys(contact.email)

    def open_add_contact_page(self):
        self.wait_for_element(By.LINK_TEXT, "add new").click()

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