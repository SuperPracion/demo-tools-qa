from selenium.webdriver.common.by import By

from tests.conftest import *
from pages.main.main import Main
from pages.alerts_windows.alerts_windows import AlertsWindows
from pages.alerts_windows.nestedframes import NestedFrames


@allure.title('')
def test_switch_to_parent_frame(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.click(main_page.get_alerts_windows_button())
    alerts_windows = AlertsWindows(main_page.driver)
    alerts_windows.nested_frames_click()

    nestedframes = NestedFrames(alerts_windows.driver)
    frame = nestedframes.get_parent_frame()
    nestedframes.driver.switch_to.frame(frame)

    assert nestedframes.driver.find_element(By.XPATH, '//body').text == 'Parent frame'


@allure.title('')
def test_switch_to_child_frame(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.click(main_page.get_alerts_windows_button())
    alerts_windows = AlertsWindows(main_page.driver)
    alerts_windows.nested_frames_click()

    nestedframes = NestedFrames(alerts_windows.driver)
    parent_frame = nestedframes.get_parent_frame()
    nestedframes.driver.switch_to.frame(parent_frame)

    child_frame = nestedframes.get_child_frame()
    nestedframes.driver.switch_to.frame(child_frame)

    assert nestedframes.driver.find_element(By.XPATH, '//body').text == 'Child Iframe'
