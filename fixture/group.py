from selenium.webdriver.common.by import By

from model.group import Group


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
        self.open_new_group_page()
        self.fill_group_form(group)
        # submit group creation
        self.app.wait_for_element(By.NAME, "submit").click()
        self.return_to_groups_page()


    def open_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len (wd.find_elements(By.NAME, "new")) > 0:
            return
        self.app.wait_for_element(By.LINK_TEXT, "groups").click()


    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        if not self.is_group_exist():
            self.open_new_group_page()
            self.create(Group(name="New group", header="New header"))
        self.app.wait_for_element(By.NAME, "selected[]").click()
        self.app.wait_for_element(By.NAME, "delete").click()
        self.return_to_groups_page()


    def edit_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        if not self.is_group_exist():
            self.open_new_group_page()
            self.create(group)
        self.app.wait_for_element(By.NAME, "selected[]").click()
        self.app.wait_for_element(By.NAME, "edit").click()
        self.fill_group_form(group)
        # submit group creation
        self.app.wait_for_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def open_new_group_page(self):
        self.app.wait_for_element(By.NAME, "new").click()

    def fill_group_form(self, group):
        group_name = self.app.wait_for_element(By.NAME, "group_name")
        group_name.click()
        group_name.send_keys(group.name)
        group_header = self.app.wait_for_element(By.NAME, "group_header")
        group_header.click()
        group_header.clear()
        group_header.send_keys(group.header)


    def is_group_exist(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, "selected[]")) > 0
