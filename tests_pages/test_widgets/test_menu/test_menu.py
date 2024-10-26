import pytest
import time

from pages.main.main import Main
from pages.widgets.widgets import Widgets
from pages.widgets.menu import Menu


@pytest.fixture
def menu(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.widgets_button_click()
    widgets = Widgets(setup_driver)
    widgets.menu_button_click()
    menu = Menu(setup_driver)
    yield menu

def test_menu_item_1(menu):
    menu.move_to_item(menu.get_main_item_1())
    assert menu.get_main_item_1().text == 'Main Item 1'


def test_menu_item_2(menu):
    menu.move_to_item(menu.get_main_item_2())
    assert menu.get_main_item_2().text == 'Main Item 2'


def test_menu_sub_item_1(menu):
    menu.move_to_item(menu.get_main_item_2())
    menu.move_to_item(menu.get_sub_item_1())
    assert menu.get_sub_item_1().text == 'Sub Item'


def test_menu_sub_item_2(menu):
    menu.move_to_item(menu.get_main_item_2())
    menu.move_to_item(menu.get_sub_item_2())
    assert menu.get_sub_item_2().text == 'Sub Item'


def test_menu_sub_sub_list(menu):
    menu.move_to_item(menu.get_main_item_2())
    menu.move_to_item(menu.get_sub_sub_list())
    assert menu.get_sub_sub_list().text == 'SUB SUB LIST »'


def test_menu_sub_sub_item_1(menu):
    menu.move_to_item(menu.get_main_item_2())
    menu.move_to_item(menu.get_sub_sub_list())
    menu.move_to_item(menu.get_sub_sub_item_1())
    assert menu.get_sub_sub_item_1().text == 'Sub Sub Item 1'


def test_menu_sub_sub_item_2(menu):
    menu.move_to_item(menu.get_main_item_2())
    menu.move_to_item(menu.get_sub_sub_list())
    menu.move_to_item(menu.get_sub_sub_item_2())
    assert menu.get_sub_sub_item_2().text == 'Sub Sub Item 2'


def test_menu_item_3(menu):
    menu.move_to_item(menu.get_main_item_3())
    assert menu.get_main_item_3().text == 'Main Item 3'
