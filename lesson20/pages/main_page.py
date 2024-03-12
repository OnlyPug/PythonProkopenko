from lesson20.pages.base_pages import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_strategy = ['xpath', '//div[@class="frontCategories-carousel"]//li[4]']

    def this_main_page(self):
        elem = self.find_element(self.locator_strategy)
        if elem:
            return True
        else:
            return False

    def click_strategy(self):
        self.click_on_element(self.locator_strategy)
