from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, time_wait=50):
        self.driver = driver
        self.web_driver_wait = WebDriverWait(driver, time_wait)

    def wait_util_element_presents(self, locator: tuple[str, str]):
        return self.web_driver_wait.until(EC.presence_of_element_located(locator))

    def click_on_element(self, locator: tuple[str, str]):
        element = self.wait_util_element_presents(locator)
        element.click()

    def find_element(self, locator):
        element = self.wait_util_element_presents(locator)
        return element

    def scroll_to_element_and_click(self, locator: tuple[str, str]):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(200, 200).perform()
        self.click_on_element(locator)

    def input_text(self, locator, text):
        element = self.find_element(locator=locator)
        element.send_keys(text)

    def check_value(self, locator: tuple[str, str]):
        element = self.find_element(locator=locator)
        value = element.get_attribute("value")
        return value

    def scroll_to_element(self, locator: tuple[str, str]):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(200, 200).perform()
        self.find_element(locator)

    def close_window(self, index):
        browser_tabs = self.driver.window_handles
        if index < len(browser_tabs):
            self.driver.switch_to.window(browser_tabs[index])
            self.driver.close()

    def move_to_element(self, locator: tuple[str]):
        element = self.find_element(locator=locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def click_back(self):
        self.driver.back()

    # COOKIES

    def get_cookies(self):
        cookies = self.driver.get_cookies()
        return print(f'Cookies: {cookies}')

    def add_cookies(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    # LOCAL STORAGE

    def add_local_storage(self, name, value):
        self.driver.execute_script(f'window.localStorage["{name}"]="{value}"')

    def is_element_clicable(self, locator: tuple[str]):
        self.driver.find_element(locator=locator)
