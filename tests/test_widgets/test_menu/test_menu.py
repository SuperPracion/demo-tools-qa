import allure


@allure.title('')
class TestMenuList:
    @allure.step('')
    def test_menu_item_1(self, menu_page):
        # TODO В родителя вынесен общий метод hover_over_element. Переписать
        menu_page.move_to_item(menu_page.get_main_item_1())
        assert menu_page.get_main_item_1().text == 'Main Item 1'

    @allure.step('')
    def test_menu_item_2(self, menu_page):
        menu_page.move_to_item(menu_page.get_main_item_2())
        assert menu_page.get_main_item_2().text == 'Main Item 2'

    @allure.step('')
    def test_menu_sub_item_1(self, menu_page):
        menu_page.move_to_item(menu_page.get_main_item_2())
        menu_page.move_to_item(menu_page.get_sub_item_1())
        assert menu_page.get_sub_item_1().text == 'Sub Item'

    @allure.step('')
    def test_menu_sub_item_2(self, menu_page):
        menu_page.move_to_item(menu_page.get_main_item_2())
        menu_page.move_to_item(menu_page.get_sub_item_2())
        assert menu_page.get_sub_item_2().text == 'Sub Item'

    @allure.step('')
    def test_menu_sub_sub_list(self, menu_page):
        menu_page.move_to_item(menu_page.get_main_item_2())
        menu_page.move_to_item(menu_page.get_sub_sub_list())
        assert menu_page.get_sub_sub_list().text == 'SUB SUB LIST »'

    @allure.step('')
    def test_menu_sub_sub_item_1(self, menu_page):
        menu_page.move_to_item(menu_page.get_main_item_2())
        menu_page.move_to_item(menu_page.get_sub_sub_list())
        menu_page.move_to_item(menu_page.get_sub_sub_item_1())
        assert menu_page.get_sub_sub_item_1().text == 'Sub Sub Item 1'

    @allure.step('')
    def test_menu_sub_sub_item_2(self, menu_page):
        menu_page.move_to_item(menu_page.get_main_item_2())
        menu_page.move_to_item(menu_page.get_sub_sub_list())
        menu_page.move_to_item(menu_page.get_sub_sub_item_2())
        assert menu_page.get_sub_sub_item_2().text == 'Sub Sub Item 2'

    @allure.step('')
    def test_menu_item_3(self, menu_page):
        menu_page.move_to_item(menu_page.get_main_item_3())
        assert menu_page.get_main_item_3().text == 'Main Item 3'
