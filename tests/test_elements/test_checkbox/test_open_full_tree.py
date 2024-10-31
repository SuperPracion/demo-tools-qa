import allure


@allure.title('')
class TestOpenTreeCatalogs:
    @allure.step('')
    def test_open_home(self, checkbox_page):
        home_toggle = checkbox_page.get_home_toggle()
        checkbox_page.click(home_toggle)
        # TODO добавить проверки

    @allure.step('')
    def test_select_home_checkbox(self, checkbox_page):
        home_checkbox = checkbox_page.get_home_checkbox()
        checkbox_page.click(home_checkbox)
        # TODO добавить проверки

    @allure.step('')
    def test_open_desktop(self, checkbox_page):
        home_toggle = checkbox_page.get_home_toggle()
        checkbox_page.click(home_toggle)
        desktop_toggle = checkbox_page.get_desktop_toggle()
        checkbox_page.click(desktop_toggle)
        # TODO добавить проверки

    @allure.step('')
    def test_select_desktop_checkbox(self, checkbox_page):
        home_toggle = checkbox_page.get_home_toggle()
        checkbox_page.click(home_toggle)
        desktop_toggle = checkbox_page.get_desktop_checkbox()
        checkbox_page.click(desktop_toggle)
        # TODO добавить проверки

    @allure.step('')
    def test_open_documents(self, checkbox_page):
        home_toggle = checkbox_page.get_home_toggle()
        checkbox_page.click(home_toggle)
        document_toggle = checkbox_page.get_documents_toggle()
        checkbox_page.click(document_toggle)
        # TODO добавить проверки

    @allure.step('')
    def test_select_documents_checkbox(self, checkbox_page):
        home_toggle = checkbox_page.get_home_toggle()
        checkbox_page.click(home_toggle)
        checkbox_document = checkbox_page.get_documents_checkbox()
        checkbox_page.click(checkbox_document)
        # TODO добавить проверки

    @allure.step('')
    def test_open_downloads(self, checkbox_page):
        home_toggle = checkbox_page.get_home_toggle()
        checkbox_page.click(home_toggle)
        download_toggle = checkbox_page.get_downloads_toggle()
        checkbox_page.click(download_toggle)
        # TODO добавить проверки

    @allure.step('')
    def test_select_downloads_checkbox(self, checkbox_page):
        home_toggle = checkbox_page.get_home_toggle()
        checkbox_page.click(home_toggle)
        checkbox_download = checkbox_page.get_downloads_checkbox()
        checkbox_page.click(checkbox_download)
        # TODO добавить проверки
