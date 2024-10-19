from anyio.abc import value

from base.driver import Driver

from selenium.webdriver.common.by import By


class CheckBox(Driver):
    def get_expand_all_button(self):
        return self.driver.find_element(By.XPATH, '//*[@aria-label="Expand all"]')

    def expand_button_click(self):
        self.get_expand_all_button()
        # TODO добавить проверки

    def get_collapse_all_button(self):
        return self.driver.find_element(By.XPATH, '//*[@aria-label="Collapse all"]')

    def collapse_all_button_click(self):
        self.get_collapse_all_button().click()
        # TODO добавить проверки

    def get_home_toggle(self):
        return self.driver.find_element(By.XPATH, '(//*[@title="Toggle"])[1]')

    def home_toggle_click(self):
        self.get_home_toggle().click()
        # TODO добавить проверки

    def get_home_checkbox(self):
        return self.driver.find_element(By.XPATH, '//*[@for="tree-node-home"]/*[@class="rct-checkbox"]')

    def home_check_box_click(self):
        self.get_home_checkbox().click()
        # TODO добавить проверки

    def get_desktop_toggle(self):
        return self.driver.find_element(By.XPATH, '(//*[@title="Toggle"])[2]')

    def desktop_toggle_click(self):
        self.get_desktop_toggle().click()

    def get_desktop_checkbox(self):
        return self.driver.find_element(By.XPATH, '//*[@for="tree-node-desktop"]/*[@class="rct-checkbox"]')

    def desktop_checkbox_click(self):
        self.get_desktop_checkbox().click()
        # TODO добавить проверки

    def get_documents_toggle(self):
        return self.driver.find_element(By.XPATH, '(//*[@title="Toggle"])[3]')

    def documents_toggle_click(self):
        self.get_documents_toggle().click()
        # TODO добавить проверки

    def get_documents_checkbox(self):
        return self.driver.find_element(By.XPATH, '//*[@for="tree-node-documents"]/*[@class="rct-checkbox"]')

    def documents_checkbox_click(self):
        self.get_documents_checkbox().click()
        # TODO добавить проверки

    def get_downloads_toggle(self):
        return self.driver.find_element(By.XPATH, '(//*[@title="Toggle"])[4]')

    def downloads_toggle_click(self):
        self.get_downloads_toggle().click()
        # TODO добавить проверки

    def get_downloads_checkbox(self):
        return self.driver.find_element(By.XPATH, '//*[@for="tree-node-downloads"]/*[@class="rct-checkbox"]')

    def download_checkbox_click(self):
        self.get_downloads_checkbox().click()
        # TODO добавить проверки

    def get_result(self):
        return self.driver.find_element(By.XPATH, '//*[@id="result"]')

    def result_check(self, *values):
        values = list(*values)
        index = 1
        while element := self.driver.find_element(By.XPATH, f'//*[@class="text-success"][{index}]'):
            print(element.text)
            values.remove(value)

        assert values == []