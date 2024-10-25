import pytest

from pages.main.main import Main
from pages.widgets.widgets import Widgets
from pages.widgets.tabs import Tabs


@pytest.fixture
def tabs(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.widgets_button_click()
    widgets = Widgets(setup_driver)
    widgets.tabs_button_click()
    tabs = Tabs(setup_driver)
    yield tabs

def test_open_what_tab(tabs):
    tabs.what_tab_click()


def test_open_origin_tab(tabs):
    tabs.origin_tab_click()


def test_open_use_tab(tabs):
    tabs.use_tab_click()


def test_open_more_tab(tabs):
    tabs.more_tab_click()
