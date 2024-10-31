from base.driver import Driver

from selenium.webdriver.common.by import By

class Slider(Driver):
    def get_range_slider(self):
        return self.driver.find_element(By.XPATH, '//*[@class="range-slider range-slider--primary"]')

    def get_slider_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="sliderValue"]')