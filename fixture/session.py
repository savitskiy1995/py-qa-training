from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        self.app.wait_for_element(By.NAME, "user").send_keys(username)
        self.app.wait_for_element(By.NAME, "pass").send_keys(password)
        self.app.wait_for_element(By.XPATH, "//input[@value='Login']").click()


    def logout(self):
        wd = self.app.wd
        self.app.wait_for_element(By.LINK_TEXT, "Logout").click()