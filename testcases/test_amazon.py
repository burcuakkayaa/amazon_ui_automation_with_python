import pytest


@pytest.mark.usefixtures("test_setup")
class TestAddToWishList():
    def test_amazon_add_to_wish_list(self):
        print("lets do it")
