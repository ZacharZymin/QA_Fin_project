from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page.base_page import BasePage
from resources.settings import PageSettings


class RegistrationPage(BasePage, PageSettings):
    def __int__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def input_field_first_name_new_acc(self, firstname):
        self.wait_for(self.field_firstname).send_keys(firstname)

    def input_field_last_name_new_acc(self, lastname):
        self.wait_for(self.field_lastname).send_keys(lastname)

    def input_field_user_name_new_acc(self, email):
        self.wait_for(self.field_username).send_keys(email)

    def input_field_password_first(self, password):
        self.wait_for(self.field_first_password).send_keys(password)

    def input_field_password_last(self, password):
        self.wait_for(self.field_last_password).send_keys(password)
