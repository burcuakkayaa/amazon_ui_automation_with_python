from selenium.webdriver.common.by import By

from configfiles.config import TestData
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):

    ADD_TO_LIST_BUTTON = (By.CSS_SELECTOR, "#add-to-wishlist-button-submit")
    WISH_LIST_MODAL = (By.CSS_SELECTOR, "#a-popover-7")
    WISH_LIST_NAME_TEXTBOX = (By.ID, "list-name")

    def __init__(self, driver):
        super().__init__(driver)

    def verifyOpenProductDetailsPage(self, search_product, product_number):
        self.wait_for_load()
        self.url_contains(TestData.SEARCH)
        assert "ref=sr_1_" + str(TestData.PRODUCT_NUMBER) in self.driver.current_url

    def add_to_wishlist(self):
        self.wait_for_load()
        self.scroll_page_down(self.ADD_TO_LIST_BUTTON)
        self.element_is_visible(self.ADD_TO_LIST_BUTTON)
        self.clickable_and_click(self.ADD_TO_LIST_BUTTON)
        self.element_is_presence(self.WISH_LIST_MODAL)
