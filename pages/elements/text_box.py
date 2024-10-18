from base.driver import Driver
from selenium.webdriver.common.by import By


class TestBox(Driver):
    def get_full_name_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="userName"]')

    def input_full_name(self, value):
        self.get_full_name_field().send_keys(value)
        assert self.get_full_name_field().get_attribute('value') == value

    def get_email_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="userEmail"]')

    def input_email(self, value):
        self.get_email_field().send_keys(value)
        assert self.get_email_field().get_attribute('value') == value

    def get_current_address_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="currentAddress"]')

    def input_current_address(self, value):
        self.get_current_address_field().send_keys(value)
        assert self.get_current_address_field().get_attribute('value') == value

    def get_permanent_address_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="permanentAddress"]')

    def input_permanent_address(self, value):
        self.get_permanent_address_field().send_keys(value)
        assert self.get_permanent_address_field().get_attribute('value') == value

    def get_submit_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="submit"]')

    def submit_button_click(self):
        self.get_submit_button().click()

    def get_output_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="output"]')

    def output_field_check_values(self, name=None, email=None, current_address=None, permanent_address=None):
        output_field = self.get_output_field()
        if name:
            assert output_field.find_element(By.XPATH, '//*[@id="name"]').text == f'Name:{name}'
        if email:
            assert output_field.find_element(By.XPATH, '//*[@id="email"]').text == f'Email:{email}'
        if current_address:
            assert output_field.find_element(By.XPATH, '//p[@id="currentAddress"]').text == f'Current Address :{current_address}'
        if permanent_address:
            assert output_field.find_element(By.XPATH, '//p[@id="permanentAddress"]').text == f'Permananet Address :{permanent_address}'