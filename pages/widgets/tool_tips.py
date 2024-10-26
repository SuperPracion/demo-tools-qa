from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from base.driver import Driver


class ToolsTips(Driver):
    def get_tools_tip_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="toolTipButton"]')

    def move_to_tool_tip_button(self):
        ActionChains(self.driver).move_to_element(self.get_tools_tip_button()).perform()

    def get_tools_tip_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="toolTipTextField"]')

    def move_to_tools_tip_field(self):
        ActionChains(self.driver).move_to_element(self.get_tools_tip_field()).perform()

    def get_tools_tip_container(self):
        return self.driver.find_element(By.XPATH, '//*[@id="texToolTopContainer"]')

    def move_to_tools_tip_container_contrary(self):
        element = self.get_tools_tip_container().find_element(By.XPATH, '//*[contains(text(), "Contrary")]')
        ActionChains(self.driver).move_to_element(element).perform()

    def move_to_tools_tip_container_1_10_32(self):
        element = self.get_tools_tip_container().find_element(By.XPATH, '//*[contains(text(), "1.10.32")]')
        ActionChains(self.driver).move_to_element(element).perform()