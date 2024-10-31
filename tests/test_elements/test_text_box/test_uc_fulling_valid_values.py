import allure
from selenium.webdriver.common.by import By


@allure.title('')
class TestUCFullingValidValues:
    @allure.step('')
    def test_fulling_valid_values(self, text_box_page):
        full_name = 'Ivanov Ivan Ivanovich'
        email = 'ivanov@gmail.com'
        current_address = 'Moscow'
        permanent_address = 'SPb'

        full_name_field = text_box_page.get_full_name_field()
        email_field = text_box_page.get_email_field()
        current_address_field = text_box_page.get_current_address_field()
        permanent_address_field = text_box_page.get_permanent_address_field()
        submit_button = text_box_page.get_submit_button()
        output_field = text_box_page.get_output_field()

        text_box_page.input_text(full_name_field, full_name)
        text_box_page.input_text(email_field, email)
        text_box_page.input_text(current_address_field, current_address)
        text_box_page.input_text(permanent_address_field, permanent_address)
        text_box_page.click(submit_button)

        assert output_field.find_element(By.XPATH, '//*[@id="name"]').text == f'Name:{full_name}'
        assert output_field.find_element(By.XPATH, '//*[@id="email"]').text == f'Email:{email}'
        assert output_field.find_element(By.XPATH, '//p[@id="currentAddress"]').text == f'Current Address :{current_address}'
        assert output_field.find_element(By.XPATH,'//p[@id="permanentAddress"]').text == f'Permananet Address :{permanent_address}'

