import allure
import pytest
from selenium.webdriver.common.by import By

from pages.alerts_windows.browser_windows import BrowserWindows


@pytest.fixture
def browser_page(alerts_windows_page):
    alerts_windows_page.click(alerts_windows_page.get_browser_windows_button())
    browser_page = BrowserWindows(alerts_windows_page.driver)
    yield browser_page


@allure.title('')
@allure.step('')
def test_open_new_tab(browser_page):
    button = browser_page.get_new_tab_button()
    browser_page.click(button)
    assert len(browser_page.driver.window_handles) > 1
    browser_page.driver.switch_to.window(browser_page.driver.window_handles[1])
    assert browser_page.driver.find_element(By.XPATH, "//*[@id='sampleHeading']").text == 'This is a sample page'


@allure.title('')
@allure.step('')
def test_open_new_window(browser_page):
    button = browser_page.get_new_window_button()
    browser_page.click(button)
    assert len(browser_page.driver.window_handles) > 1
    browser_page.driver.switch_to.window(browser_page.driver.window_handles[1])
    assert browser_page.driver.find_element(By.XPATH, "//*[@id='sampleHeading']").text == 'This is a sample page'


@allure.title('')
@allure.step('')
def test_open_new_windows_message(browser_page):
    button = browser_page.get_new_window_message_button()
    browser_page.click(button)
    assert len(browser_page.driver.window_handles) > 1
