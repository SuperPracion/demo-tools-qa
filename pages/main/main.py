import allure
from selenium.webdriver.common.by import By

import settings
from base.user import User
from base.driver import Driver


class Main(Driver):
    @allure.step('Open main page')
    def __init__(self, user: User, driver):
        super().__init__(driver)
        self.user = user
        self.driver.get(settings.MAIN_URL)

    def get_header_button(self):
        return self.driver.find_element(By.XPATH, '//*[@href="https://demoqa.com"]')

    # def header_button_click(self):
    #     self.get_header_button().click()
    #     assert self.driver.current_url == 'https://demoqa.com/'

    def get_banner(self):
        return self.driver.find_element(By.XPATH, '//*[@class="home-banner"]')

    # def banner_click(self):
    #     self.get_banner().click()
    #     assert self.driver.current_url == 'https://www.toolsqa.com/selenium-training/'

    def get_elements_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][1]')

    def get_forms_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][2]')

    def get_alerts_windows_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][3]')

    def get_widgets_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][4]')

    def get_interactions_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][5]')

    def get_books_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][6]')

    def get_footer(self):
        element = self.driver.find_element(By.XPATH, '//footer')
        assert element.text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
        return element
