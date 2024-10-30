from base.driver import Driver
from selenium.webdriver.common.by import By


class Elements(Driver):
    def get_text_box_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Text Box')]/parent::*")

    def get_checkbox_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Check Box')]/parent::*")

    def get_radio_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Radio Button')]/parent::*")

    def get_web_tables_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Web Tables')]/parent::*")

    def get_buttons_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Buttons')]/parent::*")

    def get_links_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Links')]/parent::*")

    def get_broken_links_images_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Broken Links - Images')]/parent::*")

    def get_upload_and_download_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Upload and Download')]/parent::*")

    def get_dynamic_properties_button(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Dynamic Properties')]/parent::*")
