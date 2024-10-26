import pytest

from pages.main.main import Main
from pages.widgets.widgets import Widgets
from pages.widgets.auto_complete import AutoComplete


@pytest.fixture
def auto_complete(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.widgets_button_click()
    widgets = Widgets(setup_driver)
    widgets.auto_complete_button_click()
    auto_complete = AutoComplete(setup_driver)
    yield auto_complete

def test_multiple_auto_complete(auto_complete):
    auto_complete.auto_complete_multiple_write('Re')
    auto_complete.auto_complete_multiple_write('Ye')

def test_single_auto_complete(auto_complete):
    auto_complete.auto_complete_single_write('Re')

def test_single_and_auto_complete(auto_complete):
    auto_complete.auto_complete_single_write('Gre')
    auto_complete.auto_complete_multiple_write('Blu')