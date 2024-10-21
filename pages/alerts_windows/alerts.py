from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from base.driver import Driver


class Alerts(Driver):
    def get_alert_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="alertButton"]')

    def alert_button_click(self):
        self.get_alert_button().click()

    def alert_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def alert_dismiss(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def get_timer_alert_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="timerAlertButton"]')

    def time_alert_button_click(self):
        self.get_timer_alert_button().click()

    def get_confirm_alert_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="confirmButton"]')

    def confirm_alert_button_click(self):
        self.get_confirm_alert_button().click()

    def confirm_alert_accept(self):
        self.alert_accept()
        assert self.driver.find_element(By.XPATH, '//*[@id="confirmResult"]').text =='You selected Ok'

    def confirm_alert_dismiss(self):
        self.alert_dismiss()
        assert self.driver.find_element(By.XPATH, '//*[@id="confirmResult"]').text == 'You selected Cancel'

    def get_promt_alert_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="promtButton"]')

    def promt_alert_button_click(self):
        self.get_promt_alert_button().click()

    def promt_alert_accept(self, value):
        alert = self.driver.switch_to.alert
        alert.send_keys(value)
        self.alert_accept()
        assert self.driver.find_element(By.XPATH, '//*[@id="promptResult"]').text == f'You entered {value}'

    def promt_alert_dismiss(self):
        self.alert_dismiss()
        try:
            self.driver.find_element(By.XPATH, '//*[@id="promptResult"]')
        except NoSuchElementException:
            pass