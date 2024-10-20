# test/conftest.py
import pytest
from selenium import webdriver

from base.user import User


@pytest.fixture
def setup_user():
    user = User()
    yield user


@pytest.fixture
def setup_driver():
    #driver = webdriver.Edge()
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
