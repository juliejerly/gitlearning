import time

import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


# @pytest.mark.xdist_group(name="settings")
class TestsE2eFlow:

    @pytest.mark.parametrize("credentials, selector, expected", [
        ("INVALID_CREDENTIALS", "data-test=error",
         "Epic sadface: Username and password do not match any user in this service"),
        ("VALID_CREDENTIALS", ".title", "Products")
    ])
    def test_login(self, page, get_test_data, credentials, selector, expected):
        login_page = LoginPage(page)
        creds = get_test_data[credentials]
        url = get_test_data["URLS"]["QA_URL"]
        login_page.enter_credentials(url, creds["USERNAME"], creds["PASSWORD"])
        home_page = HomePage(page)
        home_page.verify_page(selector, expected)

    def test_add_to_cart(self, page):
        home_page = HomePage(page)
        self.added_item_name = home_page.get_first_item_name()
        home_page.click_add_to_cart()
        home_page.click_shopping_cart_link()

    def test_view_cart(self, page):
        cart_page = CartPage(page)
        cart_page.verify_cart_page_is_displayed()
        self.view_cart_added_item_name = cart_page.get_added_item_name_view_cart()
        # assert self.added_item_name == self.view_cart_added_item_name

