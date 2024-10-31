import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from base.element_found_exception import ElementFoundException


@allure.title('')
class TestUCFullingInvalidValues:
    @allure.step('')
    def test_uc_fulling_invalid_values(self, text_box_page):
        full_name = '   '
        email = '!@#'
        current_address = ''
        permanent_address = ''

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

        try:
            text_box_page.driver.find_element(By.XPATH, '//*[@id="output"]/div/p')
            raise ElementFoundException
        except NoSuchElementException:
            pass
