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

    def this_page_sale(self):
        elem = self.find_element(self.locator.locator_page_sale)
        if elem:
            return True
        else:
            return False

    # CALL US SECTION

    def move_on_call_us_section(self):
        self.move_to_element(self.locator.locator_call_us)

    def call_us_section_snow(self):
        elem = self.find_element(self.locator.locator_call_us_back)
        if elem:
            return True
        else:
            return False

    def click_call_us_back(self):
        self.click_on_element(self.locator.locator_call_us_back)

    def call_us_pop_up_snow(self):
        elem = self.find_element(self.locator.locator_pop_up_call_back)
        if elem:
            return True
        else:
            return False

    def input_name(self, text=None):
        self.click_on_element(self.locator.locator_pop_up_call_back_name)
        self.input_text(self.locator.locator_pop_up_call_back_name, text=text)

    def input_number(self, text=None):
        self.click_on_element(self.locator.locator_pop_up_call_back_number)
        self.input_text(self.locator.locator_pop_up_call_back_number, text=text)

    def is_send_button(self):
        elem = self.find_element(self.locator.locator_pop_up_call_back_send)
        if elem:
            return True
        else:
            return False

    # Login section

    def click_login_button(self):
        self.click_on_element(self.locator.locator_login)

    def login_pop_up_snow(self):
        elem = self.find_element(self.locator.locator_login_pop_up)
        if elem:
            return True
        else:
            return False

    def input_user_name(self, text=None):
        self.click_on_element(self.locator.locator_user_email)
        self.input_text(self.locator.locator_user_email, text=text)

    def input_user_password(self, text=None):
        self.click_on_element(self.locator.locator_user_password)
        self.input_text(self.locator.locator_user_password, text=text)

    def is_login_button(self):
        elem = self.find_element(self.locator.locator_user_password)
        if elem:
            return True
        else:
            return False

    def click_login_user_button(self):
        self.click_on_element(self.locator.locator_user_password_login)

    def error_shown(self):
        elem = self.find_element(self.locator.locator_user_error)
        if elem:
            return True
        else:
            return False

    def click_close_pop_up(self):
        self.click_on_element(self.locator.locator_login_close)

    def pop_up_close(self):
        elem = self.find_element(self.locator.locator_login)
        if elem:
            return True
        else:
            return False

    def click_new_user_button(self):
        self.click_on_element(self.locator.locator_registration)

    def this_page_registration(self):
        elem = self.find_element(self.locator.locator_registration_name)
        if elem:
            return True
        else:
            return False

    def input_first_second_name(self, text=None):
        self.input_text(self.locator.locator_registration_name, text=text)

    def input_new_user_password(self, text=None):
        self.input_text(self.locator.locator_registration_password, text=text)

    def input_new_email_password(self, text=None):
        self.click_on_element(self.locator.locator_registration_email_address)
        self.input_text(self.locator.locator_registration_email_address, text=text)

    def is_registration_button(self):
        elem = self.find_element(self.locator.locator_registration_btn)
        if elem:
            return True
        else:
            return False

    def click_registration_user_button(self):
        self.click_on_element(self.locator.locator_registration_btn)

    def error_registration_shown(self):
        elem = self.find_element(self.locator.locator_registration_error)
        if elem:
            return True
        else:
            return False
