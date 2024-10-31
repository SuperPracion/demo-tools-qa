import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

@allure.title('')
class TestSortItems:
    @allure.step('')
    def test_list_items_sort(self, sortable_page):
        list_button = sortable_page.get_sortable_list()
        sortable_page.click(list_button)
        item_two = sortable_page.get_element_by_text_in_list('Two')
        action = ActionChains(sortable_page.driver)
        action.drag_and_drop_by_offset(item_two, 0, -45).perform()
        assert sortable_page.driver.find_element(By.XPATH, '//*[@class="vertical-list-container mt-4"]//*[@class="list-group-item list-group-item-action"]').text == 'Two'

    @allure.step('')
    def test_grid_items_sort(self, sortable_page):
        grid_button = sortable_page.get_sortable_grid()
        sortable_page.click(grid_button)
        item_nine = sortable_page.get_element_by_text_in_grid('Nine')
        action = ActionChains(sortable_page.driver)
        action.drag_and_drop_by_offset(item_nine, -666, -536).perform()
        assert sortable_page.driver.find_element(By.XPATH, '//*[@class="create-grid"]//*[@class="list-group-item list-group-item-action"]').text == 'Nine'