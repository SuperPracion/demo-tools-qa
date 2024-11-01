from selenium.webdriver.common.by import By

from base.driver import Driver


class NestedFrames(Driver):
    def get_parent_frame(self):
        return self.driver.find_element(By.XPATH, '//*[@id="frame1"]')

    def get_child_frame(self):
        return self.driver.find_element(By.XPATH, '//*[@srcdoc="<p>Child Iframe</p>"]')
