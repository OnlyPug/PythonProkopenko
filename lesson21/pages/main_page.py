from lesson21.pages.base_pages import BasePage
from lesson21.pages.strategy_game_page import StrategyGamePage
from lesson21.core import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = MainPageLocators()

    def this_main_page(self):
        elem = self.find_element(self.locator.locator_strategy)
        if elem:
            return True
        else:
            return False

    def click_strategy(self):
        self.click_on_element(self.locator.locator_strategy)
        return StrategyGamePage(self.driver)
