import allure
import pytest
from allure_commons.types import AttachmentType

from pages.alerts_windows.frames import Frames

@allure.step('open frame page')
@pytest.fixture
def frames_page(alerts_windows_page):
    alerts_windows_page.click(alerts_windows_page.get_frames_button())
    frames_page = Frames(alerts_windows_page.driver)
    yield frames_page


@allure.title('Test switch to page frame 1')
@allure.step('switch to frame 1')
def test_switch_to_frame1(frames_page):
    frames_page.switch_to_frame1()
    allure.attach(frames_page.driver.get_screenshot_as_png(), 'switch_to_frame1', AttachmentType.PNG)


@allure.title('Test switch to page frame 2')
@allure.step('switch to frame 2')
def test_switch_to_from2(frames_page):
    frames_page.switch_to_frame2()
    allure.attach(frames_page.driver.get_screenshot_as_png(), 'switch_to_from2', AttachmentType.PNG)
