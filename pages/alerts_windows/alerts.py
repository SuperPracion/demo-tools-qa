from selenium.webdriver.common.by import By

from base.driver import Driver


class Alerts(Driver):
    def get_alert_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="promtButton"]')

    def alert_button_click(self):
        self.get_alert_button().click()
        return self.driver.switch_to.alert

    def get_timer_alert_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="timerAlertButton"]')

    def time_alert_button_click(self):
        self.get_timer_alert_button().click()
        return self.driver.switch_to.alert

    def get_confirm_alert_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="confirmButton"]')

    def confirm_alert_button_click(self):
        self.get_confirm_alert_button().click()
        return self.driver.switch_to.alert

    def get_promt_alert_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="promtButton"]')

    def promt_alert_button_click(self):
        self.get_promt_alert_button().click()
        return self.driver.switch_to.alert
