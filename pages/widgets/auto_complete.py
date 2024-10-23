from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.driver import Driver


class AutoComplete(Driver):
    def get_auto_complete_multiple_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="autoCompleteMultipleInput"]')

    def auto_complete_multiple_write(self, value):
        field = self.get_auto_complete_multiple_field()
        field.click()
        field.send_keys(value)
        field.send_keys(Keys.ENTER)
        for i in range(10):
            try:
                if value in self.driver.find_element(By.XPATH, f'(//*[@class="css-12jo7m5 auto-complete__multi-value__label"])[{i}]').text:
                    break
            except:
                pass
        else:
            raise NoSuchElementException

    def get_auto_complete_single_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="autoCompleteSingleInput"]')

    def auto_complete_single_write(self, value):
        field = self.get_auto_complete_single_field()
        field.click()
        field.send_keys(value)
        field.send_keys(Keys.ENTER)
        field.send_keys(Keys.ENTER)
        assert value in self.driver.find_element(By.XPATH, '//*[@class="auto-complete__single-value css-1uccc91-singleValue"]').text