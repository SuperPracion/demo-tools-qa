from selenium.webdriver.common.by import By

from base.driver import Driver


class NestedFrames(Driver):
    def get_parent_frame(self):
        return self.driver.find_element(By.XPATH, '//*[@id="frame1"]')

    def switch_to_parent_frame(self):
        frame = self.get_parent_frame()
        self.driver.switch_to.frame(frame)
        assert self.driver.find_element(By.XPATH, '//body').text == 'Parent frame'

    def get_child_frame(self):
        return self.driver.find_element(By.XPATH, '//*[@srcdoc="<p>Child Iframe</p>"]')

    def switch_to_child_frame(self):
        self.switch_to_parent_frame()
        frame = self.get_child_frame()
        self.driver.switch_to.frame(frame)
        assert self.driver.find_element(By.XPATH, '//body').text == 'Child Iframe'
