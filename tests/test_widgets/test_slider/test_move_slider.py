import allure

from selenium.webdriver.common.action_chains import ActionChains


@allure.title('')
class TestMoveSlider:
    @allure.step('')
    def test_set_value_to_field(self, slider_page):
        slider = slider_page.get_slider_field()
        slider_page.input_text(slider, -80)
        assert slider_page.get_range_slider().get_attribute('value') == '25'

    @allure.step('')
    def test_move_slider(self, slider_page):
        mover = ActionChains(slider_page.driver)
        slider = slider_page.get_range_slider()
        mover.click_and_hold(slider).move_by_offset(80, 0).release().perform()
        assert slider_page.get_slider_field().get_attribute('value') == '69'
