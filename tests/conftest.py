# test/conftest.py
import pytest
from selenium import webdriver

from base.user import User
from pages.main.main import Main


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
