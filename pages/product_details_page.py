from selenium.webdriver.common.by import By

from configfiles.config import TestData
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):

    ADD_TO_LIST_BUTTON = (By.ID, "wishListMainButton")
    WISH_LIST_NAME_TEXTBOX = (By.ID, "list-name")
    CREATE_WISH_LIST_BUTTON = (By.XPATH, "//span[@class='a-button a-button-primary']")
    CLOSE_WISH_LIST_POP_UP = (By.XPATH, "//button[contains(@class,'a-button-close a-declarative')]")
    VIEW_WISH_LIST_BUTTON = (By.ID, "huc-view-your-list-button")
    PRODUCT_TITLE = (By.ID, "productTitle")

    def __init__(self, driver):
        super().__init__(driver)

    def verifyOpenProductDetailsPage(self, search_product, product_number):
        self.wait_for_load()
        self.url_contains(TestData.SEARCH)
        assert "ref=sr_1_" + str(TestData.PRODUCT_NUMBER) in self.driver.current_url

    def add_to_wishlist(self):
        self.wait_for_load()
        self.scroll_page_down_with(400)

        BasePage._product_name = self.get_element_text(self.PRODUCT_TITLE)
        print(BasePage._product_name)

        self.element_is_visible(self.ADD_TO_LIST_BUTTON)
        self.clickable_and_click(self.ADD_TO_LIST_BUTTON)
        try:
            self.element_is_presence(self.WISH_LIST_NAME_TEXTBOX)
            self.clickable_and_click(self.CREATE_WISH_LIST_BUTTON)
        except Exception:
            pass

        self.clickable_and_click(self.VIEW_WISH_LIST_BUTTON)

