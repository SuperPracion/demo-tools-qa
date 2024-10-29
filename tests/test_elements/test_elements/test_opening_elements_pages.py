import pytest

from pages.main.main import Main
from pages.elements.elements import Elements


def test_open_text_box_page(elements_page):
    elements_page.text_box_button_click()


def test_open_check_box_page(elements_page):
    elements_page.checkbox_button_click()


def test_open_radio_button_page(elements_page):
    elements_page.radio_button_click()


def test_open_web_tables_page(elements_page):
    elements_page.web_tables_button_click()


def test_open_buttons_page(elements_page):
    elements_page.buttons_button_click()


def test_open_links_page(elements_page):
    elements_page.links_button_click()


def test_open_broken_page(elements_page):
    elements_page.broken_links_images_button_click()


def test_open_upload_download_page(elements_page):
    elements_page.upload_and_download_button_click()


def test_open_dynamic_properties_page(elements_page):
    elements_page.dynamic_properties_button_click()
