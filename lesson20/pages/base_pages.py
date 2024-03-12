
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, time_wait=40):
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
