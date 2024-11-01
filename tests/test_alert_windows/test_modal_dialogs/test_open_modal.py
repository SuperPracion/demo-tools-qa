import allure
import pytest

from pages.alerts_windows.modal_dialogs import ModalDialogs


@allure.step('open modal dialogs page')
@pytest.fixture
def modal_dialogs_page(alerts_windows_page):
    alerts_windows_page.click(alerts_windows_page.get_modal_dialogs_button())
    modal_dialogs_page = ModalDialogs(alerts_windows_page.driver)
    yield modal_dialogs_page


@allure.title('')
@allure.step('')
def test_open_small_modal(modal_dialogs_page):
    modal_dialogs_page.small_modal_button_click()


@allure.title('')
@allure.step('')
def test_open_lange_modal(modal_dialogs_page):
    modal_dialogs_page.large_modal_button_click()


@allure.title('')
@allure.step('')
def test_small_dialog_close(modal_dialogs_page):
    modal_dialogs_page.small_modal_button_click()
    modal_dialogs_page.close_button_click()


@allure.title('')
@allure.step('')
def test_large_dialog_close(modal_dialogs_page):
    modal_dialogs_page.large_modal_button_click()
    modal_dialogs_page.close_button_click()


@allure.title('')
@allure.step('')
def test_small_dialog_close_with_x(modal_dialogs_page):
    modal_dialogs_page.small_modal_button_click()
    modal_dialogs_page.small_button_close_click()


@allure.title('')
@allure.step('')
def test_large_dialog_close_with_x(modal_dialogs_page):
    modal_dialogs_page.large_modal_button_click()
    modal_dialogs_page.small_button_close_click()
