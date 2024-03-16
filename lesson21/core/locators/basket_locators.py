class BasketLocators:
    def __init__(self):
        # Xpath from Product page
        self.locators_this_page = ['xpath', '//div[@class="popup-block"]//div[text()="Кошик"]']

        # Xpath Basket
        self.locators_product_check = ['xpath', '//*[@id="product_a34d19071922bd1c7a8348ec0cd6c51f"]/td[2]/div[1]/a']
        self.locators_add_btn = ['xpath', '//section[@id="cart"]//button[@class="counter-btn __plus j-increase-p"]']
        self.locators_check_text = ['xpath', '//section[@id="cart"]//input[@class="counter-field j-quantity-p"]']
        self.locators_back_to_product = ['xpath', '//section[@id="cart"]//button[@class="btn __clear"]']
        self.locators_cross_to_product = ['xpath', '//section[@id="cart"]//a[@class="popup-close"]']

        # Xpath from Header



