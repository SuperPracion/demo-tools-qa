from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from base.driver import Driver


class Resizable(Driver):
    def get_resizable_box_with_restriction(self):
        return self.driver.find_element(By.XPATH, '//*[@id="resizableBoxWithRestriction"]')

    def get_resizable(self):
        return self.driver.find_element(By.XPATH, '//*[@id="resizable"]')

    def set_resizable_size(self, element, width, height):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, width - 200, height - 200)
