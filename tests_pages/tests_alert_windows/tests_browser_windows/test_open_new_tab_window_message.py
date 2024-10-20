import pytest

from pages.main.main import Main
from pages.alerts_windows.alerts_windows import AlertsWindows
from pages.alerts_windows.browser_windows import BrowserWindows


@pytest.fixture
def browser_windows(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.alerts_windows_button_click()
    alerts_windows = AlertsWindows(setup_driver)
    alerts_windows.browser_windows_button_click()
    browser_windows = BrowserWindows(setup_driver)
    yield browser_windows


def test_open_new_tab(browser_windows):
    browser_windows.new_tab_button_click()


def test_open_new_window(browser_windows):
    browser_windows.new_window_button_click()


def test_open_new_windows_message(browser_windows):
    browser_windows.new_window_message_button_click()
