from selenium.webdriver.common.by import By

from configfiles.config import TestData
from pages.base_page import BasePage


class CategoryPage(BasePage):
    CATEGORY_RESULT_TEXT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    SEARCH_RESULTS = (By.XPATH, '//span[@class=\'a-size-medium a-color-base a-text-normal\']')

    def __init__(self, driver):
        super().__init__(driver)
        self.element_list = None

    def verify_search_results(self):
        self.url_contains(TestData.SEARCH)
        assert self.element_is_visible(self.CATEGORY_RESULT_TEXT) is True
        assert TestData.SEARCH in self.get_element_text(self.CATEGORY_RESULT_TEXT)

    def user_clicks_search_result(self, result_number):
        self.elements_are_presence(self.SEARCH_RESULTS)
        self.visibility_of_all_elements_located(self.SEARCH_RESULTS)
        element_list = self.get_web_elements(self.SEARCH_RESULTS)

        element = element_list[result_number-1]
        self.scroll_in_the_middle_of_element(element)
        element.click()
