from selenium.webdriver.common.by import By

from base.driver import Driver


class Tabs(Driver):
    def get_what_tab(self):
        return self.driver.find_element(By.LINK_TEXT, 'What')

    def get_origin_tab(self):
        return self.driver.find_element(By.LINK_TEXT, 'Origin')

    def get_use_tab(self):
        return self.driver.find_element(By.LINK_TEXT, 'Use')

    def get_more_tab(self):
        return self.driver.find_element(By.LINK_TEXT, 'More')
