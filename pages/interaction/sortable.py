from selenium.webdriver.common.by import By

from base.driver import Driver

class Sortable(Driver):
    def get_sortable_list(self):
        return self.driver.find_element(By.XPATH, '//*[@id="demo-tab-list"]')

    def click_sortable_list(self):
        self.get_sortable_list().click()

    def get_vertical_list_container(self):
        return self.driver.find_element(By.XPATH, 'class="vertical-list-container mt-4"')

    def get_sortable_grid(self):
        return self.driver.find_element(By.XPATH, '//*[@id="demo-tab-grid"]')

    def click_sortable_grid(self):
        self.get_sortable_grid().click()

    def get_create_grid(self):
        return self.driver.find_element(By.XPATH, '//*[@class="create-grid"]')

    def get_element_by_text_in_list(self, text):
        self.get_sortable_list().find_element(By.XPATH, f'//*[contains(text(), "{text}")]')

    def get_element_by_text_in_grid(self, text):
        self.get_sortable_grid().find_element(By.XPATH, f'//*[contains(text(), "{text}")]')