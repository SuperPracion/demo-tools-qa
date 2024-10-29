import allure


@allure.title('Test main page widgets button')
class TestMainPageWidgetsButton:
    @allure.step('check widgets button text')
    def test_widgets_button_text(self, main_page):
        button = main_page.get_widgets_button()
        assert button.text == 'Widgets'

    @allure.step('check widgets button link')
    def test_widgets_button_click(self, main_page):
        button = main_page.get_widgets_button()
        main_page.click(button)
        assert main_page.current_url == 'https://demoqa.com/widgets'
