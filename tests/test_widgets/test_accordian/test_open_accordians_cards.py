import allure

from selenium.webdriver.common.by import By


@allure.title('')
class TestAccordianCards:
    @allure.step('')
    def test_what_is_lorem_open(self, accordian_page):
        card = accordian_page.get_card_header_what_is_lorem()
        accordian_page.click(card)
        assert accordian_page.driver.find_element(By.XPATH, '//*[@id="section1Content"]').text

    @allure.step('')
    def test_where_does_it_come_from_open(self, accordian_page):
        card = accordian_page.get_card_header_where_does_it_come_from()
        accordian_page.click(card)
        assert accordian_page.driver.find_element(By.XPATH, '//*[@id="section2Content"]/p').text

    @allure.step('')
    def test_why_do_we_use_it(self, accordian_page):
        card = accordian_page.get_card_header_why_do_we_use_it()
        accordian_page.click(card)
        assert accordian_page.driver.find_element(By.XPATH, '//*[@id="section3Content"]/p').text
