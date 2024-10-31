from selenium.webdriver.common.by import By

from base.driver import Driver


class Selectable(Driver):
    def get_demo_tab_list(self):
        return self.driver.find_element(By.XPATH, '//*[@id="demo-tab-list"]')

    def get_demo_tab_grid(self):
        return self.driver.find_element(By.XPATH, '//*[@id="demo-tab-grid"]')

    def get_group_item_by_text(self, text):
        return self.driver.find_element(By.XPATH, f'//*[contains(text(), "{text}")]')
