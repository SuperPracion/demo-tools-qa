import allure


@allure.title('Test main page forms button')
class TestMainPageFormsButton:
    @allure.step('check forms button text')
    def test_forms_button_text(self, main_page):
        button = main_page.get_forms_button()
        assert button.text == 'Forms'

    @allure.step('check forms button link')
    def test_forms_button_click(self, main_page):
        button = main_page.get_forms_button()
        main_page.click(button)
        assert main_page.current_url == 'https://demoqa.com/forms'
