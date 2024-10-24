from base.driver import Driver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Slider(Driver):
    def get_range_slider(self):
        return self.driver.find_element(By.XPATH, '//*[@class="range-slider range-slider--primary"]')

    def set_range_slider_value(self):
        mover = ActionChains(self.driver)
        slider = self.get_range_slider()
        mover.click_and_hold(slider).move_by_offset(20, 0).release().perform()

    def get_slider_field(self):
        return self.driver.find_element(By.XPATH, '//*[@id="sliderValue"]')

    def set_slider_field_value(self, value):
        self.get_slider_field().send_keys(value)