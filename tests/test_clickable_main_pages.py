from base.user import User
from pages.main.main import Main

from selenium import webdriver


def test_open_elements_page():
    user = User()
    driver = webdriver.Chrome()
    main_page = Main(user, driver)
    main_page.elements_button_click()
    driver.close()


def test_open_forms_page():
    user = User()
    driver = webdriver.Chrome()
    main_page = Main(user, driver)
    main_page.forms_buttons_click()
    driver.close()


def test_open_alerts_windows_page():
    user = User()
    driver = webdriver.Chrome()
    main_page = Main(user, driver)
    main_page.alerts_windows_button_click()
    driver.close()


def test_open_widgets_page():
    user = User()
    driver = webdriver.Chrome()
    main_page = Main(user, driver)
    main_page.widgets_button_click()
    driver.close()


def test_open_interaction_page():
    user = User()
    driver = webdriver.Chrome()
    main_page = Main(user, driver)
    main_page.interaction_button_click()
    driver.close()


def test_open_books_page():
    user = User()
    driver = webdriver.Chrome()
    main_page = Main(user, driver)
    main_page.book_button_click()
    driver.close()

def test_open_all_pages():
    user = User()
    driver = webdriver.Chrome()
    main_page = Main(user, driver)

    main_page.elements_button_click()
    main_page.driver.back()

    main_page.forms_buttons_click()
    main_page.driver.back()

    main_page.alerts_windows_button_click()
    main_page.driver.back()

    main_page.widgets_button_click()
    main_page.driver.back()

    main_page.interaction_button_click()
    main_page.driver.back()

    main_page.book_button_click()
    main_page.driver.back()

    driver.close()