import allure


@allure.title('Test main page module buttons')
class TestMainPageElementsButton:
    @allure.step('check elements button text')
    def test_element_button_text(self, main_page):
        button = main_page.get_elements_button()
        assert button.text == 'Elements'

    @allure.step('check element button link')
    def test_element_button_click(self, main_page):
        button = main_page.get_elements_button()
        main_page.click(button)
        assert main_page.current_url == 'https://demoqa.com/elements'
