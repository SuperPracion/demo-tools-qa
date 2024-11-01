import allure
import pytest

from pages.alerts_windows.frames import Frames

@allure.step('open frame page')
@pytest.fixture
def frames_page(alerts_windows_page):
    alerts_windows_page.click(alerts_windows_page.get_frames_button())
    frames_page = Frames(alerts_windows_page.driver)
    yield frames_page


@allure.title('')
@allure.step('')
def test_switch_to_frame1(frames_page):
    frames_page.switch_to_frame1()


@allure.title('')
@allure.step('')
def test_switch_to_from2(frames_page):
    frames_page.switch_to_frame2()
