from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(3)

    def wait_for_element(self, by, value, timeout=10):
        try:
            return WebDriverWait(self.wd, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            raise AssertionError(f"Element not found: {by}={value}")

    def logout(self):
        wd = self.wd
        self.wait_for_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        self.wait_for_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
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
        self.return_to_groups_page()

    def open_group_page(self):
        wd = self.wd
        self.wait_for_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        self.wait_for_element(By.NAME, "user").send_keys(username)
        self.wait_for_element(By.NAME, "pass").send_keys(password)
        self.wait_for_element(By.XPATH, "//input[@value='Login']").click()


    def create_contact(self, contact):
        wd = self.wd
        self.open_add_contact_page()
        # fill contact form
        self.wait_for_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.wait_for_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.wait_for_element(By.NAME, "company").send_keys(contact.company)
        self.wait_for_element(By.NAME, "home").send_keys(contact.home_phone)
        self.wait_for_element(By.NAME, "email").send_keys(contact.email)
        # submit contact creation
        self.wait_for_element(By.XPATH, "//div[@id='content']/form/input[20]").click()
        self.return_to_home_page()

    def open_add_contact_page(self):
        self.wait_for_element(By.LINK_TEXT, "add new").click()

    def return_to_home_page(self):
        self.wait_for_element(By.LINK_TEXT, "home page").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
