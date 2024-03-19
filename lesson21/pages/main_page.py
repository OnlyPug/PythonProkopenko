from lesson21.pages.base_pages import BasePage
from lesson21.pages.strategy_game_page import StrategyGamePage
from lesson21.pages.header_page import HeaderPage
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

    # COOKIES
    def cookies_main_page(self):
        self.get_cookies()

    def add_cookies_main_page(self, cookie_dict):
        self.add_cookies(cookie_dict)
        self.get_cookies()

    # LOCAL STORAGE

    def add_or_change_local_storage_main_page(self, name, value):
        self.add_local_storage(name, value)

    # Navigation

    def check_navigation(self):
        self.move_to_element(self.locator.locator_navigation_board_game)

    def this_navigation_meny_board_game(self):
        elem = self.find_element(self.locator.locator_this_navigation_board_game)
        if elem:
            return True
        else:
            return False

    # CREATORS
    def clik_on_logo_new_era(self):
        self.click_on_element(self.locator.locator_new_era)

    def this_page_new_era(self):
        elem = self.find_element(self.locator.locator_this_navigation_board_game)
        if elem:
            return True
        else:
            return False

    def clik_on_igames(self):
        self.click_on_element(self.locator.locator_igames)

    def this_page_igames(self):
        elem = self.find_element(self.locator.locator_igames_this_page)
        if elem:
            return True
        else:
            return False

    def clik_on_logo_fealindigo(self):
        self.click_on_element(self.locator.locator_fealindigo)

    def this_page_fealindigo(self):
        elem = self.find_element(self.locator.locator_fealindigo_this_page)
        if elem:
            return True
        else:
            return False

    def clik_on_logo_game_seven(self):
        self.click_on_element(self.locator.locator_game_seven)

    def this_page_game_seven(self):
        elem = self.find_element(self.locator.locator_game_seven_this_page)
        if elem:
            return True
        else:
            return False

    def click_show_more_button(self):
        self.click_on_element(self.locator.locator_show_more)

    def more_is_show(self):
        self.scroll_to_element(self.locator.locator_show_more_open)
        elem = self.find_element(self.locator.locator_show_more_open)
        if elem:
            return True
        else:
            return False

    # CAROUSEL

    def click_on_carousel_page(self):
        self.click_on_element(self.locator.locator_carousel)

    def click_next(self):
        self.click_on_element(self.locator.locator_btn_right)

    def click_prev(self):
        self.click_on_element(self.locator.locator_btn_left)

    def carouse(self):
        elem = self.find_element(self.locator.locator_carousel_this_page)
        if elem:
            return True
        else:
            return False

    def click_sale_method(self):
        self.click_on_element(self.locator.locator_sale)
        return HeaderPage(self.driver)

