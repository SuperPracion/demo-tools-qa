import allure

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@allure.title('')
class TestAutoCompleteField:
    @allure.step('')
    def test_multiple_auto_complete(self, auto_complete_page):
        field = auto_complete_page.get_auto_complete_multiple_field()
        field.click()
        field.send_keys('Re')
        field.send_keys(Keys.ENTER)
        field.send_keys('Ye')
        assert auto_complete_page.driver.find_element(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div/div[1]/div[1]').text == 'Red'
        assert auto_complete_page.driver.find_element(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div/div[1]/div[2]').text == 'Yellow'

    @allure.step('')
    def test_single_auto_complete(self, auto_complete_page):
        field = auto_complete_page.get_auto_complete_single_field()
        field.click()
        field.send_keys('Re')
        field.send_keys(Keys.ENTER)
        field.send_keys(Keys.ENTER)
        assert auto_complete_page.driver.find_element(By.XPATH, '//*[@class="auto-complete__single-value css-1uccc91-singleValue"]').text == 'Red'
