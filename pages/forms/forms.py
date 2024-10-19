from base.driver import Driver
from selenium.webdriver.common.by import By
from settings import MAIN_URL

class Forms(Driver):
    def get_practice_form_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Practice Form')]/parent::*")

    def practice_form_button_click(self):
        self.get_practice_form_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/automation-practice-form'