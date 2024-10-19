from selenium.webdriver.common.by import By

from base.driver import Driver
from settings import MAIN_URL


class AlertsWindows(Driver):
    def get_browser_windows_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Browser Windows')]/parent::*")

    def browser_windows_button_click(self):
        self.get_browser_windows_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/browser-windows'

    def get_alerts_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Alerts')]/parent::li")

    def alerts_button_click(self):
        self.get_alerts_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/alerts'

    def get_frames_button(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Frames']/parent::*")

    def frames_button_click(self):
        self.get_frames_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/frames'

    def get_nested_frames_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Nested Frames')]/parent::*")

    def nested_frames_click(self):
        self.get_nested_frames_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/nestedframes'

    def get_modal_dialogs_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Modal Dialogs')]/parent::li")

    def modal_dialogs_button_click(self):
        self.get_modal_dialogs_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/modal-dialogs'