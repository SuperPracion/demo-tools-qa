from selenium.webdriver.common.by import By

from settings import MAIN_URL
from base.driver import Driver


class Interaction(Driver):
    def get_sortable_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Sortable')]/parent::*")

    def sortable_button_click(self):
        self.get_sortable_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/sortable'

    def get_selectable_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Selectable')]/parent::*")

    def selectable_button_click(self):
        self.get_selectable_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/selectable'

    def get_resizable_button(self):
        return self.driver.find_element(By.XPATH, "Resizable")

    def resizable_button_click(self):
        self.get_resizable_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/resizable'

    def get_droppable_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Droppable')]/parent::*")

    def droppable_button_click(self):
        self.get_droppable_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/droppable'

    def get_dragabble_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Dragabble')]/parent::li")

    def dragabble_button_click(self):
        self.get_dragabble_button().click()
        assert self.driver.current_url == f'{MAIN_URL}/dragabble'
