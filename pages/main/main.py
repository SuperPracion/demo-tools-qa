import settings
from pages.driver import Driver

from selenium.webdriver.common.by import By


class Main(Driver):
    def get_header_button(self):
        pass

    def header_button_click(self):
        pass

    def get_banner(self):
        pass

    def banner_click(self):
        pass

    def get_elements_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][1]')

    def elements_button_click(self):
        self.get_elements_button().click()
        # TODO добавить тесты

    def get_forms_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][2]')

    def forms_buttons_click(self):
        self.get_forms_button().click()
        # TODO добавить тесты

    def get_alerts_windows_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][3]')

    def alerts_windows_button_click(self):
        self.get_alerts_windows_button().click()
        # TODO добавить тесты

    def get_widgets_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][4]')

    def widgets_button_click(self):
        self.get_widgets_button().click()
        # TODO добавить тесты

    def get_integrations_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][5]')

    def integrations_button_click(self):
        self.get_integrations_button().click()
        # TODO добавить тесты

    def get_book_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][6]')

    def book_button_click(self):
        self.get_book_button().click()
        # TODO добавить тесты
