from lesson21.pages.base_pages import BasePage


class ComicsBookPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_navigation_test(self, category, item_list):
        self.move_to_element(category)
        results = []
        for item in item_list:
            item_obj = self.wait_util_element_presents(item)
            results.append(item_obj.is_displayed())
        return all(results)
