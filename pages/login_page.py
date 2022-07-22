from selenium.webdriver.common.by import By

from configfiles.config import TestData
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_TEXT_AREA = (By.ID, "ap_email")
    CONTINUE_BUTTON = (By.ID, "continue")
    PASSWORD_TEXT_AREA = (By.ID, "ap_password")
    SIGN_IN_BUTTON = (By.ID, "signInSubmit")

    def __init__(self, driver):
        super().__init__(driver)

    def user_signs_up(self):
        self.element_is_visible(self.EMAIL_TEXT_AREA)
        self.send_key(self.EMAIL_TEXT_AREA, TestData.EMAIL)
        self.clickable_and_click(self.CONTINUE_BUTTON)

        self.wait_for_load()
        self.element_is_visible(self.PASSWORD_TEXT_AREA)
        self.send_key(self.PASSWORD_TEXT_AREA, TestData.PASSWORD)

        self.element_is_presence(self.SIGN_IN_BUTTON)
        self.clickable_and_click(self.SIGN_IN_BUTTON)


