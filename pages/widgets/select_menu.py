from selenium.webdriver.common.by import By

from base.driver import Driver


class SelectMenu(Driver):
    def get_with_option_group_container(self):
        return self.driver.find_element(By.XPATH, '//*[@id="withOptGroup"]')

    def click_with_option_group_container(self):
        self.get_with_option_group_container().click()

    def get_select_one_container(self):
        return self.driver.find_element(By.XPATH, '//*[@id="selectOne"]')

    def click_select_one_container(self):
        self.get_select_one_container().click()

    def get_old_select_container(self):
        return self.driver.find_element(By.XPATH, '//*[@id="oldSelectMenu"]')

    def click_old_select_container(self):
        self.get_old_select_container().click()

    def get_multiselect_drop_down_container(self):
        return self.driver.find_element(By.XPATH, '(//*[@class=" css-yk16xz-control"])[3]')

    def click_multi_drop_down_container(self):
        self.get_multiselect_drop_down_container().click()

    def select_container_value_by_text(self, value, pos=1):
        self.driver.find_element(By.XPATH, f'(//*[contains(text(), "{value}")])[{pos}]').click()
