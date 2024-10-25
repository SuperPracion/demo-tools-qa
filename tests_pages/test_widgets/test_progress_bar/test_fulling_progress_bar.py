import pytest

from pages.main.main import Main
from pages.widgets.widgets import Widgets
from pages.widgets.progress_bar import ProgressBar


@pytest.fixture
def progress_bar(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.widgets_button_click()
    widgets = Widgets(setup_driver)
    widgets.progress_dar_button_click()
    progress_bar = ProgressBar(setup_driver)
    yield progress_bar


def test_25_percent_fulling(progress_bar):
    progress_bar.start_stop_button_click()
    while progress_bar.get_progress_bar().get_attribute('aria-valuenow') != '25':
        pass
    progress_bar.start_stop_button_click()
    assert progress_bar.get_progress_bar().text == '25%'

def test_50_percent_fulling(progress_bar):
    progress_bar.start_stop_button_click()
    while progress_bar.get_progress_bar().get_attribute('aria-valuenow') != '50':
        pass
    progress_bar.start_stop_button_click()
    assert progress_bar.get_progress_bar().text == '50%'

def test_100_percent_fulling(progress_bar):
    progress_bar.start_stop_button_click()
    while progress_bar.get_progress_bar().get_attribute('aria-valuenow') != '100':
        pass
    progress_bar.rest_button_click()
    assert progress_bar.get_progress_bar().text == '0%'
