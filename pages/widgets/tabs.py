from selenium.webdriver.common.by import By

from base.driver import Driver


class Tabs(Driver):
    def get_what_tab(self):
        return self.driver.find_element(By.LINK_TEXT, 'What')

    def what_tab_click(self):
        self.get_what_tab().click()
        assert self.get_what_tab().get_attribute('aria-hidden') == 'false'

    def get_origin_tab(self):
        return self.driver.find_element(By.LINK_TEXT, 'Origin')

    def origin_tab_click(self):
        self.get_origin_tab().click()
        assert self.get_origin_tab().get_attribute('aria-hidden') == 'false'

    def get_use_tab(self):
        return self.driver.find_element(By.LINK_TEXT, 'Use')

    def use_tab_click(self):
        self.get_use_tab().click()
        assert self.get_use_tab().get_attribute('aria-hidden') == 'false'

    def get_more_tab(self):
        return self.driver.find_element(By.LINK_TEXT, 'More')

    def more_tab_click(self):
        self.get_more_tab().click()
        assert self.get_more_tab().get_attribute('aria-hidden') == 'false'