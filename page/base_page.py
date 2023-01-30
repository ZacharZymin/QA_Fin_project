from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from resources.locators import PageLocators
from resources.settings import PageSettings


class BasePage(PageLocators, PageSettings):
    """The BasePage class holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    """

    def __init__(self, driver):
        """ This function is called every time a new object of the base class is created"""
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def wait_for(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def input_field_login(self, email):
        self.wait_for(self.field_email).send_keys(email)

    def input_field_password(self, password):
        self.wait_for(self.login_password_field).send_keys(password)

    def click_btn_login(self):
        self.find(self.button_login).click()

    def click_btn_change_acc(self):
        self.find(self.button_change_account).click()

    def click_btn_further(self):
        self.find(self.button_further).click()

    def click_btn_for_work(self):
        self.find(self.button_forwork).click()

    def click_btn_create_account(self):
        self.find(self.button_create_account).click()

    def click_btn_logo(self):
        self.find(self.button_logo).click()
