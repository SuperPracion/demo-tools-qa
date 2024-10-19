import pytest

from pages.main.main import Main
from pages.elements.elements import Elements
from pages.elements.text_box import TextBox


@pytest.fixture
def text_box(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.elements_button_click()
    elements = Elements(setup_driver)
    elements.text_box_button_click()
    text_box = TextBox(setup_driver)
    yield text_box


def test_filling_fullname(text_box):
    text_box.input_full_name('123')


def test_filling_email(text_box):
    text_box.input_email('123')


def test_filling_current_address(text_box):
    text_box.input_current_address('123')


def test_filling_permanent_address(text_box):
    text_box.input_permanent_address('123')


def test_all_fields_filling(text_box):
    text_box.input_full_name('Иванов')
    text_box.input_email('ivanov@gmail.com')
    text_box.input_current_address('Moscow')
    text_box.input_permanent_address('SPb')


def test_output_visualization(text_box):
    full_name = 'Ivanov Ivan Ivanovich'
    email = 'ivanov@gmail.com'
    current_address = 'Moscow'
    permanent_address = 'SPb'

    text_box.input_full_name(full_name)
    text_box.input_email(email)
    text_box.input_current_address(current_address)
    text_box.input_permanent_address(permanent_address)
    text_box.submit_button_click()
    text_box.output_field_check_values(full_name, email, current_address, permanent_address)
