import time
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from pages.main.main import Main
from pages.alerts_windows.alerts import Alerts
from pages.alerts_windows.alerts_windows import AlertsWindows
from base.element_found_exception import ElementFoundException


@pytest.fixture
def alerts(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.alerts_windows_button_click()
    alerts_windows = AlertsWindows(setup_driver)
    alerts_windows.alerts_button_click()
    alerts = Alerts(setup_driver)
    yield alerts


@allure.title('Accept simple alert with check text')
class TestSimpleAlert:
    @allure.step('check text in simple alert')
    def test_accept_simple_alert(self, alerts):
        alerts.click(alerts.get_alert_button())
        assert alerts.get_alert()
        assert alerts.get_alert().text == 'You clicked a button'
        alerts.accept_alert()
        try:
            alerts.get_alert()
            raise ElementFoundException
        except TimeoutException:
            pass


@allure.title('Accept timer alert')
class TestTimerAlert:
    @allure.step('accept alert after timer')
    def test_accept_timer_alert(self, alerts):
        alerts.click(alerts.get_timer_alert_button())
        time.sleep(6)
        assert alerts.get_alert()
        assert alerts.get_alert().text == 'This alert appeared after 5 seconds'
        alerts.accept_alert()
        try:
            alerts.get_alert()
            raise ElementFoundException
        except TimeoutException:
            pass


@allure.title('Check alert witch confirm')
class TestConfirmAlert:
    @allure.step('accept confirm alert')
    def test_accept_confirm_alert(self, alerts):
        alerts.click(alerts.get_confirm_alert_button())
        assert alerts.get_alert()
        assert alerts.get_alert().text == 'Do you confirm action?'
        alerts.accept_alert()
        assert alerts.driver.find_element(By.XPATH, '//*[@id="confirmResult"]').text == 'You selected Ok'

    @allure.step('dismiss confirm alert')
    def test_cancel_confirm_alert(self, alerts):
        alerts.click(alerts.get_confirm_alert_button())
        assert alerts.get_alert()
        assert alerts.get_alert().text == 'Do you confirm action?'
        alerts.dismiss_alert()
        assert alerts.driver.find_element(By.XPATH, '//*[@id="confirmResult"]').text == 'You selected Cancel'


@allure.title('Alert with promt')
class TestPromtAlert:
    @allure.step('accept promt alert')
    def test_accept_promt_alert(sefl, alerts):
        alerts.click(alerts.get_promt_alert_button())
        assert alerts.get_alert()
        assert alerts.get_alert().text == 'Please enter your name'
        alerts.get_alert().send_keys('123')
        alerts.accept_alert()
        assert alerts.driver.find_element(By.XPATH, '//*[@id="promptResult"]').text == f'You entered 123'

    @allure.step('dismiss promt alert')
    def test_cancel_promt_alert(self, alerts):
        alerts.click(alerts.get_promt_alert_button())
        assert alerts.get_alert()
        assert alerts.get_alert().text == 'Please enter your name'
        alerts.dismiss_alert()
        try:
            alerts.get_alert()
            raise ElementFoundException
        except TimeoutException:
            pass
