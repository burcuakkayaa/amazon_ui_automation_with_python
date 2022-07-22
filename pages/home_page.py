import time

from selenium.webdriver.common.by import By

from configfiles.config import TestData
from pages.base_page import BasePage


class HomePage(BasePage):
    SIGN_IN = (By.ID, "nav-link-accountList")

    def __init__(self, driver):
        super().__init__(driver)

    def user_is_on_homepage(self, site):
        self.wait_for_load()
        print(self.driver.current_url)
        self.url_contains(site)

    def user_see_true_page_title(self):
        print(self.driver.title)
        self.title_contains(TestData.BASE_TITLE)
        assert TestData.BASE_TITLE in self.driver.title

    def user_clicks_sign_in(self):
        self.clickable_and_click(self.SIGN_IN)
        assert self.driver != TestData.BASE_URL







