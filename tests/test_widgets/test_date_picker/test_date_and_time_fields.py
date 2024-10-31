import allure

from selenium.webdriver.common.keys import Keys

@allure.title('')
class TestDateTimeField:
    @allure.step('')
    def test_set_month_and_year(self, date_picker_page):
        field = date_picker_page.get_date_picker_month_year_input()
        field.click()
        field.send_keys(Keys.CONTROL + 'a')
        field.send_keys(Keys.BACKSPACE)
        field.send_keys('12/12/1999')
        field.send_keys(Keys.ENTER)
        assert field.get_attribute('value') == '12/12/1999'

    @allure.step('')
    def test_set_day_month_and_year(self, date_picker_page):
        field = date_picker_page.get_date_and_time_picker_input()
        field.click()
        field.send_keys(Keys.CONTROL + 'a')
        field.send_keys(Keys.BACKSPACE)
        field.send_keys('01/02/2003 07:30')
        field.send_keys(Keys.ENTER)
        assert date_picker_page.get_date_and_time_picker_input().get_attribute('value') == 'January 2, 2003 7:30 AM'
