from base.driver import Driver
from selenium.webdriver.common.by import By

class TestBox(Driver):
    def get_full_name_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="userName"]')

    def input_full_name(self, value):
        self.get_full_name_field().send_keys(value)

    def get_email_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="userEmail"]')

    def input_email(self, value):
        self.get_email_field().send_keys(value)

    def get_current_address_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="currentAddress"]')

    def input_current_address(self, value):
        self.get_current_address_field().send_keys(value)

    def get_permanent_address_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="permanentAddress"]')

    def input_permanent_address(self, value):
        self.get_permanent_address_field().send_keys(value)

    def get_submit_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="submit"]')

    def submit_button_click(self):
        self.get_submit_button().click()