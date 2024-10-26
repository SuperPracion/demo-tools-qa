import pytest
from time import sleep

from pages.main.main import Main
from pages.alerts_windows.alerts_windows import AlertsWindows
from pages.alerts_windows.alerts import Alerts


@pytest.fixture
def alert(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.alerts_windows_button_click()
    alerts_windows = AlertsWindows(setup_driver)
    alerts_windows.alerts_button_click()
    alert = Alerts(setup_driver)
    yield alert


def test_accept_simple_alert(alert):
    alert.alert_button_click()
    alert.alert_accept()


def test_accept_timer_alert(alert):
    alert.time_alert_button_click()
    sleep(5)
    alert.alert_accept()


def test_accept_confirm_alert(alert):
    alert.confirm_alert_button_click()
    alert.confirm_alert_accept()


def test_cancel_confirm_alert(alert):
    alert.confirm_alert_button_click()
    alert.confirm_alert_dismiss()


def test_accept_promt_alert(alert):
    alert.promt_alert_button_click()
    alert.promt_alert_accept('123')


def test_cancel_promt_alert(alert):
    alert.promt_alert_button_click()
    alert.promt_alert_dismiss()
