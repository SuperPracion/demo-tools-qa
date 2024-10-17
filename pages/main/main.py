from base.user import User
from base.driver import Driver

from selenium.webdriver.common.by import By


class Main(Driver):
    def __init__(self, user: User, driver):
        super().__init__(driver)
        self.user = user

    def get_header_button(self):
        return self.driver.find_element(By.XPATH, '//*[@href="https://demoqa.com"]')


    def header_button_click(self):
        self.get_header_button().click()
        assert self.driver.current_url == 'https://demoqa.com/'


    def get_banner(self):
        return self.driver.find_element(By.XPATH, '//*[@class="home-banner"]')


    def banner_click(self):
        self.get_banner().click()
        assert self.driver.current_url == 'https://www.toolsqa.com/selenium-training/'


    def get_elements_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][1]')


    def elements_button_click(self):
        self.get_elements_button().click()
        assert self.driver.current_url == 'https://demoqa.com/elements'


    def get_forms_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][2]')


    def forms_buttons_click(self):
        self.get_forms_button().click()
        assert self.driver.current_url == 'https://demoqa.com/forms'


    def get_alerts_windows_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][3]')


    def alerts_windows_button_click(self):
        self.get_alerts_windows_button().click()
        assert self.driver.current_url == 'https://demoqa.com/alertsWindows'


    def get_widgets_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][4]')


    def widgets_button_click(self):
        self.get_widgets_button().click()
        assert self.driver.current_url == 'https://demoqa.com/widgets'


    def get_interaction_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][5]')


    def interaction_button_click(self):
        self.get_interaction_button().click()
        assert self.driver.current_url == 'https://demoqa.com/interaction'


    def get_book_button(self):
        return self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][6]')


    def book_button_click(self):
        self.get_book_button().click()
        assert self.driver.current_url == 'https://demoqa.com/books'