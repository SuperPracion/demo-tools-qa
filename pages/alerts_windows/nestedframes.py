from base.driver import Driver
from selenium.webdriver.common.by import By


class NestedFrames(Driver):
    def get_parent_frame(self):
        return self.driver.find_element(By.XPATH, '//*[@id="frame1Wrapper"]')

    def switch_to_parent_frame(self):
        frame = self.get_parent_frame()
        self.driver.switch_to.frame(frame)
        assert self.driver.find_element(By.XPATH, '//body').text == 'Parent frame'

    def get_child_frame(self):
        return self.driver.find_element(By.XPATH, '//*[@srcdoc="<p>Child Iframe</p>"]')

    def switch_to_child_frame(self):
        frame = self.get_child_frame()
        self.driver.switch_to.frame(frame)
        assert self.driver.find_element(By.XPATH, '//body').text == 'Child Iframe'
