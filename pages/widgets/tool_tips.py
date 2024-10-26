from selenium.webdriver.common.by import By

from base.driver import Driver

class ToolsTips(Driver):
    def get_tools_tip_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="toolTipButton"]')

    def get_tools_tip_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="toolTipTextField"]')

    def get_tools_tip_container(self):
        return self.driver.find_element(By.XPATH, '//*[@id="texToolTopContainer"]')