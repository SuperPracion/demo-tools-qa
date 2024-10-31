import allure


@allure.title('')
class TestTabbing:
    @allure.title('open tab what')
    def test_open_what_tab(self, tabs_page):
        tab = tabs_page.get_what_tab()
        tabs_page.click(tab)
        assert tab.get_attribute('aria-selected') == 'true'

    @allure.title('open tab Origin')
    def test_open_origin_tab(self, tabs_page):
        tab = tabs_page.get_origin_tab()
        tabs_page.click(tab)
        assert tab.get_attribute('aria-selected') == 'true'

    @allure.title('open tab Use')
    def test_open_use_tab(self, tabs_page):
        tab = tabs_page.get_use_tab()
        tabs_page.click(tab)
        assert tab.get_attribute('aria-selected') == 'true'

    @allure.title('open tab More')
    def test_open_more_tab(self, tabs_page):
        tab = tabs_page.get_more_tab()
        tabs_page.click(tab)
        assert tab.is_enabled()
        # assert self.get_more_tab().get_attribute('aria-selected') == 'true'
