from selenium.webdriver.common.by import By

from base.driver import Driver
from settings import MAIN_URL


class Books(Driver):
    def get_login_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Login')]/parent::*")

    def login_button_click(self):
        self.get_login_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/login'

    def get_books_button(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Book Store']/parent::*")

    def books_button_click(self):
        self.get_books_button().click()
        assert self.driver.current_url == f'{MAIN_URL}//books'

    def get_profile_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Profile')]/parent::*")

    def profile_button_click(self):
        self.get_profile_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/profile'

    def get_book_store_api_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Book Store API')]/parent::*")

    def book_store_api_button_click(self):
        self.get_book_store_api_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/swagger/'