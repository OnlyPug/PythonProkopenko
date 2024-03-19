class MainPageLocators:
    def __init__(self):
        self.locator_strategy = ['xpath', '//div[@class="frontCategories-carousel"]//li[4]']

        # NAVIGATION
        self.locator_navigation_board_game = ['xpath', '//div[@class="header__bottom"]//a[@href="/catalog/"]']
        self.locator_this_navigation_board_game = ['xpath',
                                                   '//li[@class="productsMenu-submenu-i "]//a[@href="/novinki/"]']

        # CREATORS
        self.locator_new_era = ['xpath', '//div[@class="layout-wrap"]//a[@href="/nova-era/"]']
        self.locator_new_era_this_page = ['xpath', '//div[@class="catalog__top-col catalog__top-col--left"]//h1[text()="Нова Ера"]']

        self.locator_igames = ['xpath', '//div[@class="layout-wrap"]//a[@href="/igames/"]']
        self.locator_igames_this_page = ['xpath', '//div[@class="catalog__top-col catalog__top-col--left"]//h1[text()="IGAMES"]']

        self.locator_fealindigo = ['xpath', '//div[@class="layout-wrap"]//a[@href="/feelindigo/"]']
        self.locator_fealindigo_this_page = ['xpath', '//div[@class="catalog__top-col catalog__top-col--left"]//h1[text()="Feelindigo"]']

        self.locator_game_seven = ['xpath', '//div[@class="layout-wrap"]//a[@href="/games-7-days/"]']
        self.locator_game_seven_this_page = ['xpath', '//div[@class="catalog__top-col catalog__top-col--left"]//h1[text()="Games 7 Days"]']

        self.locator_show_more = ['xpath', '//div[@class="frontBrands-expander"]/a']
        self.locator_show_more_open = ['xpath', '//div[@class="frontBrands-container"]//a[@href="/brands/"]']

        # CAROUSEL

        self.locator_carousel = ['xpath', '//div[@class="banners-pagination j-banners-pagination swiper-pagination-clickable swiper-pagination-bullets"]/span[@class="banners-pagination__bullet"][4]']
        self.locator_carousel_this_page = ['xpath', '//div[@class="banners-pagination j-banners-pagination swiper-pagination-clickable swiper-pagination-bullets"]/span[@class="banners-pagination__bullet is-active"]']
        self.locator_btn_left = ['xpath', '//div[@class="banners-arrow banners-arrow--prev j-banners-arrow-prev"]/div[@class="banners-arrow__icon"]']
        self.locator_btn_right = ['xpath', '//div[@class="banners-arrow banners-arrow--next j-banners-arrow-next"]/div[@class="banners-arrow__icon"]']

        # INFORMATION

        self.locator_sale = ['xpath', '//div[@class="frontBenefits-txt-h"][text()="Найкращі  ціни "]']