from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app


    def return_to_groups_page(self):
        wd = self.app.wd
        self.app.wait_for_element(By.LINK_TEXT, "group page").click()


    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        self.app.wait_for_element(By.NAME, "new").click()
        # fill group form
        group_name = self.app.wait_for_element(By.NAME, "group_name")
        group_name.click()
        group_name.send_keys(group.name)
        group_header = self.app.wait_for_element(By.NAME, "group_header")
        group_header.click()
        group_header.clear()
        group_header.send_keys(group.header)
        # submit group creation
        self.app.wait_for_element(By.NAME, "submit").click()
        self.return_to_groups_page()


    def open_group_page(self):
        wd = self.app.wd
        self.app.wait_for_element(By.LINK_TEXT, "groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.app.wait_for_element(By.NAME, "selected[]").click()
        self.app.wait_for_element(By.NAME, "delete").click()
        self.return_to_groups_page()
