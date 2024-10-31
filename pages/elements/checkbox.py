from anyio.abc import value

from base.driver import Driver

from selenium.webdriver.common.by import By


class CheckBox(Driver):
    def get_expand_all_button(self):
        return self.driver.find_element(By.XPATH, '//*[@aria-label="Expand all"]')

    def get_collapse_all_button(self):
        return self.driver.find_element(By.XPATH, '//*[@aria-label="Collapse all"]')

    def get_home_toggle(self):
        return self.driver.find_element(By.XPATH, '(//*[@title="Toggle"])[1]')

    def get_home_checkbox(self):
        return self.driver.find_element(By.XPATH, '//*[@for="tree-node-home"]/*[@class="rct-checkbox"]')

    def get_desktop_toggle(self):
        return self.driver.find_element(By.XPATH, '(//*[@title="Toggle"])[2]')

    def get_desktop_checkbox(self):
        return self.driver.find_element(By.XPATH, '//*[@for="tree-node-desktop"]/*[@class="rct-checkbox"]')

    def get_documents_toggle(self):
        return self.driver.find_element(By.XPATH, '(//*[@title="Toggle"])[3]')

    def get_documents_checkbox(self):
        return self.driver.find_element(By.XPATH, '//*[@for="tree-node-documents"]/*[@class="rct-checkbox"]')

    def get_downloads_toggle(self):
        return self.driver.find_element(By.XPATH, '(//*[@title="Toggle"])[4]')

    def get_downloads_checkbox(self):
        return self.driver.find_element(By.XPATH, '//*[@for="tree-node-downloads"]/*[@class="rct-checkbox"]')

    def get_result(self):
        return self.driver.find_element(By.XPATH, '//*[@id="result"]')
