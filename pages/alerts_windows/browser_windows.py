from selenium.webdriver.common.by import By

from base.driver import Driver
from settings import MAIN_URL


class BrowserWindows(Driver):
    def get_new_tab_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='tabButton']")

    def new_tab_button_click(self):
        self.get_new_tab_button().click()

        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) > 1

        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.find_element(By.XPATH, "//*[@id='sampleHeading']").text == 'This is a sample page'

        self.driver.switch_to.window(original_window)

    def get_new_window_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='tabButton']")

    def new_window_button_click(self):
        self.get_new_window_button().click()

        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) > 1

        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.find_element(By.XPATH, "//*[@id='sampleHeading']").text == 'This is a sample page'

        self.driver.switch_to.window(original_window)


    def get_new_window_message_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='messageWindowButton']")

    def new_window_message_button_click(self):
        self.get_new_window_message_button().click()

        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) > 1

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.switch_to.window(original_window)
