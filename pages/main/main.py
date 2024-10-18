import settings
from base.user import User
from base.driver import Driver

from selenium.webdriver.common.by import By


class Main(Driver):
    def __init__(self, user: User, driver):
        super().__init__(driver)
        self.user = user
        self.driver.get(settings.MAIN_URL)

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
        button = self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][1]')
        assert button.text == 'Elements'
        return button

    def elements_button_click(self):
        self.get_elements_button().click()
        assert self.driver.current_url == 'https://demoqa.com/elements'

    def get_forms_button(self):
        button = self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][2]')
        assert button.text == 'Forms'
        return button

    def forms_buttons_click(self):
        self.get_forms_button().click()
        assert self.driver.current_url == 'https://demoqa.com/forms'

    def get_alerts_windows_button(self):
        button = self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][3]')
        assert button.text == 'Alerts, Frame & Windows'
        return button

    def alerts_windows_button_click(self):
        self.get_alerts_windows_button().click()
        assert self.driver.current_url == 'https://demoqa.com/alertsWindows'

    def get_widgets_button(self):
        button = self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][4]')
        assert button.text == 'Widgets'
        return button

    def widgets_button_click(self):
        self.get_widgets_button().click()
        assert self.driver.current_url == 'https://demoqa.com/widgets'

    def get_interaction_button(self):
        button = self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][5]')
        assert button.text == 'Interactions'
        return button

    def interaction_button_click(self):
        self.get_interaction_button().click()
        assert self.driver.current_url == 'https://demoqa.com/interaction'

    def get_books_button(self):
        button = self.driver.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][6]')
        assert button.text == 'Book Store Application'
        return button

    def books_button_click(self):
        self.get_books_button().click()
        assert self.driver.current_url == 'https://demoqa.com/books'

    def get_footer(self):
        element = self.driver.find_element(By.XPATH, '//footer')
        assert element.text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
        return element