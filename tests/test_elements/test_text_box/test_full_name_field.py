import allure


@allure.title('TestFullNameField')
class TestFullNameField:
    @allure.step('check placeholder')
    def test_placeholder(self, text_box_page):
        field = text_box_page.get_full_name_field()
        assert field.get_attribute('placeholder') == 'Full Name'

    @allure.step('fulling full name digits')
    def test_filling_digits(self, text_box_page):
        field = text_box_page.get_full_name_field()
        text_box_page.input_text(field, 123)
        assert field.get_attribute('value') == '123'

    @allure.step('fulling full name lower str')
    def test_filling_lower_str(self, text_box_page):
        field = text_box_page.get_full_name_field()
        text_box_page.input_text(field, 'abc')
        assert field.get_attribute('value') == 'abc'

    @allure.step('fulling full name upper str')
    def test_filling_upper_str(self, text_box_page):
        # Как пример теста на поле TODO
        pass

    @allure.step('fulling full name en name')
    def test_fulling_en_full_name(self, text_box_page):
        field = text_box_page.get_full_name_field()
        text_box_page.input_text(field, 'Tim Cook')
        assert field.get_attribute('value') == 'Tim Cook'

    @allure.step('fulling full name ru name')
    def test_fulling_ru_full_name(self, text_box_page):
        field = text_box_page.get_full_name_field()
        text_box_page.input_text(field, 'Поворович Тимур Кухневич')
        assert field.get_attribute('value') == 'Поворович Тимур Кухневич'

    @allure.step('fulling full name special characters')
    def test_filling_special_characters(self, text_box_page):
        # Как пример теста на поле TODO
        pass

    @allure.step('fulling full name ch name')
    def test_fulling_ch_full_name(self, text_box_page):
        # Как пример теста на поле TODO
        pass

    @allure.step('fulling full name nones value')
    def test_fulling_none(self, text_box_page):
        # Как пример теста на поле TODO
        pass

    @allure.step('fulling full name sql injections')
    def test_fulling_sql_injection(self, text_box_page):
        # Как пример теста на поле TODO
        pass
