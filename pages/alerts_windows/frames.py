from selenium.webdriver.common.by import By

from base.driver import Driver


class Framer(Driver):
    def get_frame1(self):
        return self.driver.find_element(By.XPATH, '//*[@id="frame1Wrapper"]')

    def switch_to_frame1(self):
        frame = self.get_frame1()
        self.driver.switch_to.frame(frame)
        assert self.driver.find_element(By.XPATH, '//*[@id="sampleHeading"]') == 'This is a sample page'

    def get_frame2(self):
        return self.driver.find_element(By.XPATH, '//*[@id="frame2Wrapper"]')

    def switch_to_frame2(self):
        frame = self.get_frame2()
        self.driver.switch_to.frame(frame)
        assert self.driver.find_element(By.XPATH, '//*[@id="sampleHeading"]') == 'This is a sample page'