# test/conftest.py
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from base.user import User
from pages.main.main import Main

from pages.elements.elements import Elements
from pages.elements.text_box import TextBox
from pages.elements.checkbox import CheckBox

from pages.interaction.interaction import Interaction
from pages.interaction.resizable import Resizable
from pages.interaction.selectable import Selectable
from pages.interaction.sortable import Sortable

from pages.widgets.widgets import Widgets
from pages.widgets.accordian import Accordian
from pages.widgets.auto_complete import AutoComplete
from pages.widgets.date_picker import DatePicker
from pages.widgets.menu import Menu
from pages.widgets.progress_bar import ProgressBar
from pages.widgets.select_menu import SelectMenu
from pages.widgets.slider import Slider
from pages.widgets.tabs import Tabs
from pages.widgets.tool_tips import ToolTips

from pages.alerts_windows.alerts_windows import AlertsWindows


@pytest.fixture
def setup_user():
    user = User()
    yield user


@pytest.fixture
def setup_driver():
    options = Options()
    options.add_argument('--headless')
    # driver = webdriver.Edge()
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture
def main_page(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    yield main_page


@allure.step('open elements page')
@pytest.fixture
def elements_page(main_page):
    main_page.click(main_page.get_elements_button())
    elements_page = Elements(main_page.driver)
    yield elements_page


@allure.step('open text box page')
@pytest.fixture
def text_box_page(elements_page):
    elements_page.click(elements_page.get_text_box_button())
    text_box = TextBox(elements_page.driver)
    yield text_box


@allure.step('open checkbox page')
@pytest.fixture
def checkbox_page(elements_page):
    elements_page.click(elements_page.get_checkbox_button())
    checkbox = CheckBox(elements_page.driver)
    yield checkbox


@allure.step('open interactions page')
@pytest.fixture
def interactions_page(main_page):
    main_page.click(main_page.get_interactions_button())
    interactions_page = Interaction(main_page.driver)
    yield interactions_page


@allure.step('open interactions page')
@pytest.fixture
def resizable_page(interactions_page):
    interactions_page.click(interactions_page.get_resizable_button())
    resizable_page = Resizable(interactions_page.driver)
    yield resizable_page


@allure.step('open selectable page')
@pytest.fixture
def selectable_page(interactions_page):
    interactions_page.click(interactions_page.get_selectable_button())
    selectable_page = Selectable(interactions_page.driver)
    yield selectable_page


@allure.step('open sortable page')
@pytest.fixture
def sortable_page(interactions_page):
    interactions_page.click(interactions_page.get_sortable_button())
    sortable_page = Sortable(interactions_page.driver)
    yield sortable_page


@allure.step('open widgets page')
@pytest.fixture
def widgets_page(main_page):
    main_page.click(main_page.get_widgets_button())
    widgets_page = Widgets(main_page.driver)
    yield widgets_page


@allure.step('open accordian page')
@pytest.fixture
def accordian_page(widgets_page):
    widgets_page.click(widgets_page.get_accordian_button())
    accordian_page = Accordian(widgets_page.driver)
    yield accordian_page


@allure.step('open auto-complete page')
@pytest.fixture
def auto_complete_page(widgets_page):
    widgets_page.click(widgets_page.get_auto_complete_button())
    auto_complete_page = AutoComplete(widgets_page.driver)
    yield auto_complete_page


@allure.step('open date picker page')
@pytest.fixture
def date_picker_page(widgets_page):
    widgets_page.click(widgets_page.get_date_picker_button())
    date_picker_page = DatePicker(widgets_page.driver)
    yield date_picker_page


@allure.step('open menu page')
@pytest.fixture
def menu_page(widgets_page):
    widgets_page.click(widgets_page.get_menu_button())
    menu_page = Menu(widgets_page.driver)
    yield menu_page


@allure.step('open progress bar page')
@pytest.fixture
def progress_bar_page(widgets_page):
    widgets_page.click(widgets_page.get_progress_bar_button())
    progress_bar_page = ProgressBar(widgets_page.driver)
    yield progress_bar_page


@allure.step('open select menu page')
@pytest.fixture
def select_menu_page(widgets_page):
    widgets_page.click(widgets_page.get_select_menu_button())
    select_menu_page = SelectMenu(widgets_page.driver)
    yield select_menu_page


@allure.step('open slider page')
@pytest.fixture
def slider_page(widgets_page):
    widgets_page.click(widgets_page.get_slider_button())
    slider_page = Slider(widgets_page.driver)
    yield slider_page


@allure.step('open tabs page')
@pytest.fixture
def tabs_page(widgets_page):
    widgets_page.click(widgets_page.get_tabs_button())
    tabs_page = Tabs(widgets_page.driver)
    yield tabs_page


@allure.step('open tool tips page')
@pytest.fixture
def tool_tips_page(widgets_page):
    widgets_page.click(widgets_page.get_tools_tips_button())
    tool_tips_page = ToolTips(widgets_page.driver)
    yield tool_tips_page


@allure.step('open alert page')
@pytest.fixture
def alerts_windows_page(main_page):
    main_page.click(main_page.get_alerts_windows_button())
    alerts_windows_page = AlertsWindows(main_page.driver)
    yield alerts_windows_page
