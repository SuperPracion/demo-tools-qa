import time
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from pages.alerts_windows.alerts import Alerts
from base.element_found_exception import ElementFoundException


@pytest.fixture
def alerts_page(alerts_windows_page):
    alerts_windows_page.click(alerts_windows_page.get_alerts_button())
    alerts_page = Alerts(alerts_windows_page.driver)
    yield alerts_page


@allure.title('Accept simple alert with check text')
class TestSimpleAlert:
    @allure.step('check text in simple alert')
    def test_accept_simple_alert(self, alerts_page):
        alerts_page.click(alerts_page.get_alert_button())
        assert alerts_page.get_alert()
        assert alerts_page.get_alert().text == 'You clicked a button'
        alerts_page.accept_alert()
        try:
            alerts_page.get_alert()
            raise ElementFoundException
        except TimeoutException:
            pass


@allure.title('Accept timer alert')
class TestTimerAlert:
    @allure.step('accept alert after timer')
    def test_accept_timer_alert(self, alerts_page):
        alerts_page.click(alerts_page.get_timer_alert_button())
        time.sleep(6)
        assert alerts_page.get_alert()
        assert alerts_page.get_alert().text == 'This alert appeared after 5 seconds'
        alerts_page.accept_alert()
        try:
            alerts_page.get_alert()
            raise ElementFoundException
        except TimeoutException:
            pass


@allure.title('Check alert witch confirm')
class TestConfirmAlert:
    @allure.step('accept confirm alert')
    def test_accept_confirm_alert(self, alerts_page):
        alerts_page.click(alerts_page.get_confirm_alert_button())
        assert alerts_page.get_alert()
        assert alerts_page.get_alert().text == 'Do you confirm action?'
        alerts_page.accept_alert()
        assert alerts_page.driver.find_element(By.XPATH, '//*[@id="confirmResult"]').text == 'You selected Ok'

    @allure.step('dismiss confirm alert')
    def test_cancel_confirm_alert(self, alerts_page):
        alerts_page.click(alerts_page.get_confirm_alert_button())
        assert alerts_page.get_alert()
        assert alerts_page.get_alert().text == 'Do you confirm action?'
        alerts_page.dismiss_alert()
        assert alerts_page.driver.find_element(By.XPATH, '//*[@id="confirmResult"]').text == 'You selected Cancel'


@allure.title('Alert with promt')
class TestPromtAlert:
    @allure.step('accept promt alert')
    def test_accept_promt_alert(sefl, alerts_page):
        alerts_page.click(alerts_page.get_promt_alert_button())
        assert alerts_page.get_alert()
        assert alerts_page.get_alert().text == 'Please enter your name'
        alerts_page.get_alert().send_keys('123')
        alerts_page.accept_alert()
        assert alerts_page.driver.find_element(By.XPATH, '//*[@id="promptResult"]').text == f'You entered 123'

    @allure.step('dismiss promt alert')
    def test_cancel_promt_alert(self, alerts_page):
        alerts_page.click(alerts_page.get_promt_alert_button())
        assert alerts_page.get_alert()
        assert alerts_page.get_alert().text == 'Please enter your name'
        alerts_page.dismiss_alert()
        try:
            alerts_page.get_alert()
            raise ElementFoundException
        except TimeoutException:
            pass
