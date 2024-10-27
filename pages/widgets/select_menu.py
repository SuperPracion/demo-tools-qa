from selenium.webdriver.common.by import By

from base.driver import Driver


class SelectMenu(Driver):
    def get_with_option_group_container(self):
        return self.driver.find_element(By.XPATH, '//*[@id="withOptGroup"]')

    def get_select_one_container(self):
        return self.driver.find_element(By.XPATH, '//*[@id="selectOne"]')

    def get_old_select_container(self):
        self.driver.find_element(By.XPATH, '//*[@id="oldSelectMenu"]')

    def get_multiselect_drop_down_container(self):
        return self.driver.find_element(By.XPATH, '(//*[@class=" css-yk16xz-control"])[3]')

    def select_container_value_by_text(self, value):
        self.driver.find_element(By.XPATH, f'//*[contains(text(), "{value}")]').click()
