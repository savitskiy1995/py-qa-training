from selenium.webdriver.common.by import By

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app


    contacts_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, "selected[]"))


    def create_contact(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        self.app.wait_for_element(By.XPATH, "//div[@id='content']/form/input[20]").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def fill_contact_form(self, contact):
        firstname_field = self.app.wait_for_element(By.NAME, "firstname")
        firstname_field.clear()
        if contact.firstname:
            firstname_field.send_keys(contact.firstname)

        lastname_field = self.app.wait_for_element(By.NAME, "lastname")
        lastname_field.clear()
        if contact.lastname:
            lastname_field.send_keys(contact.lastname)

        company_field = self.app.wait_for_element(By.NAME, "company")
        company_field.clear()
        if contact.company:
            company_field.send_keys(contact.company)

        home_phone_field = self.app.wait_for_element(By.NAME, "home")
        home_phone_field.clear()
        if contact.home_phone:
            home_phone_field.send_keys(contact.home_phone)

        email_field = self.app.wait_for_element(By.NAME, "email")
        email_field.clear()
        if contact.email:
            email_field.send_keys(contact.email)


    def open_add_contact_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/edit.php") and len (wd.find_elements(By.NAME, "Enter")) > 0:
            return
        self.app.wait_for_element(By.LINK_TEXT, "add new").click()


    def return_to_home_page(self):
        self.app.wait_for_element(By.LINK_TEXT, "home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        if not self.is_contact_exist():
            self.open_add_contact_page()
            self.create_contact(Contact(
                firstname="John",
                lastname="Smith",
                company="Google",
                home_phone="+7999999999",
                email="johnsmith@gmail.com"
            ))
        self.select_contact_by_index(index)
        self.app.wait_for_element(By.XPATH, "//input[@value='Delete']").click()
        self.contacts_cache = None


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.XPATH, "//img[@title='Edit']")[index].click()


    def edit_first_contact(self, contact):
        wd = self.app.wd
        wd.edit_contact_by_index(contact, 0)


    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        if not self.is_contact_exist():
            self.open_add_contact_page()
            self.create_contact(contact)
        self.select_contact_by_index(index)
        self.fill_contact_form(contact)
        self.app.wait_for_element(By.XPATH, "//input[@value='Update']").click()
        self.contacts_cache = None
        self.return_to_home_page()


    def is_contact_exist(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, "selected[]")) > 0

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.contacts_cache = []
            self.app.wait_for_element(By.NAME, "entry")
            for element in wd.find_elements(By.NAME, "entry"):
                cells = element.find_elements(By.TAG_NAME, "td")
                id = element.find_element(By.TAG_NAME, "input").get_attribute("value")
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                email = cells[4].text
                phone = cells[5].text
                self.contacts_cache.append(Contact(id=id, firstname=first_name, lastname=last_name,
                                                  address=address, email=email,
                                                  home_phone=phone))
        return list(self.contacts_cache)
