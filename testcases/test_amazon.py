import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("test_setup")
class TestAddToWishList():
    def test_amazon_add_to_wish_list(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)

        home_page.user_is_on_homepage("amazon")
        home_page.user_see_true_page_title()
        home_page.user_clicks_sign_in()
        login_page.user_signs_up()

