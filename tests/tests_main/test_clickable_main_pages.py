import pytest
from base.user import User
from pages.main.main import Main

from selenium import webdriver


@pytest.fixture
def setup_user():
    user = User()
    yield user


@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


@pytest.fixture
def main_page(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    yield main_page


def test_open_elements_page(main_page):
    main_page.elements_button_click()


def test_open_forms_page(main_page):
    main_page.forms_buttons_click()


def test_open_alerts_windows_page(main_page):
    main_page.alerts_windows_button_click()


def test_open_widgets_page(main_page):
    main_page.widgets_button_click()


def test_open_interaction_page(main_page):
    main_page.interaction_button_click()


def test_open_books_page(main_page):
    main_page.books_button_click()


def test_open_all_pages(main_page):
    main_page.elements_button_click()
    main_page.driver.back()

    main_page.forms_buttons_click()
    main_page.driver.back()

    main_page.alerts_windows_button_click()
    main_page.driver.back()

    main_page.widgets_button_click()
    main_page.driver.back()

    main_page.interaction_button_click()
    main_page.driver.back()

    main_page.books_button_click()
    main_page.driver.back()
