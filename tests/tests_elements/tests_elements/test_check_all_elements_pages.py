from base.user import User
from pages.main.main import Main
from pages.elements.elements import Elements

import pytest
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
def elements(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.elements_button_click()
    elements = Elements(setup_driver)
    yield elements


def test_open_text_box_page(elements):
    elements.text_box_button_click()


def test_open_check_box_page(elements):
    elements.check_box_button_click()


def test_open_radio_button_page(elements):
    elements.radio_button_click()


def test_open_web_tables_page(elements):
    elements.web_tables_button_click()


def test_open_buttons_page(elements):
    elements.buttons_button_click()


def test_open_links_page(elements):
    elements.links_button_click()


def test_open_broken_page(elements):
    elements.broken_links_images_button_click()


def test_open_upload_download_page(elements):
    elements.upload_and_download_button_click()


def test_open_dynamic_properties_page(elements):
    elements.dynamic_properties_button_click()
