import allure


@allure.title('Test email field filling')
class TestEmailFiled:
    @allure.step('check placeholder')
    def test_placeholder(self, text_box_page):
        field = text_box_page.get_email_field()
        assert field.get_attribute('placeholder') == 'name@example.com'

    @allure.step('check fulling digits')
    def test_filling_digits(self, text_box_page):
        field = text_box_page.get_email_field()
        text_box_page.input_text(field, 123)
        assert field.get_attribute('value') == '123'

    @allure.step('check fulling lower str')
    def test_filling_lower_str(self, text_box_page):
        field = text_box_page.get_email_field()
        text_box_page.input_text(field, 'zxc')
        assert field.get_attribute('value') == 'zxc'

    @allure.step('check fulling upper')
    def test_filling_upper_str(self, text_box_page):
        # Как пример тесла TODO
        pass

    @allure.step('check fulling en email')
    def test_filling_en_email(self, text_box_page):
        field = text_box_page.get_email_field()
        text_box_page.input_text(field, 'timcook@gmail.com')
        assert field.get_attribute('value') == 'timcook@gmail.com'

    @allure.step('check fulling ru email')
    def test_filling_ru_email(self, text_box_page):
        # Как пример, если валидация на поле идёт сразу
        pass
