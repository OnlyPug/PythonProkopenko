class StrategyLocators:
    def __init__(self):
        self.locator_strategy_page = ['xpath',
                                      '//div[@class="breadcrumbs-i"]/span[@content="https://gameland.com.ua/strategii/"]']
        # Xpath for sort
        self.locator_lover_price = ['xpath', '//div[@class="catalog-sorting__list"]//span[2]']
        self.locator_max_price = ['xpath', '//div[@class="catalog-sorting__list"]//span[3]']
        self.locator_popular = ['xpath', '//div[@class="catalog-sorting__list"]//span[1]']
        self.locator_name = ['xpath', '//div[@class="catalog-sorting__list"]//span[4]']
        self.locator_wait_page = ['xpath', '//span[@class="catalog-sorting__item is-active j-catalog-sorting-button"]']

        # Xpath for check-box
        self.locator_check_box = ['xpath', '//span[@class="filter-title"][contains(text(), "Актерська гра")]']
        self.locator_page_check_box = ['xpath', '//a[@class="filter-current-i"]']

        # Xpath for product
        self.locator_first_strategy_game = ['xpath', '//ul//li[1]//div[@class="catalogCard-main-b"]']
