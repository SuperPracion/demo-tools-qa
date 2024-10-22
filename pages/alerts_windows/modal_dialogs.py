from selenium.webdriver.common.by import By

from base.driver import Driver

small_modal_text = "This is a small modal. It has very less content"
large_modal_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."


class ModalDialogs(Driver):
    def get_small_modal_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='showSmallModal']")

    def small_modal_button_click(self):
        self.get_small_modal_button().click()
        assert self.driver.find_element(By.XPATH, '//*[@class="modal-content"]')
        assert self.driver.find_element(By.XPATH, '//*[@class="modal-body"]').text == small_modal_text

    def get_large_modal_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='showLargeModal']")

    def large_modal_button_click(self):
        self.get_large_modal_button().click()
        assert self.driver.find_element(By.XPATH, '//*[@class="modal-content"]')
        assert self.driver.find_element(By.XPATH, '//*[@class="modal-body"]/p').text == large_modal_text

    def get_close_button(self):
        return self.driver.find_element(By.XPATH, "//button[contains(text(), 'Close')]")

    def close_button_click(self):
        self.get_close_button().click()

    def get_small_close_button(self):
        return self.driver.find_element(By.XPATH, "//button[@class='close']")

    def small_button_close_click(self):
        self.get_small_close_button().click()
