import allure


@allure.title('Test main page interactions button')
class TestMainPageInteractionsButton:
    @allure.step('check interactions button text')
    def test_interactions_button_text(self, main_page):
        button = main_page.get_interactions_button()
        assert button.text == 'Interactions'

    @allure.step('check interactions button link')
    def test_interaction_button_click(self, main_page):
        button = main_page.get_interactions_button()
        main_page.click(button)
        assert main_page.current_url == 'https://demoqa.com/interaction'
