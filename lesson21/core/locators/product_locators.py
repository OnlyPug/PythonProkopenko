class ProductLocators:
    def __init__(self, number=None):
        self.locator_product = ['xpath', '//div[@class="product-header__code"]']
        self.locator_btn_up = ['xpath', '//a[@class="upButton-btn"]']

        # Xpath comment
        self.locator_comment = ['xpath', '//div[@id="comments"]']
        self.locator_comment_check = ['xpath', '//div[@class="product__column-item"]//a[@href="#vіdguki-0"][@class="product-heading__tab is-active"]']
        self.locator_name = ['xpath', '//div[@class="p-review-add__form-item"]/input[@type="text"]']
        self.locator_email = ['xpath', '//div[@class="p-review-add__form-item"]/input[@type="email"]']
        self.locator_text = ['xpath', '//div[@class="p-review-add__form-item"]/textarea[@name="form[text]"]']
        self.locator_stars = ['xpath', '//div[@class="productRating-select j-rate-stars"]/div[@class="productRating-star"][1]']
        self.locator_stars_check = ['xpath', '//div[@class="productRating-select j-rate-stars"]/div[@class="productRating-star __active"][1]']

        # Xpath PDF
        self.locator_pdf = ['xpath', '//li[@class="files__item"][1]//div[@class="files__item-icon"][1]']
        self.locator_pdf_page = ['xpath', '//iframe[@id="__acrobatNewDialog__"]']

        # Xpath pages
        self.locator_together_next = ['xpath', '//div[@class="carousel-btn carousel-btn--next"]']
        self.locator_together_check2 = ['xpath', '//div[@class="carousel-pagination j-products-set-pagination swiper-pagination-clickable swiper-pagination-bullets"]/span[2]']
        self.locator_together_check3 = ['xpath', '//div[@class="carousel-pagination j-products-set-pagination swiper-pagination-clickable swiper-pagination-bullets"]/span[3]']
        self.locator_together_check4 = ['xpath', '/div[@class="carousel-pagination j-products-set-pagination swiper-pagination-clickable swiper-pagination-bullets"]/span[4]']
        self.locator_together_check5 = ['xpath', '/div[@class="carousel-pagination j-products-set-pagination swiper-pagination-clickable swiper-pagination-bullets"]/span[5]']
        self.locator_together_check6 = ['xpath', '/div[@class="carousel-pagination j-products-set-pagination swiper-pagination-clickable swiper-pagination-bullets"]/span[6]']

        # Xpath from Product page
        self.locators_basket = ['xpath', '//div[@class="product-order__block product-order__block--buy"]//span[@class="btn-content"]']