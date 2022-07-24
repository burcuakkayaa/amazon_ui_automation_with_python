from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WishlistPage(BasePage):

    DELETE_BUTTON = (By.XPATH, "(//input[@name='submit.deleteItem'])[1]")
    DELETED_MESSAGE = (By.XPATH, "//div[text()='Deleted']")

    def __init__(self, driver):
        super().__init__(driver)
        self.__xpath = None
        self.__product_locator = None

    def verify_wish_list_page_is_open(self):
        self.wait_for_load()
        self.url_contains("_view_your_list")

    def verify_product_have_been_added_successfully(self):
        self.__xpath = "//h2/a[@title='" + BasePage._product_name + "']"
        self.__product_locator = (By.XPATH, self.__xpath)

        assert self.element_is_displayed(self.__product_locator) is True

    def delete_product_on_the_wishlist(self):
        self.clickable_and_click(self.DELETE_BUTTON)
        self.wait_for_load()
        print(self.__product_locator)
        assert self.element_is_displayed(self.DELETED_MESSAGE) is True
        assert self.element_is_displayed(self.__product_locator) is False


