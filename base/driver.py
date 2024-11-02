import allure
import os.path
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Driver:
    """
    Описание: Базовый класс для страниц. В класс вынесены общие действия.
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 2)

    @property
    def current_url(self):
        return self.driver.current_url

    @allure.step('touch element')
    def click(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step('write text into')
    def input_text(self, element, text):
        self.wait.until(expected_conditions.visibility_of(element)).send_keys(text)

    def get_element_text(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).text

    @allure.step('scroll to element')
    def scroll_to_element(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def get_alert(self):
        alert = self.wait.until(expected_conditions.alert_is_present())
        return alert

    @allure.step('alert accept')
    def accept_alert(self):
        alert = self.wait.until(expected_conditions.alert_is_present())
        alert.accept()

    @allure.step('alert dismiss')
    def dismiss_alert(self):
        alert = self.wait.until(expected_conditions.alert_is_present())
        alert.dismiss()

    @allure.step('hover over to element')
    def hover_over_element(self, element):
        element = self.wait.until(expected_conditions.visibility_of(element))
        ActionChains(self.driver).move_to_element(element)

    @allure.step('save screenshot')
    def save_screenshot(self, name=None, dir='screenshots'):
        if not name:
            name = self.driver.current_url

        timestamp = datetime.now().strftime('%Y%m%d %H:%M:%S')
        screen_path = os.path.join(dir, f'{name} {timestamp}.png')

        self.driver.save_screenshot(screen_path)

        with open(screen_path, 'rb') as image_file:
            allure.attach(image_file.read(), name=f'{name} {timestamp}', attachment_type=allure.attachment_type.PNG)
