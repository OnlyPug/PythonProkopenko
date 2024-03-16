import time

from lesson21.pages.base_pages import BasePage
from lesson21.core import BasketLocators


class BasketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = BasketLocators()

    def this_page(self):
        elem = self.find_element(self.locators.locators_this_page)
        if elem:
            return True
        else:
            return False

    def product_chouse(self):
        self.find_element(self.locators.locators_product_check)

    def click_add_this_product(self):
        self.click_on_element(self.locators.locators_add_btn)

    def check_value_basket(self):
        value = self.check_value(self.locators.locators_check_text)
        return value

    def delete_this_product(self):
        self.click_on_element(self.locators.locators_back_to_product)
        return

    def click_back(self):
        time.sleep(5)
        self.find_element(self.locators.locators_back_to_product)
        self.click_on_element(self.locators.locators_back_to_product)

    def click_cross(self):
        time.sleep(5)
        self.find_element(self.locators.locators_cross_to_product)
        self.click_on_element(self.locators.locators_cross_to_product)



