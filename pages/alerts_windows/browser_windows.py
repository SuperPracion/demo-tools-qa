from selenium.webdriver.common.by import By

from base.driver import Driver

class BrowserWindows(Driver):
    def get_new_tab_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='tabButton']")

    def get_new_window_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='tabButton']")

    def get_new_window_message_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='messageWindowButton']")