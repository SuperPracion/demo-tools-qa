# test/conftest.py
import pytest
import allure
from selenium import webdriver

from base.user import User
from pages.main.main import Main
from pages.elements.elements import Elements
from pages.elements.text_box import TextBox


@pytest.fixture
def setup_user():
    user = User()
    yield user


@pytest.fixture
def setup_driver():
    # driver = webdriver.Edge()
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
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
