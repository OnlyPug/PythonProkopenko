class HeaderLocators:
    def __init__(self):
        # Xpath search
        self.locator_search = ['xpath', '//input[@class="search__input"]']
        self.locator_button_search = ['xpath', '//li[@class="search-results__item"]/a[@class="search-results__link search-results__link--all"]']
        self.locator_search_mafia = ['xpath', '//h1[@class="main-h"][contains(text(), "Результати пошуку «мафія»")]']

        # Xpath information
        self.locator_about_us = ['xpath', '//span[@class="site-menu__item"]/a[contains(text(), "Про нас")]']
        self.locator_page_about_us = ['xpath', '//h1[@class="main-h"][contains(text(), "Про нас")]']
        self.locator_blogs_news = ['xpath', '//span[@class="site-menu__item"]/a[contains(text(), "Блог та новини")]']
        self.locator_page_blogs_news = ['xpath', '//h1[@class="main-h"][contains(text(), "Блог та новини")]']
        self.locator_vidavnitstvo = ['xpath', '//span[@class="site-menu__item"]/a[contains(text(), "Видавництво Нова Ера")]']
        self.locator_page_vidavnitstvo = ['xpath', '//h1[@class="main-h"][contains(text(), "Видавництво Нова Ера")]']

        self.locator_wait_selector_search = ['xpath', '//div[@class="session-messages"]']
        self.locator_wait_page = ['xpath', '//h1[@class="main-h"][contains(text(), "Результати пошуку «мафія»")]']