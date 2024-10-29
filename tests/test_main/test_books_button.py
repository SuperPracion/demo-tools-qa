import allure

@allure.title('Test main page books button')
class TestMainPageBooksButton:
    @allure.step('check books button text')
    def test_books_button_text(self, main_page):
        button = main_page.get_books_button()
        assert button.text == 'Book Store Application'

    @allure.step('check books buttons link')
    def test_books_button_click(self, main_page):
        button = main_page.get_books_button()
        main_page.click(button)
        assert main_page.current_url == 'https://demoqa.com/books'
