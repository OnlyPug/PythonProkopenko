from lesson20.pages.base_pages import BasePage


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Xpath search
        self.search = ['xpath', '//input[@class="search__input"]']
        self.button_search = ['xpath', '//li[@class="search-results__item"]/a[@class="search-results__link search-results__link--all"]']
        self.search_mafia = ['xpath', '//h1[@class="main-h"][contains(text(), "Результати пошуку «мафія»")]']

        # Xpath information
        self.about_us = ['xpath', '//span[@class="site-menu__item"]/a[contains(text(), "Про нас")]']
        self.page_about_us = ['xpath', '//h1[@class="main-h"][contains(text(), "Про нас")]']
        self.blogs_news = ['xpath', '//span[@class="site-menu__item"]/a[contains(text(), "Блог та новини")]']
        self.page_blogs_news = ['xpath', '//h1[@class="main-h"][contains(text(), "Блог та новини")]']
        self.vidavnitstvo = ['xpath', '//span[@class="site-menu__item"]/a[contains(text(), "Видавництво Нова Ера")]']
        self.page_vidavnitstvo = ['xpath', '//h1[@class="main-h"][contains(text(), "Видавництво Нова Ера")]']

        self.wait_selector_search = ['xpath', '//div[@class="session-messages"]']
        self.wait_page = ['xpath', '//h1[@class="main-h"][contains(text(), "Результати пошуку «мафія»")]']

    def input_text_on_search(self):
        self.input_text(locator=self.search, text='мафія')

    def wait_search_selection(self):
        self.wait_util_element_presents(self.wait_selector_search)

    def click_on_search_button(self):
        self.click_on_element(self.button_search)

    def page_load(self):
        self.wait_util_element_presents(self.wait_page)

    def this_page_after_search_mafia(self):
        elem = self.find_element(self.search_mafia)
        if elem:
            return True
        else:
            return False

    def click_on_about_us_button(self):
        self.click_on_element(self.about_us)

    def this_page_about_us(self):
        elem = self.find_element(self.page_about_us)
        if elem:
            return True
        else:
            return False

    def click_blogs_news_button(self):
        self.click_on_element(self.blogs_news)

    def this_page_blogs_news(self):
        elem = self.find_element(self.page_blogs_news)
        if elem:
            return True
        else:
            return False

    def click_vidavnitstvo_button(self):
        self.click_on_element(self.vidavnitstvo)

    def this_page_vidavnitstvo(self):
        elem = self.find_element(self.page_vidavnitstvo)
        if elem:
            return True
        else:
            return False




