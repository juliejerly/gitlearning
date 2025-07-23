from pages.base_page import BasePage
from pages.home_page import HomePage


class CartPage(BasePage):
    selector = "data-test=title"
    expected = "Your Cart"
    inventory_item_name = ".inventory_item_name"

    def verify_cart_page_is_displayed(self):
        self.verify_current_page(self.selector, self.expected)

    def get_added_item_name_view_cart(self):
        return self.get_text(self.inventory_item_name)




