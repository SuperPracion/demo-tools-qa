import allure
from selenium.webdriver.common.by import By


@allure.title('')
class TestSelectableItems:
    @allure.step('')
    def test_select_item_in_list(self, selectable_page):
        list_button = selectable_page.get_demo_tab_list()
        selectable_page.click(list_button)
        item = selectable_page.get_group_item_by_text('Dapibus ac facilisis in')
        selectable_page.click(item)
        assert 'active' in item.get_attribute('class')
        assert len(selectable_page.driver.find_elements(By.XPATH,
                                                        '//*[@class="mt-2 list-group-item list-group-item-action"]')) == 3

    @allure.step('')
    def test_select_item_in_grid(self, selectable_page):
        grid_button = selectable_page.get_demo_tab_grid()
        selectable_page.click(grid_button)
        item = selectable_page.get_group_item_by_text('Five')
        selectable_page.click(item)
        assert 'active' in item.get_attribute('class')
        assert len(
            selectable_page.driver.find_elements(By.XPATH, '//*[@class="list-group-item list-group-item-action"]')) == 8
