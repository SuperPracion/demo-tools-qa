from base.driver import Driver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class DatePicker(Driver):
    def get_date_picker_month_year_input(self):
        return self.driver.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]')

    def set_date_picker_mont_year(self, day, month='', year=''):
        field = self.get_date_picker_month_year_input()
        field.click()
        field.send_keys(Keys.CONTROL + 'A')
        field.send_keys(Keys.BACKSPACE)
        field.send_keys('/'.join([day, month, year]))
        field.send_keys(Keys.ENTER)

    def get_date_and_time_picker_input(self):
        return self.driver.find_element(By.XPATH, '//*[@id="dateAndTimePickerInput"]')

    def set_date_and_time_picker(self, day, month='', year='', hour='', minute=''):
        field = self.get_date_and_time_picker_input()
        field.click()
        field.send_keys(Keys.CONTROL + 'A')
        field.send_keys(Keys.BACKSPACE)
        field.send_keys('/'.join([day, month, year]) + ':'.join([hour, minute]))
        field.send_keys(Keys.ENTER)