from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        # fill contact form
        self.app.wait_for_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.app.wait_for_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.app.wait_for_element(By.NAME, "company").send_keys(contact.company)
        self.app.wait_for_element(By.NAME, "home").send_keys(contact.home_phone)
        self.app.wait_for_element(By.NAME, "email").send_keys(contact.email)
        # submit contact creation
        self.app.wait_for_element(By.XPATH, "//div[@id='content']/form/input[20]").click()
        self.return_to_home_page()

    def open_add_contact_page(self):
        self.app.wait_for_element(By.LINK_TEXT, "add new").click()

    def return_to_home_page(self):
        self.app.wait_for_element(By.LINK_TEXT, "home page").click()
