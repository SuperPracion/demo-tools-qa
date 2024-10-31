from base.driver import Driver

from selenium.webdriver.common.by import By


class DatePicker(Driver):
    def get_date_picker_month_year_input(self):
        return self.driver.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]')

    def get_date_and_time_picker_input(self):
        return self.driver.find_element(By.XPATH, '//*[@id="dateAndTimePickerInput"]')