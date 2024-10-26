import pytest

from pages.main.main import Main
from pages.widgets.widgets import Widgets
from pages.widgets.slider import Slider

@pytest.fixture
def slider(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.widgets_button_click()
    widgets = Widgets(setup_driver)
    widgets.slider_button_click()
    slider = Slider(setup_driver)
    yield slider


def test_set_value_to_field(slider):
    slider.set_slider_field_value(-80)
    assert slider.get_range_slider().get_attribute('value') == '25'


def test_move_slider(slider):
    slider.set_range_slider_value(80)
    assert slider.get_slider_field().get_attribute('value') == '69'