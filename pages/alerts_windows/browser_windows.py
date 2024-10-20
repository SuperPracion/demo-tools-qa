from selenium.webdriver.common.by import By

from base.driver import Driver
from settings import MAIN_URL


class BrowserWindows(Driver):
    def get_new_tab_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='tabButton']")

    def new_tab_button_click(self):
        self.get_new_tab_button().click()
        pass

    def get_new_window_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='tabButton']")

    def new_window_button_click(self):
        self.get_new_window_button().click()
        pass

    def get_new_window_message_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='messageWindowButton']")

    def new_window_message_button_click(self):
        self.get_new_window_message_button().click()
        pass