import pytest

from pages.main.main import Main
from pages.elements.elements import Elements
from pages.elements.checkbox import CheckBox


@pytest.fixture
def checkbox(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.elements_button_click()
    elements = Elements(setup_driver)
    elements.checkbox_button_click()
    checkbox = CheckBox(setup_driver)
    yield checkbox


def test_open_home(checkbox):
    checkbox.home_toggle_click()


def test_select_home_checkbox(checkbox):
    checkbox.home_check_box_click()


def test_open_desktop(checkbox):
    checkbox.home_toggle_click()
    checkbox.desktop_toggle_click()


def test_select_desktop_checkbox(checkbox):
    checkbox.home_toggle_click()
    checkbox.desktop_checkbox_click()


def test_open_documents(checkbox):
    checkbox.home_toggle_click()
    checkbox.documents_toggle_click()


def test_select_documents_checkbox(checkbox):
    checkbox.home_toggle_click()
    checkbox.documents_checkbox_click()


def test_open_downloads(checkbox):
    checkbox.home_toggle_click()
    checkbox.downloads_toggle_click()


def test_select_downloads_checkbox(checkbox):
    checkbox.home_toggle_click()
    checkbox.download_checkbox_click()
