import allure


@allure.title('Test all modules buttons')
class TestAllMainPageModuleButtons:
    @allure.step('check elements button with go back')
    def test_elements_module(self, main_page):
        main_page.click(main_page.get_elements_button())
        main_page.driver.back()
        assert main_page.current_url == 'https://demoqa.com/'

    @allure.step('check forms button with go back')
    def test_forms_module(self, main_page):
        main_page.click(main_page.get_forms_button())
        main_page.driver.back()
        assert main_page.current_url == 'https://demoqa.com/'

    @allure.step('check alerts button with go back')
    def test_alerts_windows_module(self, main_page):
        main_page.click(main_page.get_alerts_windows_button())
        main_page.driver.back()
        assert main_page.current_url == 'https://demoqa.com/'

    @allure.step('check widgets button with go back')
    def test_widgets_module(self, main_page):
        main_page.click(main_page.get_widgets_button())
        main_page.driver.back()
        assert main_page.current_url == 'https://demoqa.com/'

    @allure.step('check interactions button with go back')
    def test_interactions_module(self, main_page):
        main_page.click(main_page.get_interactions_button())
        main_page.driver.back()
        assert main_page.current_url == 'https://demoqa.com/'

    @allure.step('check books button with go back')
    def test_books_module(self, main_page):
        main_page.click(main_page.get_books_button())
        main_page.driver.back()
        assert main_page.current_url == 'https://demoqa.com/'
