import pytest

from pages.main.main import Main
from pages.widgets.widgets import Widgets
from pages.widgets.date_picker import DatePicker

@pytest.fixture
def date_picker(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.widgets_button_click()
    widgets = Widgets(setup_driver)
    widgets.date_picker_button_click()
    date_picker = DatePicker(setup_driver)
    yield date_picker

def test_set_month_and_year(date_picker):
    date_picker.set_date_picker_mont_year('12', '12', '1999')

def test_set_day_month_and_year(date_picker):
    date_picker.set_date_and_time_picker('01', '02', '2003', '07', '30')