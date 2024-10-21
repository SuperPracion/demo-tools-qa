import pytest

from pages.main.main import Main
from pages.alerts_windows.alerts_windows import AlertsWindows
from pages.alerts_windows.frames import Frames


@pytest.fixture
def frames(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.alerts_windows_button_click()
    alerts_windows = AlertsWindows(setup_driver)
    alerts_windows.frames_button_click()
    frames = Frames(setup_driver)
    yield frames


def test_switch_to_frame1(frames):
    frames.switch_to_frame1()


def test_switch_to_from2(frames):
    frames.switch_to_frame2()