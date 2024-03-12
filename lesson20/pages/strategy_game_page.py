from lesson20.pages.base_pages import BasePage


class StrategyGamePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator_strategy_page = ['xpath', '//div[@class="breadcrumbs-i"]/span[@content="https://gameland.com.ua/strategii/"]']
        # Xpath for sort
        self.lover_price = ['xpath', '//div[@class="catalog-sorting__list"]//span[2]']
        self.max_price = ['xpath', '//div[@class="catalog-sorting__list"]//span[3]']
        self.popular = ['xpath', '//div[@class="catalog-sorting__list"]//span[1]']
        self.name = ['xpath', '//div[@class="catalog-sorting__list"]//span[4]']
        self.wait_page = ['xpath', '//span[@class="catalog-sorting__item is-active j-catalog-sorting-button"]']

        # Xpath for check-box
        self.check_box = ['xpath', '//span[@class="filter-title"][contains(text(), "Актерська гра")]']
        self.page_check_box =['xpath', '//a[@class="filter-current-i"]']

    def this_page_strategy_game(self):
        elem = self.find_element(self.locator_strategy_page)
        if elem:
            return True
        else:
            return False

    # Functionality for sort
    def click_lover_prise(self):
        self.click_on_element(self.lover_price)

    def click_max_prise(self):
        self.click_on_element(self.max_price)

    def load_page(self, page):
        self.wait_util_element_presents(page)

    def click_popular(self):
        self.click_on_element(self.popular)

    def click_name(self):
        self.click_on_element(self.name)

    # Functionality for check box

    def click_on_check_box(self):
        self.scroll_to_element_and_click(self.check_box)
