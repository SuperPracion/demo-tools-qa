import pytest
from selenium.webdriver.common.by import By

from pages.main.main import Main
from pages.widgets.widgets import Widgets
from pages.widgets.select_menu import SelectMenu


@pytest.fixture
def select_menu(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.widgets_button_click()
    widgets = Widgets(setup_driver)
    widgets.driver.execute_script("window.scrollTo(0, 250)")
    widgets.select_menu_click()
    select_menu = SelectMenu(setup_driver)
    yield select_menu


def test_select_option_value(select_menu):
    value = 'Group 2, option 1'
    select_menu.click_with_option_group_container()
    select_menu.select_container_value_by_text(value)
    assert select_menu.get_with_option_group_container().find_element(By.XPATH, '//*[@class=" css-1uccc91-singleValue"]').text == value


def test_select_one_title(select_menu):
    value = 'Mr.'
    select_menu.click_select_one_container()
    select_menu.select_container_value_by_text(value)
    assert select_menu.get_select_one_container().find_element(By.XPATH, '//*[@class=" css-1uccc91-singleValue"]').text == value


def test_select_old_style_menu_value(select_menu):
    select_menu.click_old_select_container()
    select_menu.select_container_value_by_text('Black')


def test_select_multiselect_drop_down_menu_value(select_menu):
    value = 'Green'
    select_menu.click_multi_drop_down_container()
    select_menu.select_container_value_by_text(value, 2)
    assert select_menu.driver.find_element(By.XPATH, '//*[@class="css-12jo7m5"]').text == value


def test_select_standard_multi_select_value(select_menu):
    select_menu.select_container_value_by_text('Saab')
