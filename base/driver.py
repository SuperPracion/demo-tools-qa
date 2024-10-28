import os.path
from datetime import datetime

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Driver:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).text

    def scroll_to_element(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def get_alert(self):
        alert = self.wait.until(expected_conditions.alert_is_present())
        return alert

    def accept_alert(self):
        alert = self.wait.until(expected_conditions.alert_is_present())
        alert.accept()

    def dismiss_alert(self):
        alert = self.wait.until(expected_conditions.alert_is_present())
        alert.dismiss()

    def hover_over_element(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element)

    def save_screenshot(self, name=None, dir='screenshots'):
        if not name:
            name = self.driver.current_url

        timestamp = datetime.now().strftime('%Y%m%d %H:%M:%S')
        screen_path = os.path.join(dir, f'{name} {timestamp}.png')

        self.driver.save_screenshot(screen_path)

        with open(screen_path, 'rb') as image_file:
            allure.attach(image_file.read(), name=f'{name} {timestamp}', attachment_type=allure.attachment_type.PNG)
