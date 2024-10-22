import pytest

from pages.main.main import Main
from pages.alerts_windows.alerts_windows import AlertsWindows
from pages.alerts_windows.nestedframes import NestedFrames


@pytest.fixture
def nestedframes(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.alerts_windows_button_click()
    alerts_windows = AlertsWindows(setup_driver)
    alerts_windows.nested_frames_click()
    nestedframes = NestedFrames(setup_driver)
    yield nestedframes


def test_switch_to_parent_frame(nestedframes):
    nestedframes.switch_to_parent_frame()


def test_switch_to_child_frame(nestedframes):
    nestedframes.switch_to_child_frame()
