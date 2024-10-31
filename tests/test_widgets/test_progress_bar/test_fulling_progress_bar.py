import allure

@allure.title
class TestProgressBar:
    @allure.step('')
    def test_25_percent_fulling(self, progress_bar_page):
        start_stop_button = progress_bar_page.get_start_stop_button()
        progress_bar = progress_bar_page.get_progress_bar()
        progress_bar_page.click(start_stop_button)
        while progress_bar.get_attribute('aria-valuenow') != '25':
            pass
        progress_bar_page.click(start_stop_button)
        assert progress_bar_page.get_progress_bar().text == '25%'

    @allure.step('')
    def test_50_percent_fulling(self, progress_bar_page):
        start_stop_button = progress_bar_page.get_start_stop_button()
        progress_bar = progress_bar_page.get_progress_bar()
        progress_bar_page.click(start_stop_button)
        while progress_bar.get_attribute('aria-valuenow') != '50':
            pass
        progress_bar_page.click(start_stop_button)
        assert progress_bar_page.get_progress_bar().text == '50%'

    @allure.step('')
    def test_100_percent_fulling(self, progress_bar_page):
        start_stop_button = progress_bar_page.get_start_stop_button()
        progress_bar = progress_bar_page.get_progress_bar()
        progress_bar_page.click(start_stop_button)
        while progress_bar.get_attribute('aria-valuenow') != '100':
            pass
        reset_button = progress_bar_page.get_reset_button()
        progress_bar_page.click(reset_button)
        assert progress_bar_page.get_progress_bar().text == '0%'
