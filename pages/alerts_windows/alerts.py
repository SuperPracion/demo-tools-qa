from selenium.webdriver.common.by import By

from base.driver import Driver


class Alerts(Driver):
    def get_alert_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="alertButton"]')

    def get_timer_alert_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="timerAlertButton"]')

    def get_confirm_alert_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="confirmButton"]')

    def get_promt_alert_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="promtButton"]')
