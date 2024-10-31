import allure


@allure.title('')
class TestResizable:
    @allure.step('')
    def test_set_size_resizable_element_in_container(self, resizable_page):
        element = resizable_page.get_resizable_box_with_restriction()
        resizable_page.set_resizable_size(element, 300, 300)
        assert element.get_attribute('style') == 'width: 300px; height: 300px;'

    @allure.step('')
    def test_set_size_resizable_element(self, resizable_page):
        element = resizable_page.get_resizable()
        resizable_page.set_resizable_size(element, 100, 100)
        assert element.get_attribute('style') == 'width: 100px; height: 100px;'
