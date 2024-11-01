import allure
import pytest
from allure_commons.types import AttachmentType

from pages.alerts_windows.modal_dialogs import ModalDialogs


@allure.step('open modal dialogs page')
@pytest.fixture
def modal_dialogs_page(alerts_windows_page):
    alerts_windows_page.click(alerts_windows_page.get_modal_dialogs_button())
    modal_dialogs_page = ModalDialogs(alerts_windows_page.driver)
    yield modal_dialogs_page


@allure.title('Test open small dialog modal')
@allure.step('open small modal')
def test_open_small_modal(modal_dialogs_page):
    modal_dialogs_page.small_modal_button_click()
    allure.attach(modal_dialogs_page.driver.get_screenshot_as_png(), 'open_small_modal', AttachmentType.PNG)


@allure.title('Test open lange dialog modal')
@allure.step('open lange modal')
def test_open_lange_modal(modal_dialogs_page):
    modal_dialogs_page.large_modal_button_click()
    allure.attach(modal_dialogs_page.driver.get_screenshot_as_png(), 'open_lange_modal', AttachmentType.PNG)


@allure.title('Test close small dialog modal')
@allure.step('close small modal')
def test_small_dialog_close(modal_dialogs_page):
    modal_dialogs_page.small_modal_button_click()
    modal_dialogs_page.close_button_click()
    allure.attach(modal_dialogs_page.driver.get_screenshot_as_png(), 'small_dialog_close', AttachmentType.PNG)


@allure.title('Test close large dialog modal')
@allure.step('close large modal')
def test_large_dialog_close(modal_dialogs_page):
    modal_dialogs_page.large_modal_button_click()
    modal_dialogs_page.close_button_click()
    allure.attach(modal_dialogs_page.driver.get_screenshot_as_png(), 'large_dialog_close', AttachmentType.PNG)


@allure.title('Test close small dialog with X')
@allure.step('close small modal')
def test_small_dialog_close_with_x(modal_dialogs_page):
    modal_dialogs_page.small_modal_button_click()
    modal_dialogs_page.small_button_close_click()
    allure.attach(modal_dialogs_page.driver.get_screenshot_as_png(), 'small_dialog_close_with_x', AttachmentType.PNG)


@allure.title('Test close large dialog with X')
@allure.step('close large modal')
def test_large_dialog_close_with_x(modal_dialogs_page):
    modal_dialogs_page.large_modal_button_click()
    modal_dialogs_page.small_button_close_click()
    allure.attach(modal_dialogs_page.driver.get_screenshot_as_png(), 'large_dialog_close_with_x', AttachmentType.PNG)
