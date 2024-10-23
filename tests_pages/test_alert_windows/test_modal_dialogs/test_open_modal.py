import pytest

from pages.main.main import Main
from pages.alerts_windows.alerts_windows import AlertsWindows
from pages.alerts_windows.modal_dialogs import ModalDialogs


@pytest.fixture
def modal_dialogs(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.alerts_windows_button_click()
    alerts_windows = AlertsWindows(setup_driver)
    alerts_windows.modal_dialogs_button_click()
    modal_dialogs = ModalDialogs(setup_driver)
    yield modal_dialogs


def test_open_small_modal(modal_dialogs):
    modal_dialogs.small_modal_button_click()


def test_open_lange_modal(modal_dialogs):
    modal_dialogs.large_modal_button_click()


def test_small_dialog_close(modal_dialogs):
    modal_dialogs.small_modal_button_click()
    modal_dialogs.close_button_click()


def test_large_dialog_close(modal_dialogs):
    modal_dialogs.large_modal_button_click()
    modal_dialogs.close_button_click()


def test_small_dialog_close_with_x(modal_dialogs):
    modal_dialogs.small_modal_button_click()
    modal_dialogs.small_button_close_click()


def test_large_dialog_close_with_x(modal_dialogs):
    modal_dialogs.large_modal_button_click()
    modal_dialogs.small_button_close_click()
