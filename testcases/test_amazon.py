import pytest

from configfiles.config import TestData
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from pages.wish_list_page import WishlistPage


@pytest.mark.usefixtures("test_setup")
class TestAddToWishList():
    def test_amazon_add_to_wish_list(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        category_page = CategoryPage(self.driver)
        product_details_page = ProductDetailsPage(self.driver)
        wish_list_page = WishlistPage(self.driver)

        home_page.user_is_on_homepage(TestData.PAGE_NAME)
        home_page.verify_page_title()

        home_page.user_clicks_sign_in()
        login_page.user_fills_email_and_password()

        home_page.user_searches(TestData.SEARCH)
        category_page.verify_search_results()
        category_page.user_clicks_search_result(TestData.PRODUCT_NUMBER)

        product_details_page.verifyOpenProductDetailsPage(TestData.SEARCH, TestData.PRODUCT_NUMBER)
        product_details_page.add_to_wishlist()

        wish_list_page.verify_wish_list_page_is_open()
        wish_list_page.verify_product_have_been_added_successfully()
        wish_list_page.delete_product_on_the_wishlist()


