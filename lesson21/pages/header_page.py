from lesson21.pages.base_pages import BasePage
from lesson21.core import HeaderLocators


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = HeaderLocators()

    def input_text_on_search(self):
        self.input_text(locator=self.locator.locator_search, text='мафія')

    def wait_search_selection(self):
        self.wait_util_element_presents(self.locator.locator_wait_selector_search)

    def click_on_search_button(self):
        self.click_on_element(self.locator.locator_button_search)

    def page_load(self):
        self.wait_util_element_presents(self.locator.locator_wait_page)

    def this_page_after_search_mafia(self):
        elem = self.find_element(self.locator.locator_search_mafia)
        if elem:
            return True
        else:
            return False

    def click_on_about_us_button(self):
        self.click_on_element(self.locator.locator_about_us)

    def this_page_about_us(self):
        elem = self.find_element(self.locator.locator_page_about_us)
        if elem:
            return True
        else:
            return False

    def click_blogs_news_button(self):
        self.click_on_element(self.locator.locator_blogs_news)

    def this_page_blogs_news(self):
        elem = self.find_element(self.locator.locator_page_blogs_news)
        if elem:
            return True
        else:
            return False

    def click_vidavnitstvo_button(self):
        self.click_on_element(self.locator.locator_vidavnitstvo)

    def this_page_vidavnitstvo(self):
        elem = self.find_element(self.locator.locator_page_vidavnitstvo)
        if elem:
            return True
        else:
            return False
