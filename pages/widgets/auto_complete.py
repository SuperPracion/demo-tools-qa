from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.driver import Driver


class AutoComplete(Driver):
    def get_auto_complete_multiple_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]')

    def auto_complete_multiple_write(self, value):
        field = self.get_auto_complete_single_field()
        field.send_keys(value)
        field.send_keys(Keys.ENTER)

    def get_auto_complete_single_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="autoCompleteSingleContainer"]')

    def auto_complete_single_write(self, value):
        field = self.get_auto_complete_multiple_field()
        field.send_keys(value)
        field.send_keys(Keys.ENTER)