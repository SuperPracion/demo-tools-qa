import pytest
from selenium.webdriver.common.by import By

from pages.main.main import Main
from pages.widgets.widgets import Widgets
from pages.widgets.tool_tips import ToolTips


@pytest.fixture
def tool_tips(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.widgets_button_click()
    widgets = Widgets(setup_driver)
    widgets.tool_tips_button_click()
    tool_tips = ToolTips(setup_driver)
    yield tool_tips


def tool_tip_check(tool_tips):
    assert 'You hovered over the' in tool_tips.driver.find_element(By.XPATH, '//*[@class="tooltip-inner"]').text


def test_button_tool_tips(tool_tips):
    tool_tips.move_to_tool_tip_button()
    tool_tip_check(tool_tips)


def test_field_tool_tips(tool_tips):
    tool_tips.move_to_tools_tip_field()
    tool_tip_check(tool_tips)


def test_container_tool_tips(tool_tips):
    tool_tips.move_to_tools_tip_container_contrary()
    tool_tip_check(tool_tips)
    tool_tips.move_to_tools_tip_container_1_10_32()
    tool_tip_check(tool_tips)
