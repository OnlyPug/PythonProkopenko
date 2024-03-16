from lesson21.pages.base_pages import BasePage
from lesson21.core import StrategyLocators
from lesson21.pages.product_page import ProductPage


class StrategyGamePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = StrategyLocators()
        self.driver = driver

    def this_page_strategy_game(self):
        elem = self.find_element(self.locators.locator_strategy_page)
        if elem:
            return True
        else:
            return False

    # Functionality for sort
    def click_lover_prise(self):
        self.click_on_element(self.locators.locator_lover_price)

    def click_max_prise(self):
        self.click_on_element(self.locators.locator_max_price)

    def load_page(self):
        self.wait_util_element_presents(self.locators.locator_wait_page)

    def wait_check_box(self):
        self.wait_util_element_presents(self.locators.locator_page_check_box)

    def click_popular(self):
        self.click_on_element(self.locators.locator_popular)

    def click_name(self):
        self.click_on_element(self.locators.locator_name)

    # Functionality for check box

    def click_on_check_box(self):
        self.scroll_to_element_and_click(self.locators.locator_check_box)

    def click_on_first_element(self):
        self.click_on_element(self.locators.locator_first_strategy_game)
        return ProductPage(self.driver)
