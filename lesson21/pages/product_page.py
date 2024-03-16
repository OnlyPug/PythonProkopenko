import time

from lesson21.pages.base_pages import BasePage
from lesson21.core import ProductLocators
from lesson21.pages.basket_page import BasketPage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = ProductLocators()

    def this_page(self):
        elem = self.find_element(self.locator.locator_product)
        if elem:
            return True
        else:
            return False

    # COMMENT CHECK

    def click_on_comment(self):
        self.wait_util_element_presents(self.locator.locator_comment)
        self.click_on_element(self.locator.locator_comment)

    def comments_opened(self):
        elem = self.find_element(self.locator.locator_comment_check)
        if elem:
            return True
        else:
            return False

    def input_name(self):
        self.scroll_to_element(self.locator.locator_name)
        self.input_text(locator=self.locator.locator_name, text='Anastasiia')

    def input_email(self):
        self.input_text(locator=self.locator.locator_email, text='sdfjnsjdfsdf')

    def input_text_comment(self):
        self.scroll_to_element(self.locator.locator_text)
        self.input_text(locator=self.locator.locator_text,
                        text='On your site, you don`t check email. One star for this')

    def click_on_stars(self):
        self.click_on_element(self.locator.locator_stars)

    def check_one_stars(self):
        self.find_element(self.locator.locator_stars_check)

    # PDF CHECK
    def click_on_pdf_button(self):
        self.scroll_to_element_and_click(self.locator.locator_pdf)

    def this_pdf_page(self):
        elem = self.find_element(self.locator.locator_pdf_page)
        if elem:
            return True
        else:
            return False

    def click_to_top(self):
        self.click_on_element(self.locator.locator_btn_up)

    def close_second_tab(self):
        self.close_window(1)

    # Functionality for 'Разом дешевше'

    def click_next_btn(self):
        time.sleep(2)
        self.click_on_element(self.locator.locator_together_next)

    def check_page2(self):
        elem = self.find_element(self.locator.locator_together_check2)
        if elem:
            return True
        else:
            return False

    def check_page3(self):
        elem = self.find_element(self.locator.locator_together_check3)
        if elem:
            return True
        else:
            return False

    def check_page4(self):
        elem = self.find_element(self.locator.locator_together_check4)
        if elem:
            return True
        else:
            return False

    def check_page5(self):
        elem = self.find_element(self.locator.locator_together_check5)
        if elem:
            return True
        else:
            return False

    def check_page6(self):
        elem = self.find_element(self.locator.locator_together_check6)
        if elem:
            return True
        else:
            return False

    # From product to Basket

    def on_product_page(self):
        self.click_on_element(self.locator.locators_basket)
        return BasketPage(self.driver)
