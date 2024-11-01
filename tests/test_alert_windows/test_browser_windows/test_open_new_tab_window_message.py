import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pages.alerts_windows.browser_windows import BrowserWindows

@allure.step('open browser window (its resource) page ')
@pytest.fixture
def browser_window_page(alerts_windows_page):
    alerts_windows_page.click(alerts_windows_page.get_browser_windows_button())
    browser_page = BrowserWindows(alerts_windows_page.driver)
    yield browser_page


@allure.title('Test new tab')
@allure.step('open new tab')
def test_open_new_tab(browser_window_page):
    button = browser_window_page.get_new_tab_button()
    browser_window_page.click(button)
    assert len(browser_window_page.driver.window_handles) > 1
    browser_window_page.driver.switch_to.window(browser_window_page.driver.window_handles[1])
    assert browser_window_page.driver.find_element(By.XPATH, "//*[@id='sampleHeading']").text == 'This is a sample page'
    allure.attach(browser_window_page.driver.get_screenshot_as_png(), 'open_new_tab', AttachmentType.PNG)


@allure.title('Test new window')
@allure.step('open new window')
def test_open_new_window(browser_window_page):
    button = browser_window_page.get_new_window_button()
    browser_window_page.click(button)
    assert len(browser_window_page.driver.window_handles) > 1
    browser_window_page.driver.switch_to.window(browser_window_page.driver.window_handles[1])
    assert browser_window_page.driver.find_element(By.XPATH, "//*[@id='sampleHeading']").text == 'This is a sample page'
    allure.attach(browser_window_page.driver.get_screenshot_as_png(), 'open_new_window', AttachmentType.PNG)


@allure.title('Test new window message')
@allure.step('open new window message')
def test_open_new_windows_message(browser_window_page):
    button = browser_window_page.get_new_window_message_button()
    browser_window_page.click(button)
    assert len(browser_window_page.driver.window_handles) > 1
    allure.attach(browser_window_page.driver.get_screenshot_as_png(), 'open_new_windows_message', AttachmentType.PNG)
