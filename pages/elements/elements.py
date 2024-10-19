import settings
from base.driver import Driver
from selenium.webdriver.common.by import By


class Elements(Driver):
    def get_text_box_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Text Box')]/parent::*")

    def text_box_button_click(self):
        self.get_text_box_button().click()
        assert self.driver.current_url == f'{settings.MAIN_URL}/text-box'

    def get_checkbox_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Check Box')]/parent::*")

    def checkbox_button_click(self):
        self.get_checkbox_button().click()
        assert self.driver.current_url == f'{settings.MAIN_URL}/checkbox'

    def get_radio_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Radio Button')]/parent::*")

    def radio_button_click(self):
        self.get_radio_button().click()
        assert self.driver.current_url == f'{settings.MAIN_URL}/radio-button'

    def get_web_tables_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Web Tables')]/parent::*")

    def web_tables_button_click(self):
        self.get_web_tables_button().click()
        assert self.driver.current_url == f'{settings.MAIN_URL}/webtables'

    def get_buttons_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Buttons')]/parent::*")

    def buttons_button_click(self):
        self.get_buttons_button().click()
        assert self.driver.current_url == f'{settings.MAIN_URL}/buttons'

    def get_links_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Links')]/parent::*")

    def links_button_click(self):
        self.get_links_button().click()
        assert self.driver.current_url == f'{settings.MAIN_URL}/links'

    def get_broken_links_images_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Broken Links - Images')]/parent::*")

    def broken_links_images_button_click(self):
        self.get_broken_links_images_button().click()
        assert self.driver.current_url == f'{settings.MAIN_URL}/broken'

    def get_upload_and_download_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Upload and Download')]/parent::*")

    def upload_and_download_button_click(self):
        self.get_upload_and_download_button().click()
        assert self.driver.current_url == f'{settings.MAIN_URL}/upload-download'

    def get_dynamic_properties_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Dynamic Properties')]/parent::*")

    def dynamic_properties_button_click(self):
        self.get_dynamic_properties_button().click()
        assert self.driver.current_url == f'{settings.MAIN_URL}/dynamic-properties'
