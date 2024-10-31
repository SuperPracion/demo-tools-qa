from selenium.webdriver.common.by import By

from base.driver import Driver


class ProgressBar(Driver):
    def get_start_stop_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="startStopButton"]')

    def get_progress_bar(self):
        return self.driver.find_element(By.XPATH, '//*[@role="progressbar"]')

    def get_reset_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="resetButton"]')
