import pytest
from selenium.webdriver.common.by import By

from pages.main.main import Main
from pages.interaction.interaction import Interaction
from pages.interaction.selectable import Selectable


@pytest.fixture
def selectable(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.interaction_button_click()
    interaction = Interaction(setup_driver)
    interaction.selectable_button_click()
    selectable = Selectable(setup_driver)
    yield selectable


def test_select_item_in_list(selectable):
    selectable.demo_tab_list_click()
    item = selectable.get_group_item_by_text('Dapibus ac facilisis in')
    item.click()
    assert 'active' in item.get_attribute('class')
    assert len(selectable.driver.find_elements(By.XPATH, '//*[@class="mt-2 list-group-item list-group-item-action"]')) == 3

def test_select_item_in_grid(selectable):
    selectable.demo_tab_grid_click()
    item = selectable.get_group_item_by_text('Five')
    item.click()
    assert 'active' in item.get_attribute('class')
    assert len(selectable.driver.find_elements(By.XPATH, '//*[@class="list-group-item list-group-item-action"]')) == 8
