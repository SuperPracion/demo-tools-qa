import allure
from selenium.webdriver.common.by import By


@allure.title('')
class TestSelectMenuValue:
    @allure.step('')
    def test_select_option_value(self, select_menu_page):
        value = 'Group 2, option 1'
        menu = select_menu_page.get_with_option_group_container()
        menu.select_container_value_by_text(value)
        assert select_menu_page.find_element(By.XPATH, '//*[@class=" css-1uccc91-singleValue"]').text == value

    @allure.step('')
    def test_select_one_title(self, select_menu_page):
        value = 'Mr.'
        menu = select_menu_page.get_select_one_container()
        menu.select_container_value_by_text(value)
        assert select_menu_page.find_element(By.XPATH, '//*[@class=" css-1uccc91-singleValue"]').text == value

    @allure.step('')
    def test_select_old_style_menu_value(self, select_menu_page):
        value = 'Black'
        menu = select_menu_page.get_old_select_container()
        menu.select_container_value_by_text(value)

    @allure.step('')
    def test_select_multiselect_drop_down_menu_value(self, select_menu_page):
        value = 'Green'
        menu = select_menu_page.get_multiselect_drop_down_container()
        menu.select_container_value_by_text(value, 2)
        assert select_menu_page.find_element(By.XPATH, '//*[@class="css-12jo7m5"]').text == value
