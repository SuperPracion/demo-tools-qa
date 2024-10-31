from selenium.webdriver.common.by import By

from base.driver import Driver


class AutoComplete(Driver):
    def get_auto_complete_multiple_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="autoCompleteMultipleInput"]')

    def get_auto_complete_single_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="autoCompleteSingleInput"]')
