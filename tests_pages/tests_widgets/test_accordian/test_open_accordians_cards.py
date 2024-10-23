import pytest

from pages.main.main import Main
from pages.widgets.widgets import Widgets
from pages.widgets.accordian import Accordian


@pytest.fixture
def accordian(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.widgets_button_click()
    widgets = Widgets(setup_driver)
    widgets.accordian_button_click()
    accordian = Accordian(setup_driver)
    yield accordian


def test_what_is_lorem_open(accordian):
    accordian.card_header_what_is_lorem_click()


def test_where_does_it_come_from_open(accordian):
    accordian.card_header_where_does_it_come_from_click()


def test_why_do_we_use_it(accordian):
    accordian.card_header_why_do_we_use_it_click()


def test_open_all_cards(accordian):
    accordian.card_header_why_do_we_use_it_click()
    accordian.card_header_where_does_it_come_from_click()
    accordian.card_header_what_is_lorem_click()