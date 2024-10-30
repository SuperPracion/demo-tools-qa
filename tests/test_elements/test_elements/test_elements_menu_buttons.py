import allure

import settings


@allure.title('Test left side elements menu buttons')
class TestElementsMenuButtons:
    @allure.step('check text box link verification')
    def test_open_text_box_page(self, elements_page):
        button = elements_page.get_text_box_button()
        elements_page.click(button)
        assert elements_page.current_url == f'{settings.MAIN_URL}/text-box'

    @allure.step('check check box link verification')
    def test_open_check_box_page(self, elements_page):
        button = elements_page.get_checkbox_button()
        elements_page.click(button)
        assert elements_page.current_url == f'{settings.MAIN_URL}/checkbox'

    @allure.step('check radio button link verification')
    def test_open_radio_button_page(self, elements_page):
        button = elements_page.get_radio_button()
        elements_page.click(button)
        assert elements_page.current_url == f'{settings.MAIN_URL}/radio-button'

    @allure.step('check web tables link verification')
    def test_open_web_tables_page(self, elements_page):
        button = elements_page.get_web_tables_button()
        elements_page.click(button)
        assert elements_page.current_url == f'{settings.MAIN_URL}/webtables'

    @allure.step('check open buttons link verification')
    def test_open_buttons_page(self, elements_page):
        button = elements_page.get_buttons_button()
        elements_page.click(button)
        assert elements_page.current_url == f'{settings.MAIN_URL}/buttons'

    @allure.step('check links link verification')
    def test_open_links_page(self, elements_page):
        button = elements_page.get_links_button()
        elements_page.click(button)
        assert elements_page.current_url == f'{settings.MAIN_URL}/links'

    @allure.step('check broken link verification')
    def test_open_broken_page(self, elements_page):
        button = elements_page.get_broken_links_images_button()
        elements_page.click(button)
        assert elements_page.current_url == f'{settings.MAIN_URL}/broken'

    @allure.step('check upload download link verification')
    def test_open_upload_download_page(self, elements_page):
        button = elements_page.get_upload_and_download_button()
        elements_page.click(button)
        assert elements_page.current_url == f'{settings.MAIN_URL}/upload-download'

    @allure.step('check dynamic properties link verification')
    def test_open_dynamic_properties_page(self, elements_page):
        button = elements_page.get_dynamic_properties_button()
        elements_page.click(button)
        assert elements_page.current_url == f'{settings.MAIN_URL}/dynamic-properties'
