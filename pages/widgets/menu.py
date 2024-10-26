from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from base.driver import Driver


class Menu(Driver):
    # Все имена - это оригинал элементов ресурса.
    def get_main_item_1(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(), "Main Item 1")]')

    def get_main_item_2(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(), "Main Item 2")]')

    def get_sub_item_1(self):
        return self.driver.find_element(By.XPATH, '(//*[contains(text(), "Sub Item")])[1]')

    def get_sub_item_2(self):
        return self.driver.find_element(By.XPATH, '(//*[contains(text(), "Sub Item")])[2]')

    def get_sub_sub_list(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(), "SUB SUB LIST »")]')

    def get_sub_sub_item_1(self):
        return self.driver.find_element(By.XPATH, '//a[contains(text(), "Sub Sub Item 1")]')

    def get_sub_sub_item_2(self):
        return self.driver.find_element(By.XPATH, '//a[contains(text(), "Sub Sub Item 2")]')

    def get_main_item_3(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(), "Main Item 3")]')

    def move_to_item(self, element):
        ActionChains(self.driver).move_to_element(element).perform()
