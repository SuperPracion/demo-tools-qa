from selenium.webdriver.common.by import By

from settings import MAIN_URL
from base.driver import Driver


class Widgets(Driver):
    def get_accordian_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Accordian')]/parent::*")

    def accordian_button_click(self):
        self.get_accordian_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/accordian'

    def get_auto_complete_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Auto Complete')]/parent::*")

    def auto_complete_button_click(self):
        self.get_auto_complete_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/auto-complete'

    def get_date_picker_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Date Picker')]/parent::*")

    def date_picker_button_click(self):
        self.get_date_picker_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/date-picker'

    def get_slider_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Slider')]/parent::*")

    def slider_button_click(self):
        self.get_slider_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/slider'

    def get_process_bar_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Progress Bar')]/parent::*")

    def process_dar_button_click(self):
        self.get_process_bar_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/progress-bar'

    def get_tabs_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Tabs')]/parent::*")

    def tabs_button_click(self):
        self.get_tabs_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/tabs'

    def get_tools_tips_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Tool Tips')]/parent::*")

    def tools_tips_button_click(self):
        self.get_tools_tips_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/tool-tips'

    def get_menu_button(self):
        return self.driver.find_element(By.XPATH, "(//*[contains(text(), 'Menu')]/parent::li)[1]")

    def menu_button_click(self):
        self.get_menu_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/menu'

    def get_select_menu_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Select Menu')]/parent::li")

    def select_menu_click(self):
        self.get_select_menu_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/select-menu'