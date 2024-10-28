import pytest
from selenium.webdriver.common.by import By

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
    button = browser_windows.get_new_tab_button()
    browser_windows.click(button)
    assert len(browser_windows.driver.window_handles) > 1
    browser_windows.driver.switch_to.window(browser_windows.driver.window_handles[1])
    assert browser_windows.driver.find_element(By.XPATH, "//*[@id='sampleHeading']").text == 'This is a sample page'


def test_open_new_window(browser_windows):
    button = browser_windows.get_new_window_button()
    browser_windows.click(button)
    assert len(browser_windows.driver.window_handles) > 1
    browser_windows.driver.switch_to.window(browser_windows.driver.window_handles[1])
    assert browser_windows.driver.find_element(By.XPATH, "//*[@id='sampleHeading']").text == 'This is a sample page'


def test_open_new_windows_message(browser_windows):
    button = browser_windows.get_new_window_message_button()
    browser_windows.click(button)
    assert len(browser_windows.driver.window_handles) > 1
