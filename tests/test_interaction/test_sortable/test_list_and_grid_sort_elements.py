import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.main.main import Main
from pages.interaction.interaction import Interaction
from pages.interaction.sortable import Sortable


@pytest.fixture
def sortable(setup_user, setup_driver):
    main_page = Main(setup_user, setup_driver)
    main_page.interaction_button_click()
    interaction = Interaction(setup_driver)
    interaction.sortable_button_click()
    sortable = Sortable(setup_driver)
    yield sortable


def test_list_items_sort(sortable):
    item_two = sortable.get_element_by_text_in_list('Two')
    action = ActionChains(sortable.driver)
    action.drag_and_drop_by_offset(item_two, 0, -40).perform()
    assert sortable.driver.find_element(By.XPATH, '//*[@class="vertical-list-container mt-4"]//*[@class="list-group-item list-group-item-action"]').text == 'Two'


def test_grid_items_sort(sortable):
    sortable.click_sortable_grid()
    item_nine = sortable.get_element_by_text_in_grid('Nine')
    action = ActionChains(sortable.driver)
    action.drag_and_drop_by_offset(item_nine, -666, -536).perform()
    assert sortable.driver.find_element(By.XPATH, '//*[@class="create-grid"]//*[@class="list-group-item list-group-item-action"]').text == 'Nine'