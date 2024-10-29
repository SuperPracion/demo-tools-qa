# test/conftest.py
import pytest
import allure
from selenium import webdriver

from base.user import User
from pages.main.main import Main
from pages.elements.elements import Elements


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


@pytest.fixture
@allure.step('open elements page')
def elements_page(main_page):
    main_page.click(main_page.get_elements_button())
    elements_page = Elements(main_page.driver)
    yield elements_page
