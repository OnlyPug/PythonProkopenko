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
        self.locator_page_sale = ['xpath', '//h1[@class="main-h"][contains(text(), "Дисконт")]']

        self.locator_wait_selector_search = ['xpath', '//div[@class="session-messages"]']
        self.locator_wait_page = ['xpath', '//h1[@class="main-h"][contains(text(), "Результати пошуку «мафія»")]']

        # Xpath call_us_section
        self.locator_call_us = ['xpath', '//div[@class="phones__container"]']
        self.locator_call_us_back = ['xpath', '//div[@class="phones__container"]//a[@class="phones__callback-link"]']
        self.locator_pop_up_call_back = ['xpath', '//section[@id="call-me"]']
        self.locator_pop_up_call_back_name = ['xpath', '//section[@id="call-me"]//input[@class="field j-focus"]']
        self.locator_pop_up_call_back_number = ['xpath', '//section[@id="call-me"]//input[@class="field j-phone j-phone-masked"]']
        self.locator_pop_up_call_back_send = ['xpath', '//section[@id="call-me"]//input[@class="btn-input"]']

        # Xpath login
        self.locator_login = ['xpath', '//div[@class="userbar j-user-tabs"]']
        self.locator_login_pop_up = ['xpath', '//section[@id="sign-in"]']
        self.locator_user_email = ['xpath', '//section[@id="sign-in"]//input[@type="email"]']
        self.locator_user_password = ['xpath', '//*[@id="login_form_id"]/dl/dd[2]/input']
        self.locator_user_password_login = ['xpath', '//*[@id="login_form_id"]/dl/dd[3]/span[1]/input']
        self.locator_user_error = ['xpath', '//div[@class="session-message s-error"]']
        self.locator_login_close = ['xpath', '//section[@id="sign-in"]//a[@class="popup-close"]']

        # Xpath new user
        self.locator_registration = ['xpath', '//div[@class="login-tabs j-auth-tabs"]/a[2]']
        self.locator_registration_name = ['xpath', '//*[@id="signup-form"]/dl/dd[1]/input']
        self.locator_registration_email_address = ['xpath', '//*[@id="signup-form"]/dl/dd[2]/input']
        self.locator_registration_password = ['xpath', '//*[@id="signup-form"]/dl/dd[3]/input']
        self.locator_registration_btn = ['xpath', '//*[@id="signup-form"]/dl/dd[4]/span/input']
        self.locator_registration_error = ['xpath', '//*[@id="signup-form"]/dl/dd[1]/div/div']


