from selenium.webdriver.common.by import By

from base.driver import Driver


class Selectable(Driver):
    def get_demo_tab_list(self):
        return self.driver.find_element(By.XPATH, '//*[@id="demo-tab-list"]')

    def demo_tab_list_click(self):
        self.get_demo_tab_list().click()

    def get_demo_tab_grid(self):
        return self.driver.find_element(By.XPATH, '//*[@id="demo-tab-grid"]')

    def demo_tab_grid_click(self):
        self.get_demo_tab_grid().click()

    def get_group_item_by_text(self, text):
        self.driver.find_element(By.XPATH, f'//*[contains(text(), "{text}")]')
