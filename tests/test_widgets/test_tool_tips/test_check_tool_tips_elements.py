import allure
from selenium.webdriver.common.by import By


@allure.title('')
class TestToolTips:
    @allure.step('')
    def test_button_tool_tips(self, tool_tips_page):
        tip_button = tool_tips_page.get_tools_tip_button()
        tool_tips_page.hover_over_element(tip_button)
        assert 'You hovered over the' in tool_tips_page.driver.find_element(By.XPATH, '//*[@class="tooltip-inner"]').text

    @allure.step('')
    def test_field_tool_tips(self, tool_tips_page):
        tip_field = tool_tips_page.get_tools_tip_field()
        tool_tips_page.hover_over_element(tip_field)
        assert 'You hovered over the' in tool_tips_page.driver.find_element(By.XPATH, '//*[@class="tooltip-inner"]').text


    @allure.step('')
    def test_container_tool_tips(self, tool_tips_page):
        element = tool_tips_page.get_tools_tip_container().find_element(By.XPATH, '//*[contains(text(), "Contrary")]')
        tool_tips_page.hover_over_element(element)
        assert 'You hovered over the' in tool_tips_page.driver.find_element(By.XPATH, '//*[@class="tooltip-inner"]').text

        element = tool_tips_page.get_tools_tip_container().find_element(By.XPATH, '//*[contains(text(), "1.10.32")]')
        tool_tips_page.hover_over_element(element)
        assert 'You hovered over the' in tool_tips_page.driver.find_element(By.XPATH, '//*[@class="tooltip-inner"]').text
