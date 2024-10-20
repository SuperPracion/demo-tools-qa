from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver


class Driver:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # TODO
    @property
    def get_current_url(self):
        # TODO Задушить или доработать
        """Бесполезный Метод получения текущй URL страницы"""
        return self.driver.current_url

    def check_text_on_page(self, text):
        """ Проверка наличия текста на страницы"""
        assert self.driver.find_element(By.XPATH, f'//*[contains(text(), "{text}")]')

    def create_screenshot(self,
                          path='C:\\Users\\Lenovo\\PycharmProjects\\demo-tools-qa\\tests',
                          name=f'screenshot{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}',
                          extension='png'):
        self.driver.get_screenshot_as_file(f'{path}{name}.{extension}')
