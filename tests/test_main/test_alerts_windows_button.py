import allure


@allure.title('Test main page alerts windows button')
class TestMainPageAlertsWindowsButton:
    @allure.step('check alerts windows button text')
    def test_alerts_windows_button_text(self, main_page):
        button = main_page.get_alerts_windows_button()
        assert button.text == 'Alerts, Frame & Windows'

    @allure.step('check alerts windows button link')
    def test_alerts_windows_button_click(self, main_page):
        button = main_page.get_alerts_windows_button()
        main_page.click(button)
        assert main_page.current_url == 'https://demoqa.com/alertsWindows'
