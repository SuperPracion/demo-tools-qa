from selenium.webdriver.common.by import By

from base.driver import Driver


class Accordian(Driver):
    def get_card_header_what_is_lorem(self):
        return self.driver.find_element(By.XPATH, '//*[@id="section1Heading"]')

    def get_card_header_where_does_it_come_from(self):
        return self.driver.find_element(By.XPATH, '//*[@id="section2Heading"]')

    def get_card_header_why_do_we_use_it(self):
        return self.driver.find_element(By.XPATH, '//*[@id="section3Heading"]')
